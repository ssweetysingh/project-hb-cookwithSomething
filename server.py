
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Ingredient, Menu, Recipe, Recipeingredient, Menurecipe


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Show Homepage."""

    return render_template('homepage.html')


@app.route('/recipes')
def recipe():
    # A query to retrieve a recipe based on id
    return render_template('recipe.html')

@app.route('/ingredient/<ingredient>')
def ingredient(ingredient):
    # A query to retrieve all recipes that match this ingredient
    return render_template('recipe.html',recipes=recipes)


# @app.route('/recipe/recipe_ingredients')
# def recipe_ingrdients():
#       """Show page for recipes."""

#     recipes = Recipe.query.order_by('recipe_ingredients').all()
#     return render_template("recipe.html")



if __name__ == "__main__":
        # We have to set debug=True here, since it has to be True at the point
        # that we invoke the DebugToolbarExtension

        # Do not debug for demo
    app.debug = True

    connect_to_db(app)

        # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
