from flask import Flask, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

from schema import RecipeSchema

from key import db_name, uri, log_in_key

app = Flask(__name__)

# mongoDB config
app.config['MONGO_DBNAME'] = db_name()
app.config['MONGO_URI'] = uri()


mongo = PyMongo(app)
users_colection = mongo.db.users
recipes_colection = mongo.db.recipes
forms_colection = mongo.db.forms

app.config['SECRET_KEY'] = log_in_key()



# Search classes


class Search:
    def __init__(self, colection, dic_name=str(),  sort="aggregateLikes", order=int(-1), limit=int(21)):
        self.colection = colection
        self.dic_name = dic_name
        self.sort = sort
        self.order = order
        self.limit = limit

    def find_one_by_id(self, id):
        return self.colection.find_one({"_id": ObjectId(id)})

    def sort_find_all(self):
        return self.colection.find({"recipes.visibility": True}).sort([(f'{self.dic_name}.{self.sort}', self.order)]).limit(self.limit)

    def all_filters(self, key, value):
        return self.colection.find({"$and": [{"recipes.visibility": True}, {f"{self.dic_name}.{key}": value}]}).sort([(f'{self.dic_name}.{self.sort}', self.order)]).limit(self.limit)

    def random(self, num_of_results):
        return self.colection.aggregate([{"$sample": {"size": num_of_results}}])

    def __str__(self):
        return "Main Constructor Class"

    def __len__(self):
        return recipes_colection.find().count()

class SearchForm(Search):
	def __init__(self):
		Search.__init__(self, colection=recipes_colection,
						dic_name="recipes")

	def search_reluts(self, form_data):
		self.form_data = form_data
		self.limit = self.get_limit()
		self.order = self.popularity()
		self.format_inputs()
		
		return self.results()

	def get_limit(self):
		# Adjust  limt for results
		if self.form_data.get("limit"):
			self.limit == self.form_data.get("limit")
			del self.form_data["limit"]
		else:
			del self.form_data["limit"]
			self.limit = 5000  # All recipes in db
		return self.limit

	def popularity(self):
		# Adjust  limt for results
		if self.form_data.get("sort"):
			self.order = self.form_data.get("sort").lower()
			if self.order == "ascending":
				del self.form_data["sort"]
				self.order = 1
			else:
				del self.form_data["sort"]
				self.order = -1
		else:
			self.order = -1

		return self.order

	def format_inputs(self):
		# Removes indeximg 
		# and group inputs together
		formated_inputs = {}
		for key in self.form_data:
			if key ==  "_id":
				continue
			value_key = key
			key = key.split("-")
			key = key[0]
			if key in formated_inputs:
				formated_inputs[key].append(self.form_data[value_key].lower())
			else:
				formated_inputs[f"{key}"] = []
				formated_inputs[key].append(self.form_data[value_key].lower())

		self.form_data = formated_inputs

		return self.form_data

	def get_recipes(self):
		# First search if any diets are required
		# as that is the best initial filter
		if "diets" in self.form_data:
			return self.all_filters(key="diets", value=self.form_data["diets"][0])
		if self.form_data["dishTypes"]:
			key = self.form_data.get("search_by")[0]
			value = {"$in": [f"{self.form_data.get('search_input')[0]}"]}
			del self.form_data["search_input"]
			del self.form_data["search_by"]
			return self.all_filters(key=key, value=value)
		else:
			del self.form_data["search_input"]
			del self.form_data["search_by"]
		print(self.form_data)
		return self.form_data

	def results(self):
		recipes = [x for x in recipes_colection.find()]
		inputs = self.form_data
		result = []

		for recipe in recipes:
			for key in inputs:
				if key == "search_input" or key == "search_by":
					continue
				for value in inputs[key]:
					if value in recipe["recipes"][0][key]:
						result.append(recipe)

		return result
	



class Database:

    def users(self):
        return users_colection.find()

    def forms(self, keys):
        pass

    def update(self, key):
        result = set()
        for x in Search(recipes_colection, "recipes").sort_find_all():
            x = x['recipes'][0][f'{key}']
            for y in x:
                result.add(y)
        return result

    def update_db(self, key, form_keys):
        form = {}
        for x in key:
            form[f"{x}"] = []
            for y in self.update(x):
                form[f"{x}"].append(y.capitalize())
        return form

    def update_search_form(self, key=["dishTypes", "cuisines", "diets"]):
        form = self.update_db(key, key)
        form["popularity"] = ["Ascending", "Decreasing"]
        forms_colection.insert_one(form)

	
