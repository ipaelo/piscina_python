# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 10:48:53 by itorres-          #+#    #+#              #
#    Updated: 2023/03/17 10:48:54 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
	"""Divide el texto de acuerdo al valor de sep y producirá las sub-strings. option especifica si una acción se realizará sobre las sub-strings antes de ser producidas. """
	if not isinstance(text,str):
		print("ERROR")
	if option != None and not option in ["shuffle","unique","ordered"]:
		print("ERROR")
	word_list = text.split(sep)
	if option == "shuffle":
		random.shuffle(word_list)
	if option == "unique":
		word_list = set(word_list)
	if option == "ordered":
		word_list.sort()
	for item in word_list:
		yield item

