

class RecipeSchema():

	# Make it as constractor

    def recipe_schema(self):
        return {
            "recipes": [
                {
                    "aggregateLikes": 0,
                    "extendedIngredients": [
                        {
                            "original": ""
                        }

                    ],
                    "title": "",
                    "readyInMinutes": 0,
                    "image": "https://spoonacular.com/recipeImages/496044-556x370.jpg",
                    "cuisines": [],
                    "dishTypes": [],
                    "diets": [],
                    "winePairing": {
                        "pairingText": ""
					},
                    "instructions": "",
                    "analyzedInstructions": [
                        {
                            "steps": [
                                {
                                    "number": 1,
                                    "step": ""
                                }

                            ]
                        }
                    ],
                    "creditsText": "",
                    "visibility": False
                }
            ]
        }
