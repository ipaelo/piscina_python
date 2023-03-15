# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:32:40 by itorres-          #+#    #+#              #
#    Updated: 2023/03/14 13:32:54 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
    
    number = sys.argv[1]

    if number[0] == "-":
        number=number[1:]
    if len(sys.argv) == 2 and number.isdigit():
        if int(number) == 0:
            print("Es un cero")
        elif int(number) % 2 == 0:
            print("Esto es par")
        else:
            print("Es impar")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif not number.isdigit():
        print("AssertionError: argument is not an integer")


