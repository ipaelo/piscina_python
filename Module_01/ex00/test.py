from book import Book
from recipe import Recipe

libro = Book("Cookbook")

a = Recipe("tortilla",4,50,["papas","huevos"],"","lunch")
b = Recipe("puchero",5,50,["papas","zanahoria"],"","lunch")
c = Recipe("arroz con leche",2,30,["leche","arroz"],"","dessert")
d = Recipe("aceitunas",1,5,["aceitunas"],"","starter")

libro.add_recipe(a)
libro.add_recipe(b)
libro.add_recipe(c)
libro.add_recipe(d)
libro.get_recipe_by_name("aceitunas")
print(libro.get_recipes_by_types("lunch"))
