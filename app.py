import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash

from key import db_name, uri
from helper import create_user


app = Flask(__name__)

app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html", page_title="Cookbook")

@app.route('/login', methods=['POST'])
def login():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['user_password']
		user_in_db = mongo.db.users.find_one({"username": username})
		if user_in_db:
			if check_password_hash(user_in_db['password'], password):
				return redirect(url_for('profile'))
			else:
				return "Invalid username or password"
		else:
			return f"Sorry no profile {request.form['username']} found"


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
	if request.method == "POST":
		user_in_db = mongo.db.users.find_one({"username": request.form['username']})
		if user_in_db:
			return f"Sorry profile {request.form['username']} already exist"
		else:
			create_user()
			return redirect(url_for('dashboard'))

	return render_template("sign-up.html", page_title="Sign up")


@app.route('/profile')
def profile():
	return render_template("profile.html", page_title="profile")


@app.route('/admin_dashboard')
def dashboard():
	users = mongo.db.users.find()
	return render_template("dashboard.html", page_title="dashboard", users=users)	



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
