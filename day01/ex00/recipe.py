#!/usr/bin/env python


class Recipe:
    """A simple example class"""

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe"
        """Your code goes here"""
        return txt
