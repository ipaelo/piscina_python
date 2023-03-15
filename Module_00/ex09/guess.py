# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:45:58 by itorres-          #+#    #+#              #
#    Updated: 2023/03/15 11:45:59 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import sys

adivinanza = random.randint(1, 99)

if __name__ == "__main__":
	print("Vamos a jugar: Adivina el número secreto")
	print("Introduce un número entre 1 y 99 para adivinar el número secreto")
	print("Para salir teclea 'exit")
	print("¡Buena Suerte!")
	print("\n")    
	option = input("Adivina un número entre 1 y 99: ")
	contador = 0
	while(option != "exit"):
		try:
			option = int(option)
			if option == 42:
				print("La respuesta a la gran pregunta de la vida es 42, el universo y absolutamente todo es 42")
				print("¡¡Felicidades!! Lo tienes en el primer intento")	
			elif option > adivinanza:
				print("Te has pasado")
				contador = contador + 1		
			elif option < adivinanza:
				print("Te has quedado corto")
				contador = contador + 1
			else:
				print("¡¡Felicidades!! Lo adivinaste")
				print("Has ganado en ",contador, "intentos")
				exit()
		except:
			print("Esto no es un número!")		
		option = input("Adivina un número entre 1 y 99: ")
	print("¡OOOHHH! ¡Adios!")
