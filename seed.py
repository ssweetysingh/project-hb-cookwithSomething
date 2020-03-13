import datetime
from sqlalchemy import func

from model import User, Ingredient, Recipe, Recipeingredient connect_to_db, db
from server import app


# def load_users():
#     """Load users from u.user into database."""

#     print("Users")

#     for i, row in enumerate(open("seed_data/user.seed.txt")):
#         row = row.rstrip()
#         user_id, username, password = row.split("|")

#         user = User(user_id=user_id,
#                     username=username,
#                     password=password)

#         # We need to add to the session or it won't ever be stored
#         db.session.add(user)

#         # provide some sense of progress
#         if i % 100 == 0:
#             print(i)

#     # Once we're done, we should commit our work
#     db.session.commit()


def load_ingredients():
    """Load ingrdients into database."""

    print("Ingredients")

    for i, row in enumerate(open("seed_data/ingredients.seed.txt")):
        row = row.rstrip()

        user_id, ingredient_id, ingredient_name, quantity, units = row.split("|")[:5]

        
        ingredient = Ingredient(ingredient_id=ingrdient_id,
                      ingredient_name=ingredient_name,
                      quantity=quantity,
                      units=units)

        # We need to add to the session or it won't ever be stored
        db.session.add(ingredient)

        # provide some sense of progress
        if i % 100 == 0:
            print(i)

    # Once we're done, we should commit our work
    db.session.commit()


def load_recipe():
    """Load recipes into database."""

    print("Recipes")

    for i, row in enumerate(open("seed_data/recipe.seed.txt")):
        row = row.rstrip()

        user_id, recipe_id, recipe_name, recipe_link = row.split("\t")

        user_id = int(user_id)
        recipe_id = int(recipe_id)
        recipe_link = str(recipe_link)


        recipe = Recipe(user_id=user_id,
                        recipe_id=recipe_id,
                        recipe_name=recipe_name
                        recipe_link=recipe_link)

        # We need to add to the session or it won't ever be stored
        db.session.add(recipe)

        # provide some sense of progress
        if i % 1000 == 0:
            print(i)

            # An optimization: if we commit after every add, the database
            # will do a lot of work committing each record. However, if we
            # wait until the end, on computers with smaller amounts of
            # memory, it might thrash around. By committing every 1,000th
            # add, we'll strike a good balance.


    # Once we're done, we should commit our work
    db.session.commit()

def load_recipeingredient():
    """Load recipeingrdients"""

    print("Recipeingredients")

    for i, row in enumerate(open("seed_data/recipeingrdient.seed.txt")):
        row = row.rstrip()

        recipe_ingredient_id, recipe_id, ingredient_id, quantity, units = row.split("\t")

        recipeingrdient_id = int(recipeingredient_id)
        recipe_id = int(recipe_id)
        ingredient_id = int(ingredient_id)
        quantity = float(quantity)
        units = str(units)

        # We don't care about the timestamp, so we'll ignore this

        recipeingrdient = Recipeingredient(recipeingredient_id=recipeingredient_id,
                        recipe_id=recipe_id,
                        ingredient_id=ingredient_id
                        quantity=quantity
                        units=units)

        # We need to add to the session or it won't ever be stored
        db.session.add(recipe)

        # provide some sense of progress
        if i % 1000 == 0:
            print(i)

            # An optimization: if we commit after every add, the database
            # will do a lot of work committing each record. However, if we
            # wait until the end, on computers with smaller amounts of
            # memory, it might thrash around. By committing every 1,000th
            # add, we'll strike a good balance.

    db.session.commit()


def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_ingredients()
    load_recipes()
    load_recipeingredient()
    set_val_user_id()

    
    sweetysing = User(email="sweetysing@gmail.com",
                   password="1234")
    db.session.add(sweety)
    db.session.commit()

    
