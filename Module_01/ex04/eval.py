# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 10:48:45 by itorres-          #+#    #+#              #
#    Updated: 2023/03/17 10:48:46 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Evaluator:
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return(-1)
		total = 0
		for (coefs,words) in zip(coefs,words):
			total = total + len(words)*coefs
		print(total) 

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			return(-1)
		total = 0
		for i, element in enumerate(coefs):
			total = total + len(words[i])*element
		print(total) 