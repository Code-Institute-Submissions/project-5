
# **Table of Contents**

- [**Table of Contents**](#table-of-contents)
	- [**The Cookbook**](#the-cookbook)
	- [**CI Brief**](#ci-brief)
	- [**UX**](#ux)
		- [**Requirements**](#requirements)
			- [Database](#database)
			- [Users](#users)
			- [Pages](#pages)
		- [**General Design**](#general-design)
	- [**Features**](#features)
		- [Existing features](#existing-features)
			- [Database existing features](#database-existing-features)
			- [Existing pages](#existing-pages)
			- [Helper](#helper)
		- [Features left to implement](#features-left-to-implement)
	- [**Technologies used**](#technologies-used)
		- [Front End](#front-end)
		- [Back End](#back-end)
	- [**Testing**](#testing)
		- [Tools used for testing](#tools-used-for-testing)
	- [**Changelog and Fixes**](#changelog-and-fixes)
		- [Before 2.2](#before-22)
			- [**Testing and improvements before 2.2**](#testing-and-improvements-before-22)
			- [**Some user feedbacks before 2.2**](#some-user-feedbacks-before-22)
		- [2.2 and later](#22-and-later)
			- [2.2](#22)
			- [2.3](#23)
			- [2.4](#24)
			- [2.5](#25)
			- [Bootstrap 4 Flex-box on iOS](#bootstrap-4-flex-box-on-ios)
	- [**Deployment**](#deployment)
	- [**How to run the project locally?**](#how-to-run-the-project-locally)
	- [**What could be done better?**](#what-could-be-done-better)
	- [**Credits**](#credits)
		- [Special thanks to](#special-thanks-to)
		- [Recipes](#recipes)
		- [Media](#media)

<hr />

## **The Cookbook**

Hello there,  
and welcome to my fourth [Code Institute (CI)](https://courses.codeinstitute.net/) school project.

In this project I should be able to show that I can create a web application using [Python 3](https://www.python.org/downloads/) and [Flask]( http://flask.pocoo.org/) which works with cloud **SQL** / **NoSQL** database.

I decided to follow the given example from CI for this project.

<hr />

## **CI Brief**

- **CREATE AN ONLINE COOKBOOK**
  - **Create a web application that allows users to store and easily access cooking recipes**
  - Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). 
    - Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
  Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
  - Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
  - Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
  - Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
  - Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
  - Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

- **CREATE YOUR OWN PROJECT**
  - If you choose to create your project outside the brief, the scope should be similar to that of the example brief above.

<hr />

## **UX**

*I personally do not like to cook and as I almost never visit those kind of websites, I search around the web first to get a general idea of the design and data required for this project.*

*I visited many websites and the only thing I didn’t like was that they all looks a bit "outdated" in design and sometimes "too busy".*

*Therefore, I decided to create a cooking website which will have a "modern" look while keeping clean design.*

### **Requirements**

*Based on my research and brief given by CI, I created the below requirements for this project.*

#### Database

- Create schema based on structure of the recipe/s found
- Create schema for user
- Create different collections for all above

#### Users

Use [Flask Sessions](http://flask.pocoo.org/docs/1.0/quickstart/) for easier account management.

Role | View Recipe/s | Add / Edit / Delete Recipe | Access admin area
--- | --- | --- | ---
Anonymous | Yes | No | No |
Logged in | Yes | Yes* | No |
Logged in as Admin | Yes | Yes** | Yes |
Logged in as CI | Yes | Yes** | Yes |

**User should be able to edit / delete only his own recipe/s.*

***Admin and CI should be able to delete any (user recipes).*

#### Pages

Create 6 - 7 pages for the project.

- **Any page**
  - **Navigation**
    - Logo should lead the user to "home" page
    - Create functionality for user to access **All recipes**
    - Create functionality for user to search for existing recipes
    - **Anonymous**
      - Create functionality for user to be able to create new account.  
        ***(The general idea is that only registered users can add / edit / delete recipe in the database.)***  
      - Create functionality for user to be able to log-in to existing account.
    - **Logged in**
      - Create functionality for user to be able log out from current session
      - Create functionality for user to access **Add new recipe**
      - Create functionality for user to access **Profile page**
  - **Footer**
    - **Logged in as Admin / CI**
      - Create functionality for user to access **Admin page**
- **Landing page (index.html)**
  - Welcome new or existing user  
- **All recipes**
  - Show user available recipes (if any)
    - Show base information about each of them
  - Sort the recipes based on popularity by default
  - Add pagination (if too many recipes to display)
- **Single recipe**
  - Show user detail information’s about targeted recipe
    - Title
    - Author
    - Picture (if any)
    - Indegrees
    - Step by step instructions
    - Dish type (if any)
    - Allergies (if any)
    - Time required for preparation
- **Add recipe**
  - Allow logged in user to add new recipe to database
- **Edit recipe**
  - Allow logged in user to edit his own recipe
- **Profile page**
  - Show user avatar (if any)
  - Show recipes added by user
  - Show overall popularity of the user recipes
  - Let user to edit his profile
- **Admin area**
  - Show registered users and they information
  - Show recipes by users
    - Create functionality for the user to delete recipe from database on this page
  
### **General Design**

Design | Importance
--- | ---
Functionality | 7 |
User experiences | 6 |
HTML / CSS | 5 |

[**To top**](#Table-of-Contents)

<hr />

## **Features**

### Existing features

*For more detail information please visit [**Changelog and Fixes**](#changelog-and-fixes)*

#### Database existing features

*I decided to use NoSQL database as the recipes form **API** are in this format. Also the main idea was not to overwhelm a user with too many drop-downs such as "Is the ingredient in kg, pounds, tons or spoons?".*

*[mLab](https://mlab.com/welcome/) was used to store the recipes.*

- **Schemas**
  - created [recipe schema](/assets/db/recipe_schema.json) based on the recipes recieved from **API**  
  *Example of [recipe](/assets/db/api_recipe_example.json) recieved from **API***
  - [user schema](/assets/db/user-schema.json)
  
- **Collections**
  - **recipes**
    - used to store all recipes
  - **trivia**
    - used to store trivia for [index.html](/templates/index.html)
  - **forms**
    - used to store form tags for [search-form.html](/templates/search-form.html) and [search-form-sm.html](/templates/search-form-sm.html)
  - **schemas**
    - used to store schemas such as [recipe schema](/assets/db/recipe_schema.json)
  - **testing**
    - used for development process only to avoid damage to the main **recipe** collection
  - **back_up**
    - used to store all recipes as back up if something goes wrong with the **recipe** collection

#### Existing pages

- **Any page**
  - **Navigation**
    - logo always leads user to [index.html](/templates/index.html)
    - **All Users**
      - user is now able to access [recipes.html](/templates/recipes.html) from any page
      - user is now able to access [search-form-sm.html](/templates/search-form-sm.html) on portable devices or access `search_form_modal` on extra large screens
      - user is now able to access [graphs.html](/templates/graphs.html) from any page
    - **Anonymous**
      - user is now able to access `log_in_modal` to log-in to **Flask** session or access [sign-up.html](/templates/sign-up.html) to create an account
    - **Logged in**
      - user is now able to access `log_out_modal` to log out from current **Flask** session
      - user is now able to access [add-recipe.html](/templates/add-recipe.html) from any page
      - user is now able to access [profile.html](/templates/profile.html) from any page
    - **Logged in as Admin / CI**
      - **CI** and **admin** user's are able to access [admin.html](/templates/admin.html) from any page
- **[index.html](/templates/index.html)**
  - added functionality for `trivia` section. Randomly select document from `trivia` collection (40 in total)
  - added functionality for `index-recipes` section. Randomly select 5 documents from `recipes` collection
- **[recipes.html](/templates/recipes.html)** *By default user is able to view all `visible` recipes (- pagination) sorted by `aggregateLikes` in form of cards.*
  - picture will take the user to detail view of the clicked recipe ([recipe.html](/templates/recipe.html))
  - user is now able to click on any of the tags **"dishTypes", "cuisines", "diets" and "readyInMinutes"** to instantly search for recipes of clicked tag
  - add pagination on bottom of the page. By default **6** with offset **0 / 12**
- **[recipe.html](/templates/recipe.html)**  *Show user detail information about a recipe.*
  - **All Users**
    - allow user to view detail information including
      - **title, picture, time needed, ingredients, aggregate likes, steps, wine pairing(if any), author, dish types(if any), cuisines(if any), diets(if any)**  
      *All tags are clickable and allow user to instantly search for recipes of the clicked tag.*
    - allow user to print the recipe
  - **Anonymous**
    - user is now able to access `log_in_modal` by clicking on **"You must be logged in to vote / edit recipe"**
  - **Logged in**
    - user is now able to vote up or down for the viewed recipe. All votes are recorded to prevent user to vote multiple times for the same recipe
    - **If owner**
      - user is now able to access `delete-recipe` modal to delete the viewed recipe
      - user is now able to access [add-edit-template.html](/templates/add-edit-template.html) to edit the viewed recipe
  - **Logged in as Admin / CI**
    - **If user recipe**
      - able to access `delete-recipe` modal to delete the viewed recipe
      - access [add-edit-template.html](/templates/add-edit-template.html) to edit the viewed recipe
      - approve hidden recipes  
      *All users recipes are hidden by default.*
      - hide visible recipes
- **[profile.html](/templates/profile.html)**
  - allow logged in user to see detail information about his profile including
    - **Picture** *Randomly selected while creating profile (from 4).*
    - **Profile name**
    - **Profile email** *If provided.*
    - **Recipe section**
      - If there are no recipes the user can access [add-recipe.html](/templates/add-recipe.html) instead.
      - **If any**
        - allow user to see basic information about his own recipes including **title** and **aggregate likes**
        - allow user to access [edit-recipe.html](/templates/edit-recipe.html) to edit each recipe
        - allow user to access [recipe.html](/templates/recipe.html) to view each recipe
- **[admin.html](/templates/admin.html)**
  - **CI or admin users only** *username: **CI** or **ci** password **codeinstitute***
    - **Recipes**
      - Show all user recipes `_id`
      - Show all hidden (user) recipes `_id`
    - **Users**
      - Show basic information about each user in `users` collection. Including `username`, `_id`, `email`(if any), `recipes` and `votes`.
    - **Database**
      - Show current [search form schema](/assets/db/search-form-schema.json) in use including `_id` and all tags
      - Update the current [search form schema](/assets/db/search-form-schema.json) manually
- **[add-recipe.html](/templates/add-recipe.html)**
  - allow logged in user to add new recipe to database base on [recipe schema](/assets/db/recipe_schema.json)
    - **Title for the recipe**
    - **Picture for the recipe (optional)** *Default picture always selected if no url is provided.*
    - **Time needed**
    - **Ingredients**
      - allow user to add or delete a ingredient to minimum of 1.
    - **Steps** 
      - allow user to add or delete a steps to minimum of 1.
    - **Wine pairing (optional)**
      - allow user to add wine pairing to the recipe.
    - **Tags (optional)**
      - allow user to add new tag
      - if tag already exists it will be automatically checked for user
      - select any of the tags already exists in database
- **[edit-recipe.html](/templates/edit-recipe.html)**
  - allow logged in user to edit his own recipe  
  *Same rules apply as in [add-recipe.html](/templates/add-recipe.html)*
- **[graphs.html](/templates/graphs.html)**  
*All graphs shows recipes including the ones which are hidden.*  
*I did not want to have testing recipes visible on the website.*

  - **User's recipes vs Database recipes**
  - **User's recipes vs Database recipes (Dish Types)**
  - **User's recipes vs Database recipes (Cuisines)**
  - **User's recipes vs Database recipes (Diets)**

- **[search-form.html](/templates/search-form.html)**
  - **Input search**
    - on input change user now see the number of results before searching
    - if no recipes found the search button is disabled
  - **Tags search**
    - while changing the tags user now see the number of results before searching
    - if no recipes found the search button is disabled and user is asked to remove some of the filters
  - **Limit results**
    - working for both **Input search** and **Tags search**
  - **Popularity**
    - working for both **Input search** and **Tags search** 
  - create separate view for mobile devices search **[search-form-sm.html](/templates/search-form-sm.html)** which inherit from this template
- **[404.html](/templates/404.html)**
  - allow user to get back to [index.html](/templates/index.html) after **404** error
- **[500.html](/templates/500.html)**
  - allow user to get back to [index.html](/templates/index.html) after **500** error  
  *500 error will also automatically log out user from **Flask** session to prevent additional errors.*

#### [Helper](/helper/classes.py)

**`Search`**

**Main class for sending queries to mLab**

- **`Search`**  
*Construct a query based on user input/s and return it's results.*  
*All methods which sending quires to **mLab** can return `None` if no documents are found.* 
  - `find_one_by_id()`
    - return single document for given `_id`
  - `sort_find_all()`
    - return collection of documents with only one filter (`{"visibility": True}`)
  - `match()`
    - return collection of documents for given **array of filters**  
    *Mainly used for searching by tags. The result will match any documents which match all of the filters given*
  - `text()`
    - create an "wild card" `text` index
    - return collection of documents for given **string**  
    *Mostly used for search via `input`.*
  - `all_filters()`
    - return collection of documents for given **key** and **value**  
    *However, all other filters can be passed to `__init__()`.*  
    *Mainly used while searching by individual tags group.*  
  - `random()`
    - return collection of documents based on **collection** and **number of results** given  
    *Used to get random documents for `trivia` and `index-recipes` sections in [index.html](/templates/index.html)*
  - `pagination()`
    - return dictionary containing data for pagination including **results, num_of_results, next_url** and **previous_url**
  - `__len__()`
    - return number of documents in given **collection**

**`SearchForm(Search)`**

**Main Class for working with [search-form.html](/templates/search-form.html) and [search-form-sm.html](/templates/search-form-sm.html).**  

*This Class is mainly used to format the inputs and construct filters which are passed to `Search()` to get results.*  
*This is also why the `SearchForm` class inherit from `Search()`.*

*Example of data which needs to be cleared can be viewed [here](/assets/db/form-search-data-examp.json).*

- **`SearchForm(Search)`**
  - `search_by_tags()`
    - main method which return the final result if user search by tags
  - `search_by_input()`
    - main method which return the final result if user search by input
  - `get_limit()`
    - return `limit` (if selected by user) or delete this key and return **12** (default value for pagination) if not
  - `popularity()`
    - return the `order` of recipes (**Ascending** or **Decreasing**) depends on user selection  
    *By default the `order` is set to **Decreasing**.*
  - `form_filters()`
    - return filters which are passed to query in form **list** of **dictionaries**  
    *This method format the data passed.*  
    *Example: `[{'visibility': True}, {'cuisines': 'nordic'}]`*
  - `format_tags()`
    - return dictionary of filters in form of **key** and **list** of **values**  
    *Example: `{'diets': ['vegan', 'fodmap friendly'], 'dishTypes': ['dessert']}`* 
  - `search_input()`
    - format the **string** and create the query with `Search().text()`
  - `search_tags()`
    - final stage which add the formatted filters selected by user to `Search().match()`

**`Database`**

**Used to update tags for [search-form.html](/templates/search-form.html) and [search-form-sm.html](/templates/search-form-sm.html)**

*The initial idea was much bigger for this class. However, as I updated the `Search` class later on to work with any collection this class only update the tags now.*

- **`Database`**
  - `update()`
    - search for existing tags and return them in form of in form of **key** and **list** of **values**
  - `update_db()`
    - if new tags found `append` them **list** associate with **key**
  - `update_search_form()`
    - main method which update the document in **form** collection at the end

**`Recipe(dict)`**

**Create recipe based on [recipe schema](/assets/db/recipe_schema.json)**

*Both `add_recipe()` and `edit_recipe()` use this class.*

- **`Recipe(dict)`**
  - `formate_data()`
    - format the data from request and return them in form of dictionary
  - `get_ingredients()`
    - format data from `form["ingredient"]` and return them in form of **list** of **dictionaries**
  - `get_steps()`
    - format data from `form["steps"]` and return them in form of **list** of **dictionaries**
  - `recipe_schema()`
    - final stage wich return the recipe in form of **dictionary** based on the [recipe schema](/assets/db/recipe_schema.json)

**`Charts`**

**Construct data for [graphs.html](/templates/graphs.html) and return them**

- **`Charts`**
  - `users_vs_db()`
    - construct graph data which shows **User's** vs. **Database** recipes in total in form of **pie chart**
  - `line_graph()`
    - construct graph data which shows **User's** vs. **Database** recipes in total for selected tag in form of **line chart**
  - `users_vs_db()`
    - return separate data for **User's** and **Database** in form of **dictionary**  
    *This method is used to separate data and pass them to `line_graph()`*

[**To top**](#Table-of-Contents)

### Features left to implement

- **[search-form.html](/templates/search-form.html) as `search_form_modal`**
  - **Tags search**
    - with adding more and more tags the modal eventually can not hold the numbers  
    *Easiest solution is just to use [search-form-sm.html](/templates/search-form-sm.html) for all screens and discard the modal view. Other option is to let **Jinja** to get the total number of elements (tags) and inject the columns as required. Similar approach as I done with user recipes in [profile.html](/templates/profile.html).*
- [sign-up.html](/templates/sign-up.html)
  - add second field for password to cross check it
  - add email as required field and / or allow users to login via email

[**To top**](#Table-of-Contents)

<hr />

## **Technologies used**

### Front End

- [Bootstrap 4.0.0](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
  - The project uses **Bootstrap** to speed up the development.
- [Font Awesome 5.3.1](https://fontawesome.com/)
  - The project uses **Font Awesome** for icons.
- [jQuery 3.2.1](https://blog.jquery.com/2017/03/20/jquery-3-2-1-now-available/)
  - The project uses **jQuery** for better user experiences as well as sending requests to server.

### Back End

- [Flask 1.0.2](http://flask.pocoo.org/docs/1.0/) a micro web Python framework
  - **Flask** was used to build the application as well as to speed up the development process.
- [PyMongo 3.7.2](https://api.mongodb.com/python/current/)
  - **PyMongo** was used to send quires to **mLab**
- [Pygal 2.4.0](http://pygal.org/en/stable/)
  - **Pygal** was used to generate and render the graphs data for [graphs.html](/templates/graphs.html)

[**To top**](#Table-of-Contents)

<hr />

## **Testing**

### Tools used for testing

- **Front End**
  - [W3C Markup Validation Service](https://validator.w3.org/)
    - [graphs.html](/templates/graphs.html)
      - 10 errors due to the graphs injecting with **pygal**
    - All other pages 
      - **Document checking completed. No errors or warnings to show.**

  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) (All pages)
    - Shows 29 errors and 975 warnings due to the **Bootstrap 4** clasees and rules.  
    *There are no errors showing in custom CSS's*

  - [JSHint](https://jshint.com/) (Report of all custom JS functions)
    - **Metrics**
      - There are 32 functions in this file.
      - Function with the largest signature take 3 arguments, while the median is 0.5.
      - Largest function has 18 statements in it, while the median is 3.5.
      - The most complex function has a cyclomatic complexity value of 6 while the median is 1.
    - **11 unused variables**
      - This is because the functions are called from templates
- **Back End**
  - [Jupyter Notebook](https://jupyter.org/index.html)
    - *Most of the functions has been pre-written and tested in **Jupyter Notebook**.*

  - [Visual Studio Python debugger](https://code.visualstudio.com/docs/python/debugging)
    - *Mostly used after **Jupyter Notebook** testing.*

  - [Postman](https://www.getpostman.com/)
    - To send fake requests to server  

[**To top**](#Table-of-Contents)

<hr />

## **Changelog and Fixes**

*[Git](https://git-scm.com/) has been used for version control.*

- There are 5 different branches:

  - [master branch](https://github.com/MiroslavSvec/project-4/tree/master) used in production.  
    - *The application is built from this branch on **Heroku***

  - *4 other branches has been created for development purpose only. Where each branch represent different version of the application.*

### Before 2.2

*Before version 2.2 I did not use separated branches.*

- **1.0**
  - Added User registration and Login  
  - Added Admin dashboard for testing
  - Added @routes for all above
  - Added security via hashed password
  - Users are now stored in mongoDB database
  - Added unique link for every user
  - Added sessions for users

- **1.1**
  - Connected to API

- **1.2**
  - Added fundamentals for recipes page
  - Added fundamentals for single recipe page
  - Added Search class for searching the database for recipes
  - Added functionality to search by dish types, cuisines, time needed and diets
  - Redesign  Search class to work for any collection
  - helper.py no longer used
  - Updating db now via JS for better user experiences
  - Added SearchForm class for main search
  - Also connected the form to back-end

- **1.3**
  - Finished index recipes section
  - Added random recipes and trivia to this section
  - Finished recipe.html

- **1.4**
  - Added schema for recipe based on the API
  - Added constructor class base on the schema for updating a recipe
  - Finished edit recipe
  - Added more JS for user experiences
  - Fixed many errors along the way
  - Added filters and errors handling in add / edit form
  - Users are now able to print the recipes

- **1.5**
  - schema.py no longer in use
  - Moved Recipe class to classes.py
  - Slightly improved database structure for better readability and manipulation with data
  - Extended the Search class to be able to search by `$match`, `$text`
  - Search class now dynamically set the default limit based on documents count
  - User is now redirected to the last page viewed when log-in/out
  - Add flashed messages for user when login-in / out and search recipes errors
  - Moved "Trivia" section to top for better visibility
  - **Search form**
    - Added second button to search form for user to clearly see what he is searching for
    - While changing the tags user now see the number of results before searching
    - If no recipes found the search button is disabled and user is asked to remove some of the filters
    - Removed "Search by" as this was getting too confusing for user. Instead the search input searches for any matching results
    - Added min and max length to input search. JS also checking for input length and enabling / disabling search input btn
    - JS now also checking how many recipes are found on input change
    - Create separate view for mobile devices search

- **1.6**
  - Deployed to Heroku for testing the app on mobile devices
  - Added env variables and removed key.py as no longer in use

- **1.7**
  - Send out the app to users for testing
  - Added links to Footer

- **1.8**
  - Added Pagination to recipes and search
  - Search class has now option to search without limiting the results

- **1.9**
  - Added Voting system for recipes
  - Changed the styles of sign-up.html
  - Added option to delete recipe

- **2.0**
  - Finished Profile page

- **2.1**
  - Fixed voting system
  - Added few improvements from users stories
  - Fixed issue where email address was not storing in database

#### **Testing and improvements before 2.2**

- Fixed bug in add/edit recipe where JS was incorrectly injecting `maxlength` of 60 instead of 150 in "Steps" section
- Reduced limit on "Ingredients" input `minlength` from 5 to 3
- Moved Alerts to top for better visibility
- Decided to use the mobile search for tablets as well
- At least one tag must be selected to use the for searching recipes
- Fixed bug where user will not be redirected to mobile search on tablets like screens (medium size resolutions)
- Fixed 500 error when trying to print recipe while logged out
- Fixed bug where user could vote for his own recipe.
- Added statement to check if cursor is `None` which occurs when empty form is submitted for example.
- Fixed major glitch. As soon as user voted for one recipe he could not vote for any other recipes as the app said "You already voted for this recipe"

#### **Some user feedbacks before 2.2**

- Fixed many typos
- Changed the "Welcome" message in profile page
- Increased `setTimeout()` from 5s to 7s in `flashed_messages()` as some of the messages was hard to read all before disappearing
- If not logged in user can now click on "You must be logged in to vote / edit recipe" to bring the log in modal
- Made "Register an Account" to looks like a btn for better visibility
- Reduced input search `minlength` from 5 to 4 for words like a "Fish" for example

### 2.2 and later

#### 2.2

- **Changelog**
  - Added README template and changed it to suits the project
    - Added [**Requirements**](#requirements) section to README
  - Added [404.html](/templates/404.html) template and errorhandler
  - Added [500.html](/templates/500.html) template and errorhandler
  - Added access to [Admin area](/templates/dashboard.html) for **admin** and **CI** user
- **Fixes**  
  - [add-edit-template.html](/templates/add-edit-template.html)
    - Added `autocomplete="off"` to inputs to hide the user stories
  - Reduced input search `minlength` from 4 to 3 for words like a "Egg" for example

#### 2.3

- **Changelog**
  - [classes.py](/classes.py)
    - Added **Charts** class to keep the code clean.
      - `users_vs_db()` get figure of total user recipes vs database recipes
      - `line_graph()` `return` graph for `dishTypes`, `cuisines` and `diets`
  - Added [graphs.html](/templates/graphs.html) as I decided to render the graphs on a separate page
- **Fixes**
  - [classes.py](classes.py)
    - Added `sort()` to **Search** class `text()` method as it was missing and therefore, this search did not sort the results by `aggregateLikes`.
    - [app.py](app.py)
      - Added `lower()` to `profile()` recipe search as no recipes where find if user use capital letters in his user name.

#### 2.4

- **Changelog**
  - Added functionality to delete any user recipe for **CI** and **admin**users.
  - Added functionality to hide / show any user recipe for **CI** and **admin** users.
  - Added functionality to edit any user recipe for **CI** and **admin**users.
  - [app.py](app.py)
    - Added functionality to automatically add new tags to search form schema in `approve_recipe()`
    - Added functionality for user to have random (from 4) profile picture while creating account in `sign_up()`
    - Cleaned up the code and added external files for **CSS** and **JS**
- **Fixes**
  - Recipe `visibility` is now always set to `False` every time the user edit the recipe for security reasons
  - Changed form search schema to lower cases to prevent duplications and errors in future.
  - [app.py](app.py)
    - `login()` both **ci** and **CI** share the same account
    - `delete_recipe()` 
      - will now always check the database for empty tags
      - **CI** and **admin** now able to delete other user recipes without errors when owner of the recipe no longer exists
  - [classes.py](classes.py)
    - Updated `Database()` methods to match the recipe schema

#### 2.5

- **Changelog**
  - Validate **HTML**, **CSS** and **JS**
  - Added [favicon.ico](/static/img/favicon.ico)
- **Fixes**  
  - Fixed minor layout issues as accidentally used `col-xs-12` instead of `col-12`
  - [sign-up.html](/templates/sign-up.html)
    - Fixed broken link to add recipe after user log in
  - [profile.css](/static/custom/css/profile.css)
    - made the `nav` darker for netter visibility for smaller screens
  - [recipe.html](/templates/recipe.html), [recipes.html](/templates/recipes.html) and [search-form-small.html](/templates/search-form-small.html)
    - Added more padding to top header as when logged in as **CI** or **admin** the second `nav` was covering to title
  - [search-form.html](/templates/search-form.html)
    - changed `container` to `container-fluid` as this gives more space to long tags such as **Eastern European**
  - [app.py](/app.py)
    - `hide_recipe()` database is now updated every time a recipe is hidden to prevent empty tags
  - [helper](/helper/classes.py)
    - fixed major bug when `Recipe` class lower cased image url's


#### Bootstrap 4 Flex-box on iOS

*Encountered many glitches with **Flexbox** and **iOS** (especially tablets).  
Where some of them are still present and therefore the application is not fully compatible with older versions of **Safari**.*

- Fixed issue where user was unable to access the search on iOS tablets. Was forced to use JS at the end to change the `a` to `button` on lg and xl screens.
- Found workaround with search form will not trigger event on checkbox change and / or input change. Using JS to check if user using Safari on tablet / mobile view and if so the attr `disabled` is removed so user can use the form.

[**To top**](#Table-of-Contents)

<hr />

## **Deployment**

- [Python 3.6.3](https://www.python.org/downloads/release/python-363/) and [Flask 1.0.2](http://flask.pocoo.org/docs/1.0/) was used to build the application.
  - created [requirements.txt](https://github.com/MiroslavSvec/project-4/blob/master/requirements.txt) that **Heroku** knows which packages are required for the application to run and install them.
  - created [Procfile](https://github.com/MiroslavSvec/project-4/blob/master/Procfile) that **Heroku**  knows what kind of application is this.

- [Heroku](https://www.heroku.com/home)  
*Free cloud hosting platform which simplify the deployment process.*

  - **Settings**
    - Added **Config Vars**
      - IP `0.0.0.0`
      - PORT `5000`
      - MONGO_URI
      - SECRET_KEY
    - **Deploy**
      - Connected the app to **GitHub** project
      - Enabled automatic deploys from  master branch
      - Deployed the branch manually
        - **Last Build log**
          - Python app detected
          - Installing requirements with pip
          - Discovering process types
            - Procfile declares types -> web
          - Compressing...
            - Done: 48.8M
          - Launching...
            - Released v57 https://p4-cookbook.herokuapp.com/ deployed to Heroku

[**To top**](#Table-of-Contents)

<hr />

## **How to run the project locally?**

*Please note that the project can not be run locally without database user name and password.*

*Due to the security reasons I do not publish any of those and therefore the project can not be really run locally.*

1. Download and install [Python 3](https://www.python.org/downloads/)
2. Clone or download the project  
*Please note that if you downloaded the project manually you must unpack it after*
3. Open your **Command line (CLI)** inside the project root or navigate to it
4. [Create virtual environment (venv)](https://docs.python.org/3/tutorial/venv.html) (optional)
   - Activate venv `source venv/bin/activate` where "venv" is the name of your virtual environment
5. Install required packages via **CLI**
   - `pip install -r requirements.txt`
6. Set **venv** variables
   - IP `0.0.0.0`
   - PORT `5000`
   - MONGO_URI such as `mongodb://<dbuser>:<dbpassword>@ds225442.mlab.com:25442/<dbname>`
   - SECRET_KEY `my_secret_key`
   - DEVELOPMENT (optional)
7. Run the application
   - `python app.py`
8. The application should now run on your `localhost:5000`

[**To top**](#Table-of-Contents)

<hr />

## **What could be done better?**

- MUCH better error handling. Right now, minimum to none
- Again, tests has been done manually or with little use of automated tests

[**To top**](#Table-of-Contents)

<hr />

## **Credits**

### Special thanks to

- **everyone for finding few minutes to test the project!**

  *All of you gave me constructive feedback which made the project better* 😊

### Recipes

- all non user recipes data and pictures are taken from [spoonacular.com](https://spoonacular.com/) using [Rapid API](https://rapidapi.com/)

### Media

- [favicon](/static/img/favicon.ico)
  - generated from [favicon-generator.org](https://www.favicon-generator.org/)
- all other images
  - was borrowed from multiple websites and cannot take any credit for them

[**To top**](#Table-of-Contents)

