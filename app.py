import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from key import db_name, uri, log_in_key
from helper import create_user

from collections import OrderedDict

app = Flask(__name__)

# mongoDB config
app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()


mongo = PyMongo(app)

app.config['SECRET_KEY'] = log_in_key()


# Index
@app.route('/')
@app.route('/index')
def index():
    if 'user' in session:
        user_in_db = mongo.db.users.find_one({"username": session['user']})
        return render_template("index.html", page_title="Cookbook", username=session['user'], user_id=user_in_db['_id'])
    return render_template("index.html", page_title="Cookbook")


""" Users / Log-in / Register """

# Login


@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['user_password']
        try:
            user_in_db = mongo.db.users.find_one({"username": username})
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
    if request.method == "POST":
        user_in_db = mongo.db.users.find_one(
            {"username": request.form['username']})
        if user_in_db:
            return f"Sorry profile {request.form['username']} already exist"
        hashed_pass = generate_password_hash(request.form['user_password'])
        return create_user(hashed_pass)

    if 'user' in session:
        return render_template("sign-up.html", page_title="Sign up", username=session['user'])

    return render_template("sign-up.html", page_title="Sign up")

# Log out


@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('index'))

# Profile Page


@app.route('/profile/<user_id>')
def profile(user_id):
    if session:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("profile.html", page_title="profile", user=user)

    return redirect(url_for('index'))


""" Recipes """

# Search class
class Search:
    recipes = mongo.db.recipes

    def __init__(self, k="dishTypes", sort="aggregateLikes", order=-1, limit=21):
        self.k = k
        self.sort = sort
        self.order = order
        self.limit = limit

    def find_one(self, recipe_id):
        return self.recipes.find_one({"_id": ObjectId(recipe_id)})

    def optional_filters(self):
        return self.recipes.find().sort([(f'recipes.{self.sort}', self.order)]).limit(self.limit)

    def by_all(self, v):
        self.v = v
        return self.recipes.find({f"recipes.{self.k}": f"{self.v}"}).sort([(f'recipes.{self.sort}', self.order)]).limit(self.limit)

    def __str__(self):
        return f"Key to serch for: {self.k},\nValue to search for: {self.v},\nSorted by: {self.sort}, \nLimit recipes: {self.limit}"


# Main route for all recipes
@app.route('/recipes')
def recipes(limit=21):
    recipes_in_db = Search().optional_filters()
    if session:
        user_in_db = mongo.db.users.find_one({"username": session['user']})
        return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db,  user_id=user_in_db['_id'])
    return render_template("recipes.html", page_title="Recipes", recipes=recipes_in_db)

# Search by Dish types


@app.route('/search/<dish_type>')
def search_by_type(dish_type, limit=21):
    recipes_in_db = Search().by_all(dish_type)
    if session:
        user_in_db = mongo.db.users.find_one({"username": session['user']})
        return render_template("recipes.html", page_title=dish_type+"s", recipes=recipes_in_db, user_id=user_in_db['_id'])
    return render_template("recipes.html", page_title=dish_type+"s", recipes=recipes_in_db)

# Main route for single recipe


@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    recipe = Search().find_one(recipe_id)
    return render_template("recipe.html", page_title=recipe['recipes'][0]['title'], recipe_id=recipe_id, recipe=recipe)


""" Others """

# Admin Dashboard


@app.route('/admin_dashboard')
def dashboard():
    users = mongo.db.users.find()
    return render_template("dashboard.html", page_title="dashboard", users=users)

# Error page


@app.route('/error')
def error():
    return render_template("error.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
