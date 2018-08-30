from werkzeug.security import generate_password_hash
from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect, request, url_for, session

from bson.objectid import ObjectId


from key import db_name, uri, log_in_key


app = Flask(__name__)

# mongoDB config
app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()

mongo = PyMongo(app)


def create_user(hashed_pass):
    try:
        mongo.db.users.insert_one({
            'username': request.form['username'],
            'email': request.form['email'],
            'password': hashed_pass})

        user_in_db = mongo.db.users.find_one(
            {"username": request.form['username']})
        session['user'] = request.form['username']
        return redirect(url_for('profile', user_id=user_in_db['_id']))
    except:
        return "Sorry there was an error while saving your data"
