class Recipe:
	def __init__(self, name, lvl, time,ingredients,description, recipe_type):
		
		if type(name) is not str:
			return(print("El nombre no es un string"))
		if type(lvl) != int or lvl not in range(1,5): 
			return(print("La dificultad debe estar entre 1 y 5"))
		if type(time) != int and time < 0:
			return(print("El tiempo de cocinado deber ser positivo"))
		if type(ingredients) != list:
			return(print("Los ingredientes deben ser cadenas de caracteres"))
		if not recipe_type in ('entrante', 'comida', 'postre'):
			return(print("El tipo de receta es entrante, comida o postre"))
		self.name = name
		self.cooking_lvl = lvl
		self.cooking_time = time
		self.ingredients = ingredients
		self.description = description
		self.recipe_type = recipe_type

def __str__(self):
	txt = "Imprimiendo"
	return txt
a = Recipe("tortilla",3,20,["papas","huevo"],"","posdtre")

        
