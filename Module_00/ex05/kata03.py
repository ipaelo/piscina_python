# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata03.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:35:53 by itorres-          #+#    #+#              #
#    Updated: 2023/03/14 14:27:19 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata03.py file
kata = "The right format"

number = len(kata)

for i in range(42 - number -1):
    print("-",end='')
print(kata)  

