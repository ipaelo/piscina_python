# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:32:50 by itorres-          #+#    #+#              #
#    Updated: 2023/03/14 13:32:51 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
	print("Uso: python operations.py número1 número2")
	
elif len(sys.argv) < 3 or len(sys.argv)>3:
	print("Error en los argumentos")
else:
	try:
		numero1 = int(sys.argv[1])
		numero2 = int(sys.argv[2])
		print("Suma:",numero1+numero2)
		print("Resta:",numero1-numero2)
		print("Producto:",numero1*numero2)
		if numero2 == 0:
			print("División: ERROR (división entre cero)")
			print("Resto: ERROR (resto entre cero)")
		else:
			print("División:",numero1/numero2)
			print("Resto:",numero1%numero2)
	except:
  		print("Uno de los parámetros o los dos no son enteros")
	
	
    
