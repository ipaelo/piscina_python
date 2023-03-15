# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/15 11:46:09 by itorres-          #+#    #+#              #
#    Updated: 2023/03/15 11:46:10 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if not len(sys.argv) == 3:
    print("ERROR")
else:
	try:
		cadena = (sys.argv[1])
		numero = int(sys.argv[2])
		print([word for word in cadena.split() if len(word)>numero])
	except:
  		print("ERROR")