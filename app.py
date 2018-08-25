import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from key import db_name, uri


app = Flask(__name__)

app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()

mongo = PyMongo(app)


@app.route('/')
def index():
	return render_template("index.html", page_title="Cookbook")




@app.route('/admin')
def test():
	users = mongo.db.users.find()
	return render_template("test.html", users=users, page_title="admin")











if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=os.environ.get('PORT'),
            debug=True)
