# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:35:53 by itorres-          #+#    #+#              #
#    Updated: 2023/03/14 14:05:57 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Put this at the top of your kata01.py file
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for x in kata:
   print(x,"was created by",kata[x])