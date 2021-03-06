from peewee import CharField, TextField
from app.models import BaseModel
from peewee import CharField
from playhouse.shortcuts import model_to_dict
from app.utils.utils import get_simple_string

ALLERGENE_LIST = [
    "Gluten",
    "Oeufs",
    "Lactose",
    "Fruits à coque",
    "Arachides",
    "Moutarde",
    "Soja",
    "Sulfites",
    "Sésame",
    "Poissons",
    "Crustacés",
    "Mollusques",
    "Céleri",
    "Lupins",
]
SIMPLE_ALLERGENE_LIST = [ get_simple_string(s) for s in ALLERGENE_LIST ]

class RecipeCategorie:
    cat_list = [
        "Food truck",
        "Autres",
    ]
    FOOD_TRUCK = cat_list[0]
    AUTRES = cat_list[1]
RECIPE_CATEGORIE = RecipeCategorie()

class Recipe(BaseModel):
    name = CharField()  # name of the recipe
    file_id = CharField()  # id of the recipe file
    img_id = CharField()  # google drive link to image
    img_path = CharField()  # image path
    allergene = CharField()  # recipe allegenic
    categorie = CharField()  # recipe categorie

    # search parameters
    search_name = CharField()
    search_ingredients = TextField()
    search_etapes = TextField()
    search_allergene = TextField()

    def to_dict(self, exclude=None, include=None):
        """
        This base method is made to be overridden when you need something removed to added to the returned dictionary
        """
        if include is None:
            include = {}
        if exclude is None:
            exclude = []
        returned_dict = model_to_dict(self)
        for i in exclude:
            returned_dict.pop(i)
        for key, value in include.items():
            returned_dict[key] = value
        return returned_dict