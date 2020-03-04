#SQLAlchemy & AJAX

from flask_sqlalchemy import SQLAlchemy 
import datetime


# Instantiate a SQLAlchemy object. We need this to create our db.Model classes.
db = SQLAlchemy()


##############################################################################



class User(db.Model):
    """Data model for a User."""

    __tablename__ = "users"

    #  columns and/or relationships here
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False)

    username = db.Column(db.String(25), nullable=False, unique=True,)

    password = db.Column(db.String(25), nullable=False,)


    """Return a human-readable representation."""

        #  __repr__ method    
    
    def __repr__(self):

        return f"<User user_id={self.human_id} username={self.fname}>"





class Ingredient(db.Model):
    """Data model for Ingredient."""

    __tablename__ = "ingredients"

    # columns and/or relationships here
    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False,)
    #defining the relationship here
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ######################
    ingredient_name = db.Column(db.String(50), nullable=False, unique=True,)

    quantity = db.Column(db.Float(25), nullable=False,)

    units = db.Column(db.String(25), nullable=True,)

    users = db.relationship("User", backref="ingredients")

    
    


    def __repr__(self):

        return f"<Ingredient ingredient_id={self.ingredient_id} user_id={self.user_id} ingredient_name={self.ingredient_name} quantity={self.quantity} units={self.units}>"





class Menu(db.Model):
    """Data model for Menu."""

    __tablename__ = "menus"

    # columns and/or relationships here
    menu_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False,)
    #defining the relationship here
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    
    plan_date = db.Column(db.datetime, nullable=False,)

    users = db.relationship("User", backref="menus")



    def __repr__(self):

        return f"<Menu menu_id={self.menu_id} user_id={self.user_id} plan_date={self.plan_date}>"







class Recipe(db.Model):
    """Data model for Ingredient."""

    __tablename__ = "recipes"

    # columns and/or relationships here
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False,)
    #defining the relationship here
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    ######################
    recipe_name = db.Column(db.String(50), nullable=False, unique=True,)

    recipe_link = db.Column(db.String, nullable=False,)

    recipe_text = db.Column(db.String, nullable=True,)

    users = db.relationship("User", backref="recipes")


    def __repr__(self):

        return f"<Recipe recipe_id={self.recipe_id} user_id={self.user_id} recipe_name={self.recipe_name} recipe_link={self.recipe_link} recipe_text={self.recipe_text}>"




class Recipeingredient(db.Model):
    """Data model for Ingredient."""

    __tablename__ = "recipeingredients"

    # columns and/or relationships here
    recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False,)
    #defining the relationship here
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'))

    ingredient_id = db.Column(db.Integer, db. ForeignKey('ingredients.ingredient_id'))
    ######################
    quantity = db.Column(db.Float(25), nullable=False,)

    units = db.Column(db.String(25), nullable=False,)


    recipes = db.relationship("Recipe", backref="recipeingredients")

    ingredients = db.relationship("Ingredient", backref="recipeingredients")




    def __repr__(self):

        return f"<Recipeingredient recipe_ingredient_id={self.recipe_ingredient_id} recipe_id={self.recipe_id} ingredient_id={self.ingredient_id} quantity={self.quantity} units={self.units}>"




class Menurecipe(db.Model):
    """Data model for Ingredient."""

    __tablename__ = "menurecipes"

    # columns and/or relationships here
    menu_recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True,
                                nullable=False,)
    #defining the relationship here
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.menu_id'))

    recipe_id = db.Column(db.Integer, db. ForeignKey('recipes.recipe_id'))
    ######################

    menus = db.relationship("Menu", backref="menurecipes")

    recipes = db.relationship("Recipe", backref="menurecipes")
    

    def __repr__(self):

        return f"<Menurecipe menu_recipe_id={self.menu_recipe_id} menu_id={self.menu_id} recipe_id={self.recipe_id}>"

# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///ingredients"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
