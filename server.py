
from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
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

@app.route('/home')
def home():
    """Show Homepage."""

    return render_template('homepage.html')

@app.route('/register', methods=['GET'])
def register_form():
    """Show form for create profile."""

    return render_template("register.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process create profile page."""

    # Get form variables
    username = request.form["username"]
    password = request.form["password"]
    

    new_user = User(username=username, password=password)


    db.session.add(new_user)
    db.session.commit()

    flash(f"User {username} added.")
    return redirect("/login")


@app.route('/login', methods=['GET'])
def login_form():
    """Show login page."""

    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No such user")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id

    '''jsonify login page'''

    # if username and password:
    #     name = username

    #     return jsonify({'username' : name})

    # return jsonify({'error' : 'Missing fields'})

    flash("Logged in")
    return redirect("/home")



@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/home")


# @app.route('/create profile')
# def create_account_page():
#     """Display account creation form."""

#     return render_template("register.html")

@app.route('/recipes')
def recipe():
    # A query to retrieve a recipe based on id
    return render_template('recipe.html')

@app.route('/ingredients')
def ingredient():
    # A query to retrieve all recipes that match this ingredient
    # TODO: use a user_id stored in session, not one that is hard coded :)
    if session.get("user_id") is None:
        return redirect("/login")
    else:
        user_id = session["user_id"]
        app.logger.info("User Id: %s",user_id)
        ingredients = Ingredient.query.filter_by(user_id=user_id)
        return render_template('ingredient.html', ingredients=ingredients)


@app.route('/recipes/<ingredient_id>')
def recipe_ingredients(ingredient_id):
    """Show results for ingredients in recipe."""
    recipes = Recipe.query.filter(Ingredient.ingredient_id == ingredient_id).all()
    
    #return render_template("recipe.html")
    #return redirect("/recipes")
    return render_template("recipe2.html")



if __name__ == "__main__":
        # We have to set debug=True here, since it has to be True at the point
        # that we invoke the DebugToolbarExtension

        # Do not debug for demo
    app.debug = True

    connect_to_db(app)

        # Use the DebugToolbar
    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")
