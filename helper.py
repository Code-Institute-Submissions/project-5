from werkzeug.security import generate_password_hash
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for
from key import db_name, uri


app = Flask(__name__)


app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()

mongo = PyMongo(app)


class User():
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return f'User name: {self.name}\nEmail: {self.email}\nPassword: {self.password}'


def create_user():
    hashed_pass = generate_password_hash(request.form['user_password'])
    try:
        mongo.db.users.insert_one({
            'username': request.form['username'],
            'email': request.form['email'],
            'password': hashed_pass})
        new_user = User(
            request.form['username'],
            request.form['email'],
            hashed_pass)
        user_in_db = mongo.db.users.find_one(
            {"username": request.form['username']})
        return redirect(url_for('profile', user_id=user_in_db['_id']))
    except:
        return "Sorry there was an error while saving your data"
