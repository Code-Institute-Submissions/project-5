
import os
from flask import Flask, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# mongoDB config
app.config['MONGO_DBNAME'] = os.environ.get("MONGO_DBNAME")
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)
users_collection = mongo.db.users
recipes_collection = mongo.db.recipes
forms_collection = mongo.db.forms


# Search classes

class Search:
    def __init__(self, collection, sort="aggregateLikes", order=int(-1), no_pagination=False, pagination_base="/", limit=12, offset=0):
        self.collection = collection
        self.sort = sort
        self.order = order
        self.no_pagination = bool(no_pagination)
        self.pagination_base = str(pagination_base)
        self.limit = int(limit)
        self.offset = int(offset)

    def find_one_by_id(self, id):
        return self.collection.find_one({"_id": ObjectId(id)})

    def sort_find_all(self):
        if self.no_pagination:
            return self.collection.find({"visibility": True}).sort(
                [(f'{self.sort}', self.order)]).skip(self.offset)
        else:
            results = self.collection.find({"visibility": True}).sort(
                [(f'{self.sort}', self.order)]).skip(self.offset)
            num_of_results = results.count()
            return self.pagination(results.limit(self.limit), num_of_results)

    def match(self, filters):
        if self.no_pagination:
            return self.collection.aggregate([{'$match': {"$and": filters}}, {"$sort": {self.sort: self.order}}, {"$skip": self.offset}])
        else:
            results = self.collection.aggregate(
                [{'$match': {"$and": filters}}, {"$sort": {self.sort: self.order}}, {"$skip": self.offset}, {"$limit": self.limit}])
            results = list(results)
            num_of_results = len(list(self.collection.aggregate(
                [{'$match': {"$and": filters}}, {"$sort": {self.sort: self.order}}])))
            return self.pagination(results, num_of_results)

    def text(self, value):
        self.collection.create_index([("$**", 'text')])
        if self.no_pagination:
            return self.collection.find({"$and": [{"visibility": True}, {
                "$text": {"$search": str(value)}}]}).skip(self.offset)
        else:
            results = self.collection.find({"$and": [{"visibility": True}, {
                "$text": {"$search": str(value)}}]}).skip(self.offset).limit(self.limit)
            num_of_results = results.count()
            return self.pagination(results.limit(self.limit), num_of_results)

    def all_filters(self, key, value):
        if self.no_pagination:
            return self.collection.find({"$and": [{"visibility": True}, {f"{key}": value}]}).sort(
                [(f'{self.sort}', self.order)]).skip(self.offset)
        else:
            results = self.collection.find({"$and": [{"visibility": True}, {f"{key}": value}]}).sort(
                [(f'{self.sort}', self.order)]).skip(self.offset).limit(self.limit)
            num_of_results = results.count()
            return self.pagination(results.limit(self.limit), num_of_results)

    def random(self, num_of_results):
        return self.collection.aggregate([{"$sample": {"size": num_of_results}}])

    def pagination(self, results, num_of_results):
        return {
            'result': list(results),
            'num_of_results': num_of_results,
            'next_url': f"/{self.pagination_base}?limit={self.limit}&offset={self.offset + self.limit}",
            'previous_url': f"/{self.pagination_base}?limit={self.limit}&offset={self.offset - self.limit}"
        }

    def __str__(self):
        return "Main Search Class"

    def __len__(self):
        return self.collection.find().count()
class SearchForm(Search):
	def __init__(self, form_data, no_pagination=False, offset=int(), pagination_base=""):
		Search.__init__(self, collection=recipes_collection)
		self.form_data = form_data
		self.no_pagination = no_pagination
		self.offset = offset
		self.pagination_base = pagination_base
		self.limit = int(self.get_limit())
		self.order = self.popularity()

	def search_by_tags(self):
		self.filters = [{"visibility": True}]
		del self.form_data["search_input"]
		self.format_tags()
		return self.search_tags()

	def search_by_input(self):
		if self.form_data["search_input"] != "":
			return self.search_input()
		else:
			print("Empty string")

	def get_limit(self):
		# Adjust  limt for results
		if self.form_data.get("limit"):
			self.limit = self.form_data.get("limit")
			del self.form_data["limit"]
			return self.limit
		else:
			del self.form_data["limit"]
		return self.limit

	def popularity(self):
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

	def form_filters(self):
		for key in self.form_data:
			value_key = key
			key = key.split("-")
			key = key[0]
			key = key.strip()
			for value in self.form_data[value_key]:
				search_filter = dict()
				search_filter[key] = value.lower()
				self.filters.append(search_filter)
		return self.filters

	def format_tags(self):
		# Removes indeximg
		# and group inputs together
		formated_inputs = {}

		for key in self.form_data:
			if key == "_id":
				continue
			value_key = key
			key = key.split("-")
			key = key[0]
			if key in formated_inputs:
				formated_inputs[key].append(
					self.form_data[value_key].lower())
			else:
				formated_inputs[f"{key}"] = []
				formated_inputs[key].append(
					self.form_data[value_key].lower())
		self.form_data = formated_inputs

		return self.form_data

	def search_input(self):
		return self.text(str(self.form_data["search_input"].lower()))

	def search_tags(self):
		return self.match(self.form_filters())
		

# DB classes


class Database:

	def users(self):
		return users_collection.find()

	def forms(self, keys):
		pass

	def update(self, key):
		result = set()
		for x in Search(recipes_collection, "recipes").sort_find_all():
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
		forms_collection.insert_one(form)

# Main class for add / edit recipe


class Recipe(dict):

	# Make it as constractor

	def __init__(self, form_data):
		self.recipe = self.recipe_schema(self.formate_data(form_data))

	def formate_data(self, form_data):
		formated_inputs = {}
		for key in form_data:
			if key == "_id":
				continue
			value_key = key
			key = key.split("-")
			key = key[0]
			if key in formated_inputs:
				formated_inputs[key].append(form_data[value_key].lower())
			else:
				formated_inputs[f"{key}"] = []
				formated_inputs[key].append(form_data[value_key].lower())

		return formated_inputs

	def get_ingredients(self, form):
		ingredients = []
		for ingredient in form["ingredient"]:
			ingredients.append({"original": ingredient})
		return ingredients

	def get_steps(self, form):
		steps = [{"steps": []}]
		for step in form["step"]:
			steps[0]["steps"].append(
				{
					"number": len(steps) + 1,
					"step": step
				}
			)
		return steps

	def recipe_schema(self, form):
		return {
			"aggregateLikes": int(form["aggregateLikes"][0]) or 0,
			"extendedIngredients": self.get_ingredients(form),
			"title": form["title"][0],
			"readyInMinutes": int(form["readyInMinutes"][0]) or 0,
			"image": form["new_img"][0] or form["old_img"][0] or "https://spoonacular.com/recipeImages/496044-556x370.jpg",
			"cuisines": form.get("cuisines") or [],
			"dishTypes": form.get("dishTypes") or [],
			"diets": form.get("diets") or [],
			"winePairing": {
				"pairingText": form["winePairing"][0]
			},
			"analyzedInstructions": self.get_steps(form),
			"creditsText": form["creditsText"][0],
			"visibility": False
		}
