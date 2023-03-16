from datetime import datetime
from recipe import Recipe

class Book:
	def __init__(self, name):	
		if type(name) is not str:
			return(print("El nombre no es un string"))
		self.name = name
		self.last_update = datetime.now()
		self.creation_date = datetime.now()
		self.recipes_list = {"starter":[],"lunch":[],"dessert":[]}

	def get_recipe_by_name(self, name):
		"""Obtiene una receta"""
		for recipes_type in self.recipes_list:
			for recipe in self.recipes_list[recipes_type]:
				if recipe.name == name:
					print(recipe)
					return recipe
		return False

	def get_recipes_by_types(self, recipe_type):
		"""Devuelve una lista de nombres de recetas"""
		recipes_names = list()
		if recipe_type in self.recipes_list:
			recipes_list= self.recipes_list[recipe_type]
			for recipe in recipes_list:
				recipes_names.append(recipe.name)
		return recipes_names

	def add_recipe(self, recipe):
		"""Añade una receta al libro y actualiza last_update"""
		if not isinstance(recipe, Recipe):
			print("No es una receta")
		self.recipes_list[recipe.recipe_type].append(recipe)
		self.last_update=datetime.now()
