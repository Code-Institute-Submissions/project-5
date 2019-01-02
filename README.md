
## **Table of Contents**

- [**The Cookbook**](#the-cookbook)
	- [**CI Brief**](#ci-brief)
	- [**UX**](#ux)
		- [General Design](#general-design)
		- [Requirements](#requirements)
		- [Wireframes](#wireframes)
		- [Template](#template)
	- [**Features**](#features)
		- [Existing features](#existing-features)
		- [Features left to implement](#features-left-to-implement)
	- [**Technologies used**](#technologies-used)
		- [Front End](#front-end)
		- [Back End](#back-end)
	- [**Testing**](#testing)
		- [Tools used for testing](#tools-used-for-testing)
	- [**Changelog and Fixes**](#changelog-and-fixes)
		- [**Changelog**](#changelog)
			- [1.0](#10)
			- [1.1](#11)
			- [1.2](#12)
			- [1.3](#13)
			- [1.4](#14)
			- [1.5](#15)
				- [Search form](#search-form)
			- [1.6](#16)
			- [1.7](#17)
			- [1.8](#18)
			- [1.9](#19)
			- [2.0](#20)
			- [2.1](#21)
			- [2.2](#22)
		- [**Testing and improvements**](#testing-and-improvements)
		- [**Some user feedbacks**](#some-user-feedbacks)
		- [**Need to fix**](#need-to-fix)
			- [BS4 Flex-box iOS](#bs4-flex-box-ios)
	- [**Deployment**](#deployment)
	- [**How to run the project locally?**](#how-to-run-the-project-locally)
	- [**What could be done better?**](#what-could-be-done-better)
	- [**Credits**](#credits)
		- [Special thanks to](#special-thanks-to)

<hr />

# **The Cookbook**

Hello there,  
and welcome to my fourth [Code Institute (CI)](https://courses.codeinstitute.net/) school project.  

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

### General Design


**The project general idea is for entertainment purpose only.**


### Requirements

- **Welcome page**

### Wireframes

### Template


[**To top**](#Table-of-Contents)

<hr />

## **Features**

### Existing features

- [**index.html**](https://github.com/MiroslavSvec/project-4/blob/master/templates/index.html)
  - **Create Account / Login form**
    - allow user to create an account
    - allow user to log-in to existing account
- **Any other page**
  - **Navigation**

### Features left to implement

- [**index.html**](https://github.com/MiroslavSvec/project-4/blob/master/templates/index.html)
  - Create Account / Login form
    - check user password (not required for this project)
- **Any other page**
  - **Navigation**
    - **Top Navbar**

[**To top**](#Table-of-Contents)

<hr />

## **Technologies used**

### Front End

<!-- Change links -->
- [Bootstrap 4.0.0](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
  - The project uses **Bootstrap** to speed up the development.
- [Font Awesome 4.7.0](https://fontawesome.com/)
  - The project uses **Font Awesome** for icons.
- [jQuery v3.3.1](https://blog.jquery.com/2018/01/20/jquery-3-3-1-fixed-dependencies-in-release-tag/)
  - The project uses **jQuery** for better user experiences as well as sending requests to server.
    - [jQuery Easing](https://cdnjs.com/libraries/jquery-easing) - used for "back to top button"

### Back End

- [Flask 1.0.2](http://flask.pocoo.org/docs/1.0/) a micro web Python framework
  - **Flask** was used to build the application as well as to speed up the development process.

[**To top**](#Table-of-Contents)

<hr />

## **Testing**

### Tools used for testing

- **Front End**
  - [W3C Markup Validation Service](https://validator.w3.org/) (All pages)

  - [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) (All pages)

  - [JSHint](https://jshint.com/) (Report of all custom JS functions)
    - **Metrics**
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

- There are 7 different branches:

  - [master branch](https://github.com/MiroslavSvec/project-4/tree/master) Used in production.  
    - *The application is built from this branch on **Heroku***

  - *6 other branches has been created for development purpose only. Where each branch represent different version of the application.*

### **Changelog**

#### 1.0

- Added User registration and Login  
- Added Admin dashboard for testing
- Added @routes for all above
- Added security via hashed password
- Users are now stored in mongoDB database
- Added unique link for every user
- Added sessions for users

#### 1.1

- Connected to API

#### 1.2

- Added fundamentals for recipes page
- Added fundamentals for single recipe page
- Added Search class for searching the database for recipes
- Added functionality to search by dish types, cuisines, time needed and diets
- Redesign  Search class to work for any collection
- helper.py no longer used
- Updating db now via JS for better user experiences
- Added SearchForm class for main search
- Also connected the form to back-end

#### 1.3

- Finished index recipes section
- Added random recipes and trivia to this section
- Finished recipe.html

#### 1.4

- Added schema for recipe based on the API
- Added constructor class base on the schema for updating a recipe
- Finished edit recipe
- Added more JS for user experiences
- Fixed many errors along the way
- Added filters and errors handling in add / edit form
- Users are now able to print the recipes

#### 1.5

- schema.py no longer in use
- Moved Recipe class to classes.py
- Slightly improved database structure for better readability and manipulation with data
- Extended the Search class to be able to search by `$match`, `$text`
- Search class now dynamically set the default limit based on documents count
- User is now redirected to the last page viewed when log-in/out
- Add flashed messages for user when login-in / out and search recipes errors
- Moved "Trivia" section to top for better visibility

##### Search form

- Added second button to search form for user to clearly see what he is searching for
- While changing the tags user now see the number of results before searching
- If no recipes found the search button is disabled and user is asked to remove some of the filters
- Removed "Search by" as this was getting too confusing for user. Instead the search input searches for any matching results
- Added min and max length to imput search. JS also checking for input length and enabling / disabling search input btn
- JS now also checking how many recipes are found on input change
- Create separate view for mobile devices search

#### 1.6

- Deployed to Heroku for testing the app on mobile devices
- Added env variables and removed key.py as no longer in use

#### 1.7

- Send out the app to users for testing
- Added links to Footer

#### 1.8

- Added Pagination to recipes and search
- Search class has now option to search without limiting the results

#### 1.9

- Added Voting system for recipes
- Changed the styles of sign-up.html
- Added option to delete recipe

#### 2.0

- Finished Profile page

#### 2.1

- Fixed voting system
- Added few improvements from users stories
- Fixed issue where email address was not storing in database

#### 2.2

- **Changelog**
  - Added README template and change it to suits the project
- **Fixes**  
  - [add-edit-template.html](/templates/add-edit-template.html)
    - Added `autocomplete="off"` to inputs to hide the user stories


### **Testing and improvements**

- xk lines of manual testing which I never documented :(
- FIxed bug in add/edit recipe where JS was incorrectly injecting `maxlength` of 60 instead of 150 in "Steps" section
- Reduced limit on "Ingredients" input `minlength` from 5 to 3
- Moved Alerts to top for better visibility
- Decided to use the mobile search for tablets as well
- At least one tag must be selected to use the for searching recipes
- Fixed bug where user will not be redirected to mobile search on tablets like screens (medium size resolutions)
- Fixed 500 error when trying to print recipe while logged out
- Fixed bug where user could vote for his own recipe.
- Added statement to check if cursor is `None` which occurs when empty form is submitted for example.
- Fixed major glitch. As soon as user voted for one recipe he could not vote for any other recipes as the app said "You already voted for this recipe"

### **Some user feedbacks**

- Fixed many typos
- Changed the "Welcome" message in profile page
- Increased `setTimeout()` from 5s to 7s in `flashed_messages()` as some of the messages was hard to read all before disappearing
- If not logged in user can now click on "You must be loged in to vote / edit recipe" to bring the log in modal
- Made "Register an Account" to looks like a btn for better visibility
- Reduced input search `minlength` from 5 to 4 for words like a "Fish" for example

### **Need to fix**

- somehow add partial search in the form
- add second field for cross check the password in register form
- maybe add email as required field and / or allow users to login via email
- disable drop-down with user stories in add / edit recipe
- check-boxes needs to align better on mobile view
- add more custom CSS
- need to add more JS for better user xp

#### BS4 Flex-box iOS

Encountered many glitches with Flexbox and iOS (especially tablets). Where some of them are still present and therefore the app is not fully responsive with older versions of Safari.

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
            - Released v40 https://p4-cookbook.herokuapp.com/ deployed to Heroku

[**To top**](#Table-of-Contents)

<hr />

## **How to run the project locally?**

<!-- Edit -->

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
   - SECRET_KEY `my_secret_key`
   - DEVELOPMENT (optional)
7. Run the application
   - `python app.py`
8. The application should now run on your `localhost:5000`

[**To top**](#Table-of-Contents)

<hr />

## **What could be done better?**

- Could take the advantage of WTForms which could greatly speed up the development
- MUCH better error handling. Right now, minimum to none
- Again, tests has been done manually or with little use of automated tests
- Also need to push to GitHub more often and or number the pushes more clearly

[**To top**](#Table-of-Contents)

<hr />

## **Credits**

### Special thanks to

- **everyone for finding few minutes to test the project!**

  *All of you gave me constructive feedback which made the project better* 😊

[**To top**](#Table-of-Contents)