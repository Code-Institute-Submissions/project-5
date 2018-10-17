# The Cookbook

## CI project-4

### Changelog

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
- Added filters and errors handling in add / endit form
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
- Added min and max length to imput search. JS also chceking for input length and enabling / disabling search input btn
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

- Added Voting system  for recipes
- Changed the styles of sign-up.html
- Added option to delete recipe

#### 2.0

- Finished Profile page

## Testing and improvements

- xk lines of manual testing which I never documented :(
- FIxed bug in add/edit recipe where JS was incorectly injecting `maxlength` of 60 instead of 150 in "Steps" section
- Reduced limit on "Ingredients" input `minlength` from 5 to 3
- Moved Alerts to top for better visibility
- Decided to use the mobile search for tablets as well
- At least one tag must be selected to use the for for searching recipes
- Fixed bug where user will not be redirected to mobile search on tablets like screens (medium size resolutions)
- Fixed 500 error when trying to print recipe while loged out
- Fixed bug where user could vote for his own recipe.
- Added statment to check if cursor is `None` which occurs when empty form is submited for example.

#### BS4 Flex-box iOS 

Encountered many glitches with Flexbox and iOS (especially tablets). Where some of them are still present and therefore the app is not fully responsive with older versions of Safari.

- Fixed issue where user was unable to acess the search on iOS tablets. Was forced to use JS at the end to change the `a` to `button` on lg and xl screens.
- Found workaround with search form will not trigger event on checkbox change and / or input change. Using JS to check if user using Safari on tablet / mobile view and if so the attr `disabled` is removed so user can use the form. 


### What could be done better

- Could take the advantege of WTForms which could greatly speed up the development
- MUCH better error handling. Right now minimum to none
- Again tests has been done manualy or with litlle use of automated tests
- Also need to push to GitHub more often and or number the pushes more clearly
- Still think that this project is "better" done by SQL due to relation between recipes, tags and so on