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


recipes_dict = {
    			"nombre": "bocadillo",
                 "ingredients": {"jamón","queso","pan","tomate"},
                 "meal": "almuerzo",
                 "prep_time": 10
                 "nombre":"tarta",
                 "ingredients":{"harina","azúcar","huevos"},
                 "meal": "postre",
                 "prep_time": 60
                 "nombre":"ensalada",
                 "ingredients":{"aguacate","rúcula","tomates","espinacas"},
                "meal":"almuerzo",
                 "prep_time": 15)
                     }}

def print_recipes_name(recipes_dict):
    print(recipes_dict.keys())