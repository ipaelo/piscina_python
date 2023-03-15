# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 14:42:45 by itorres-          #+#    #+#              #
#    Updated: 2023/03/14 15:22:09 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


cookbook = {"bocadillo":{'ingredients':["jamón","queso","pan","tomate"],'meal':"almuerzo",'prep_time':10},
                "tarta":{'ingredients':["harina","azúcar","huevos"],'meal':"postre",'prep_time':60},
                "ensalada":{'ingredients':["aguacate","rúcula","tomates","espinacas"],'meal':"almuerzo",'prep_time':15}}

def print_recipes_name():
    for key in cookbook:
        print(key)

def print_recipes(i):
    try:
        if i in cookbook.keys():
            print("La receta de",i)
            print("Sus ingredientes son: ", cookbook.get(i).get('ingredients'))
            print("Se suele tomar como: ", cookbook.get(i).get('meal'))
            print("Se tarda en preparar: ", cookbook.get(i).get('prep_time'))
    except:
        print("Receta no encontrada")  

def del_recipe(i):
    try:
        del cookbook[i]
    except:
        print("Receta no encontrada") 

def add_recipe():
    recipe = input("Enter a name:")
    ingredients = [element for element in input("Enter ingredients: ").split()] 
    meal = input("Enter a meal type:")
    time = int(input("Enter a preparation time:"))
    cookbook[recipe]={'ingredients':ingredients,'meal':meal,'prep_time':time}
   
if __name__ == "__main__":
 while(True):
    print("Welcome to the Python Cookbook !")
    print("List of available option:")
    print("  1: Add a recipe")
    print("  2: Delete a recipe")
    print("  3: Print a recipe")
    print("  4: Print the cookbook")
    print("  5: Quit")
    try:
        option = int(input("Please select an option:"))
    except:
            print('Wrong input. Please enter a number ...')
    if option == 1:
        add_recipe()
    elif option == 2:
        recipe = input("Enter a recipe to delete:")
        del_recipe(recipe)
    elif option == 3:
        recipe = input("Please enter a recipe name to get its details:")
        print_recipes(recipe)
    elif option == 4:
        print_recipes_name()
    elif option == 5:
        print("Cookbook closed. Goodbye !")
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 5.')