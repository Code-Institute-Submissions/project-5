import os
import pygal
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

from classes import Search, SearchForm, Database, Recipe, Charts

app = Flask(__name__)

app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

users_collection = mongo.db.users
recipes_collection = mongo.db.recipes
shemas_collection = mongo.db.schemas
forms_collection = mongo.db.forms
trivia_collection = mongo.db.trivia

recipe_schema_id = "5ba2ded543277a316cbf0ef9"


"""

index.html

"""


@app.route('/')
@app.route('/index')
def index():
    forms = forms_collection.find()
    trivia = Search(trivia_collection).random(num_of_results=1)
    random_recipes = [x for x in Search(
        recipes_collection).random(num_of_results=4)]
    main_recipe = random_recipes[0]
    side_recipes = random_recipes[1:]

    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("index.html", page_title="Cookbook", username=session['user'], user_id=user_in_db['_id'], forms=forms, main_recipe=main_recipe, side_recipes=side_recipes, trivia=trivia)
    return render_template("index.html", page_title="Cookbook", forms=forms, main_recipe=main_recipe, side_recipes=side_recipes, trivia=trivia)


"""

Users / Log-in / Register

"""

# Login


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['user_password']
        try:
            user_in_db = users_collection.find_one({"username": username})
        except:
            flash("Sorry there seems to be problem with the data")
            return redirect(url_for('index'))
        if user_in_db:
            if check_password_hash(user_in_db['password'], password):
                session['user'] = username
                flash(f"Logged in as {username}")
                return_url = request.referrer
                return redirect(return_url)
            else:
                flash("Invalid username or password")
                return redirect(url_for('index'))
        else:
            flash(f"Sorry no profile {request.form['username']} found")
            return redirect(url_for('index'))


# Sign up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    forms = forms_collection.find()
    if request.method == "POST":
        user_in_db = mongo.db.users.find_one(
            {"username": request.form['username']})
        if user_in_db:
            flash(f"Sorry profile {request.form['username']} already exist")
            return render_template("sign-up.html", page_title="Sign up", forms=forms)
        hashed_pass = generate_password_hash(request.form['user_password'])
        users_collection.insert_one(
            {'username': request.form['username'],
             'email': request.form['email'],
             'password': hashed_pass,
             'recipes': [],
             'votes': []})
        user_in_db = users_collection.find_one(
            {"username": request.form['username']})
        session['user'] = request.form['username']
        return redirect(url_for('profile', user_id=user_in_db['_id'], forms=forms))
    if 'user' in session:
        return render_template("sign-up.html", page_title="Sign up", username=session['user'], forms=forms)
    return render_template("sign-up.html", page_title="Sign up", forms=forms)

# Log out


@app.route('/logout')
def logout():
    session.pop('user')
    flash("Successfully logged out ...")
    return_url = request.referrer
    return redirect(return_url)

# Profile Page


@app.route('/profile/<user_id>')
def profile(user_id):
    forms = forms_collection.find()
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        recipes = recipes_collection.find({"creditsText": session['user']})
        return render_template("profile.html", page_title="profile", user_in_db=user_in_db, user_id=user_in_db['_id'], recipes=[x for x in recipes], forms=forms)
    flash("Please log in first")
    return redirect(url_for('index', forms=forms))


"""

Recipes


"""

# Main route for all recipes


@app.route('/recipes')
def recipes():
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    recipes_in_db = Search(recipes_collection, pagination_base="recipes",
                           limit=pagination_limit, offset=pagination_offset).sort_find_all()
    forms = forms_collection.find()
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"], limit=pagination_limit, offset=pagination_offset,  user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)

# Main route for single recipe


@app.route('/recipe/<recipe_id>', methods=['GET', 'POST'])
def recipe(recipe_id):
    recipe = Search(recipes_collection).find_one_by_id(recipe_id)
    forms = forms_collection.find()
    if request.method == "POST":
        if 'user' in session:
            user_in_db = users_collection.find_one(
                {"username": session['user']})
            return render_template("recipe.html", page_title=recipe['title'], recipe_id=recipe_id, recipe=recipe, forms=forms,  user_in_db=user_in_db, user_id=user_in_db['_id'])
        else:
            return render_template("recipe.html", page_title=recipe['title'], recipe_id=recipe_id, recipe=recipe, forms=forms)
    else:
        if 'user' in session:
            user_in_db = users_collection.find_one(
                {"username": session['user']})
            user_recipe = [x for x in user_in_db['recipes'] if x == recipe_id]
            voted_recipes = [x for x in user_in_db['votes'] if x == recipe_id]
            return render_template("recipe.html", page_title=recipe['title'], recipe_id=recipe_id, recipe=recipe, user_recipe=user_recipe, voted_recipes=voted_recipes, forms=forms,  user_in_db=user_in_db, user_id=user_in_db['_id'])
        else:
            return render_template("recipe.html", page_title=recipe['title'], recipe_id=recipe_id, recipe=recipe, forms=forms)

# Add Recipe


@app.route('/add_recipe/<user_id>', methods=['GET', 'POST'])
def add_recipe(user_id):
    forms = forms_collection.find()
    recipe_schema = Search(shemas_collection).find_one_by_id(recipe_schema_id)
    if request.method == "POST":
        form_data = request.form.to_dict()
        data = Recipe(form_data)
        data = data.__dict__
        new_recipe = recipes_collection.insert(data["recipe"])
        recipe_id = str(new_recipe)
        users_collection.update({"username": session['user']}, {
                                '$push': {'recipes': recipe_id}})
        user_in_db = users_collection.find_one({"username": session['user']})

        flash("Recipe added. Thank you!")
        flash(
            "Please note that your recipe must be approved by admin to be view in the site!")
        flash("However you can still view your recipe trought profile page.")
        return redirect(url_for("recipe", recipe_id=recipe_id))
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("add-recipe.html", page_title="Add recipe", user_in_db=user_in_db, user_id=user_in_db['_id'], forms=forms, recipe_schema=recipe_schema)

    return redirect(url_for('index', forms=forms))

# Edit Recipe


@app.route('/edit_recipe/<recipe_id>/<user_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id, user_id):
    forms = forms_collection.find()
    if request.method == "POST":
        form_data = request.form.to_dict()
        data = Recipe(form_data)
        data = data.__dict__
        recipes_collection.update({'_id': ObjectId(recipe_id)}, data["recipe"])
        recipe = data["recipe"]
        flash("Your recipe has been updated")
        user_in_db = users_collection.find_one({"username": session['user']})
        return redirect(url_for("recipe", page_title=recipe['title'], recipe_id=recipe_id, recipe=recipe, forms=forms, user_in_db=user_in_db, user_id=user_in_db['_id']))
    else:
        if 'user' in session:
            recipe = Search(recipes_collection).find_one_by_id(recipe_id)
            user_in_db = Search(users_collection).find_one_by_id(user_id)
            for x in user_in_db["recipes"]:
                if x == recipe_id:
                    return render_template("edit-recipe.html", page_title="Edit recipe", recipe_id=recipe_id, recipes=recipe, forms=forms,  user_in_db=user_in_db, user_id=user_in_db['_id'])
    return redirect(url_for('index'))


# Delete Recipe


@app.route('/delete_recipe/<recipe_id>/<user_id>', methods=['GET'])
def delete_recipe(recipe_id, user_id):
    user_in_db = Search(users_collection).find_one_by_id(user_id)
    logged_in_user = session.get('user')
    if request.method == "GET":
        if logged_in_user == user_in_db['username']:
            recipes_collection.remove({'_id': ObjectId(recipe_id)})
            users_collection.update({'_id': ObjectId(user_id)}, {
                                    "$pull": {"recipes": recipe_id}})
            flash("Your recipe has been delated")
            return redirect(url_for('index'))
        else:
            flash("Your are NOT allowed to delete this recipe!")
            return redirect(url_for('index'))
    return redirect(url_for('index'))


# Vote up for a recipe


@app.route('/vote_up/<recipe_id>/<user_id>', methods=['GET'])
def vote_up(recipe_id, user_id):
    try:
        user_in_db = Search(users_collection).find_one_by_id(user_id)
    except:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    if recipe_id in user_in_db["votes"]:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    elif recipe_id in user_in_db["recipes"]:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    else:
        votes = Search(recipes_collection).find_one_by_id(recipe_id)
        votes = votes["aggregateLikes"] + 1
        recipes_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"aggregateLikes": votes}})
        users_collection.update({'_id': ObjectId(user_id)}, {
                                '$push': {'votes': recipe_id}})
        flash("Thank you for your vote!")
        return redirect(request.referrer)

# Vote down for a recipe


@app.route('/vote_down/<recipe_id>/<user_id>', methods=['GET'])
def vote_down(recipe_id, user_id):
    try:
        user_in_db = Search(users_collection).find_one_by_id(user_id)
    except:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    if recipe_id in user_in_db["votes"]:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    elif recipe_id in user_in_db["recipes"]:
        flash("Sorry you are not allowed to vote")
        return redirect(url_for('index'))
    else:
        votes = Search(recipes_collection).find_one_by_id(recipe_id)
        votes = votes["aggregateLikes"] - 1
        recipes_collection.update({'_id': ObjectId(recipe_id)}, {
                                  "$set": {"aggregateLikes": votes}})
        users_collection.update({'_id': ObjectId(user_id)}, {
                                '$push': {'votes': recipe_id}})
        flash("Thank you for your vote!")
        return redirect(request.referrer)


"""

Search

"""

# Search view for mobiles


@app.route('/mobile_search', methods=['GET', 'POST'])
def mobile_search():
    forms = forms_collection.find()
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("search-form-sm.html", page_title="Search",  user_id=user_in_db['_id'], forms=forms)
    return render_template("search-form-sm.html", page_title="Search", forms=forms)


# Search via form input

@app.route('/input_form_search', methods=['GET', 'POST'])
def input_form_search():
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    if request.method == "POST":
        form_data = request.form.to_dict()
        session["search"] = form_data
        recipes = SearchForm(
            form_data, pagination_base="input_form_search").search_by_input()
        if recipes == None or recipes == None or recipes["num_of_results"] == 0:
            flash("Sorry did not find any recipes!")
            return_url = request.referrer
            return redirect(return_url)
        else:
            recipes['next_url'] = recipes['next_url'] + \
                f"&input={form_data['search_input']}"
            recipes['previous_url'] = recipes['previous_url'] + \
                f"&input={form_data['search_input']}"
        if 'user' in session:
            user_in_db = users_collection.find_one(
                {"username": session['user']})
            return render_template("recipes.html", user_in_db=user_in_db, user_id=user_in_db['_id'], recipes=recipes["result"], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
        return render_template("recipes.html", recipes=recipes["result"], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
    else:
        if session["search"]:
            form_data = session["search"]
            form_data["limit"] = pagination_limit
            recipes = SearchForm(
                form_data, pagination_base="input_form_search", offset=pagination_offset).search_by_input()
            if recipes == None or recipes["num_of_results"] == 0:
                flash("Sorry did not find any recipes!")
                return_url = request.referrer
                return redirect(return_url)
            else:
                recipes['next_url'] = recipes['next_url'] + \
                    f"&input={form_data['search_input']}"
                recipes['previous_url'] = recipes['previous_url'] + \
                    f"&input={form_data['search_input']}"
            if 'user' in session:
                user_in_db = users_collection.find_one(
                    {"username": session['user']})
                return render_template("recipes.html", recipes=recipes["result"], user_in_db=user_in_db, user_id=user_in_db['_id'], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
            return render_template("recipes.html", recipes=recipes["result"], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
        else:
            flash("Sorry did not find any recipes!")
            return redirect("/")

# Get how many recipes match the input


@app.route('/num_of_input_results', methods=['POST'])
def num_of_input_results():
    if request.method == "POST":
        form_data = request.form.to_dict()
        recipes = SearchForm(
            form_data, no_pagination=True).search_by_input()
        return str(len([x for x in recipes]))

# Search via form tags


@app.route('/tags_form_search', methods=['GET', 'POST'])
def tags_form_search():
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    if request.method == "POST":
        form_data = request.form.to_dict()
        session["search"] = form_data
        recipes = SearchForm(
            form_data, pagination_base="tags_form_search").search_by_tags()
        if recipes == None or recipes["num_of_results"] == 0:
            flash("Sorry did not find any recipes!")
            return_url = request.referrer
            return redirect(return_url)
        else:
            recipes['next_url'] = recipes['next_url'] + \
                f"&input={form_data}"
            recipes['previous_url'] = recipes['previous_url'] + \
                f"&input={form_data}"
        if 'user' in session:
            user_in_db = users_collection.find_one(
                {"username": session['user']})
            return render_template("recipes.html", recipes=recipes["result"], user_in_db=user_in_db, user_id=user_in_db['_id'], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
        return render_template("recipes.html", recipes=recipes["result"], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)
    else:
        if session["search"]:
            form_data = session["search"]
            form_data["limit"] = pagination_limit
            form_data["search_input"] = ""
            recipes = SearchForm(
                form_data, pagination_base="tags_form_search", offset=pagination_offset).search_by_tags()
            if recipes == None or recipes["num_of_results"] == 0:
                flash("Sorry did not find any recipes!")
                return redirect("/")
            else:
                recipes['next_url'] = recipes['next_url'] + \
                    f"&input={form_data}"
                recipes['previous_url'] = recipes['previous_url'] + \
                    f"&input={form_data}"
            if 'user' in session:
                user_in_db = users_collection.find_one(
                    {"username": session['user']})
                return render_template("recipes.html", recipes=recipes["result"], user_in_db=user_in_db, user_id=user_in_db['_id'], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)
            return render_template("recipes.html", recipes=recipes["result"], next_url=recipes["next_url"], previous_url=recipes["previous_url"], num_of_results=recipes["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)
        else:
            flash("Sorry did not find any recipes!")
            return redirect("/")


# Get how many recipes match the tags


@app.route('/num_of_tags_results', methods=['POSt'])
def num_of_tags_results():
    if request.method == "POST":
        form_data = request.form.to_dict()
        recipes = SearchForm(form_data, no_pagination=True).search_by_tags()
        return str(len([x for x in recipes]))


# Search by Dish types
@app.route('/dish_types/<dish_type>')
def search_by_type(dish_type):
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    recipes_in_db = Search(collection=recipes_collection, pagination_base=f"dish_types/{dish_type}", limit=pagination_limit, offset=pagination_offset).all_filters(
        key="dishTypes", value=dish_type)
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title=dish_type.capitalize() + "s", recipes=recipes_in_db["result"], limit=pagination_limit, next_url=recipes_in_db["next_url"], num_of_results=recipes_in_db["num_of_results"],  offset=pagination_offset, user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title=dish_type.capitalize() + "s", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)


# Search by Diets


@app.route('/diet_types/<diet_type>')
def search_by_diet(diet_type):
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    recipes_in_db = Search(collection=recipes_collection, pagination_base=f"diet_types/{diet_type}", limit=pagination_limit, offset=pagination_offset).all_filters(
        key="diets", value=diet_type)
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title=diet_type.capitalize() + "s", recipes=recipes_in_db["result"], limit=pagination_limit, next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"],  offset=pagination_offset, user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title=diet_type.capitalize() + "s", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)

# Search by Time


@app.route('/search_by_time')
def search_by_time():
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    recipes_in_db = Search(collection=recipes_collection, pagination_base=f"search_by_time", limit=pagination_limit, offset=pagination_offset,
                           order=1, sort="readyInMinutes").sort_find_all()
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title="Search by time needed", recipes=recipes_in_db["result"], limit=pagination_limit, next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"],  offset=pagination_offset, user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title="Search by time needed", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"],  limit=pagination_limit, offset=pagination_offset, forms=forms)

# Search by Cuisines


@app.route('/search_by_cuisine/<cuisine>')
def search_by_cuisines(cuisine):
    forms = forms_collection.find()
    pagination_limit = int(request.args["limit"])
    pagination_offset = int(request.args["offset"])
    recipes_in_db = Search(collection=recipes_collection, pagination_base=f"search_by_cuisine/{cuisine}", limit=pagination_limit, offset=pagination_offset).all_filters(
        key="cuisines", value=cuisine)
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title=cuisine.capitalize() + "s", recipes=recipes_in_db["result"], limit=pagination_limit, next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"],  offset=pagination_offset, user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title=cuisine.capitalize() + "s", recipes=recipes_in_db["result"], next_url=recipes_in_db["next_url"], previous_url=recipes_in_db["previous_url"], num_of_results=recipes_in_db["num_of_results"], limit=pagination_limit, offset=pagination_offset, forms=forms)


""" Others """

# Admin Dashboard


@app.route('/admin_dashboard')
def dashboard():
    """ if request.method == "GET":
        hidden_recipes = recipes_collection.delete_many({"visibility": False}) """
    if 'user' in session:
        user_in_db = users_collection.find_one({"username": session['user']})
        users = users_collection.find()
        forms = forms_collection.find()
        all_users_recipes = recipes_collection.find({"user_recipe": True})
        hidden_recipes = recipes_collection.find({"visibility": False})
        return render_template("dashboard.html", page_title="dashboard", users=users, forms=forms, users_recipes=all_users_recipes, hidden_recipes=hidden_recipes, user_id=user_in_db['_id'])
    return redirect(url_for('index'))

@app.route('/graphs')
def graphs():
	forms = forms_collection.find()
	users_vs_db = Charts().users_vs_db()
	if 'user' in session:
		user_in_db = users_collection.find_one(
			{"username": session['user']})
		return render_template("graphs.html", page_title="Graphs", username=session['user'], user_id=user_in_db['_id'], forms=forms, pie_chart=users_vs_db)
	return render_template("graphs.html", page_title="Graphs", forms=forms, pie_chart=users_vs_db)

# Update db

@app.route('/update-db', methods=['POST'])
def update_db():
    if request.method == "POST":
        Database().update_search_form()
        users = Search(users_collection, "users").sort_find_all()
        forms = forms_collection.find()

        return render_template("dashboard.html", page_title="dashboard", users=users, forms=forms)


""" 

Error Pages

"""

# 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# 500


@app.errorhandler(500)
def internal_server_error(e):
    session.clear()
    return render_template('500.html'), 500


if __name__ == '__main__':
    if os.environ.get("DEVELOPMENT"):
        app.run(host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=True)
    else:
        app.run(host=os.environ.get('IP'),
                port=os.environ.get('PORT'),
                debug=False)


""" 

Temporary notes

"""


# fix issue with time of 0 on recipes
# create adding new tags ...
# edit profile
