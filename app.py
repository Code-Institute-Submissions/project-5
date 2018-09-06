import os
from flask import Flask, render_template, redirect, request, url_for, session



from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from key import db_name, uri, log_in_key
from classes import Search, Database

app = Flask(__name__)
# mongoDB config
app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()

mongo = PyMongo(app)
users_colection = mongo.db.users
recipes_colection = mongo.db.recipes
forms_colection = mongo.db.forms


app.config['SECRET_KEY'] = log_in_key()


# Index
@app.route('/')
@app.route('/index')
def index():
    forms = Search(forms_colection, "search_form").optional_filters()
    if session:
        user_in_db = users_colection.find_one({"username": session['user']})
        return render_template("index.html", page_title="Cookbook", username=session['user'], user_id=user_in_db['_id'], forms=forms)
    return render_template("index.html", page_title="Cookbook")


""" Users / Log-in / Register """

# Login


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['user_password']
        try:
            user_in_db = users_colection.find_one({"username": username})
        except:
            return "Sorry there seems to be problem with the data"
        if user_in_db:
            if check_password_hash(user_in_db['password'], password):
                session['user'] = username
                return redirect(url_for('profile', user_id=user_in_db['_id'], username=username))
            else:
                return "Invalid username or password"
        else:
            return f"Sorry no profile {request.form['username']} found"


# Sign up
@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    forms = Search(forms_colection, "search_form").optional_filters()
    if request.method == "POST":
        user_in_db = mongo.db.users.find_one(
            {"username": request.form['username']})
        if user_in_db:
            return f"Sorry profile {request.form['username']} already exist"
        hashed_pass = generate_password_hash(request.form['user_password'])
        users_colection.insert_one(
            {'username': request.form['username'], 'password': hashed_pass})
        user_in_db = users_colection.find_one(
            {"username": request.form['username']})
        session['user'] = request.form['username']
        return redirect(url_for('profile', user_id=user_in_db['_id'], forms=forms))
    if session:
        return render_template("sign-up.html", page_title="Sign up", username=session['user'], forms=forms)

    return render_template("sign-up.html", page_title="Sign up", forms=forms)

# Log out


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

# Profile Page


@app.route('/profile/<user_id>')
def profile(user_id):
    forms = Search(forms_colection, "search_form").optional_filters()
    if session:
        user = Search(users_colection, "users").find_one_by_id(user_id)
        return render_template("profile.html", page_title="profile", user=user, forms=forms)

    return redirect(url_for('index', forms=forms))


""" Recipes """

# Main route for all recipes


@app.route('/recipes')
def recipes():
    recipes_in_db = Search(recipes_colection, "recipes").optional_filters()
    forms = Search(forms_colection, "search_form").optional_filters()
    if session:
        user_in_db = users_colection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db,  user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db, forms=forms)

# Search by Dish types


@app.route('/search/<dish_type>')
def search_by_type(dish_type):
    forms = Search(forms_colection, "search_form").optional_filters()
    recipes_in_db = Search(colection=recipes_colection, dic_name="recipes", v=dish_type).by_all()
    if session:
        user_in_db = users_colection.find_one({"username": session['user']})
        return render_template("recipes.html", page_title=dish_type.capitalize() + "s", recipes=recipes_in_db, user_id=user_in_db['_id'], forms=forms)
    return render_template("recipes.html", page_title=dish_type.capitalize() + "s", recipes=recipes_in_db, forms=forms)

# Main route for single recipe


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = Search(recipes_colection, "recipes").find_one_by_id(recipe_id)
    forms = Search(forms_colection, "search_form").optional_filters()
    return render_template("recipe.html", page_title=recipe['recipes'][0]['title'], recipe_id=recipe_id, recipe=recipe, forms=forms)


""" Others """

# Admin Dashboard


@app.route('/admin_dashboard')
def dashboard():
    users = Search(users_colection, "users").optional_filters()
    forms = forms = forms_colection.find_one(
        {"_id": ObjectId("5b90eaab37265c27d8db87cc")})
    return render_template("dashboard.html", page_title="dashboard", users=users, forms=forms)


# Update db

@app.route('/update-db', methods=['POST'])
def update_db():
    if request.method == "POST":
        Database().update_search_form()
        users = Search(users_colection, "users").optional_filters()
        forms = Search(forms_colection, "search_form").optional_filters()

        return render_template("dashboard.html", page_title="dashboard", users=users, forms=forms)


# Error page


@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
