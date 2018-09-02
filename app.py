import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from key import db_name, uri, log_in_key
from helper import create_user


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
    if 'user' in session:
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return render_template("profile.html", page_title="profile", user=user)

    return redirect(url_for('index'))


@app.route('/recipes')
def recipes():
	recipes_id_db = mongo.db.recipes.find()
	if 'user' in session:		
		user_in_db = mongo.db.users.find_one({"username": session['user']})
		return render_template("recipes.html", page_title="Recipes", recipes=recipes_id_db, username=session['user'], user_id=user_in_db['_id'])
	return render_template("recipes.html", page_title="Recipes", recipes=recipes_id_db)

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

