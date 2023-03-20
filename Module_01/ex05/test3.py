# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test3.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/14 13:54:23 by isojo-go          #+#    #+#              #
#    Updated: 2023/03/20 14:31:04 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from the_bank import Account, Bank

if __name__ == "__main__":
    bank = Bank()
    acc_valid_1 = Account('Sherlock Holmes',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=1000.0)
    acc_valid_2 = Account('James Watson',
                          zip='NW1 6XE',
                          addr='221B Baker street',
                          value=25000.0,
                          info=None)
    
    acc_invalid_4 = Account("Douglass",
                            zip='42',
                            addr='boulevard bessieres',
                            value=42)
    acc_invalid_1 = Account("Adam",
                            value=5000,
                            zip='0',
                            addr='Somewhere')
    acc_invalid_2 = Account("Bender Bending Rodríguez",
                            zip='1',
                            addr='Mexico',
                            value=42)
    acc_invalid_3 = Account("Charlotte",
                            zip='2',
                            addr='Somewhere in the Milky Way',
                            value=42)
    acc_invalid_5 = Account("Edouard",
                            zip='3',
                            addr='France',
                            value=42)
    
    bank.add(acc_valid_1)
    bank.add(acc_valid_2)
    bank.add(acc_invalid_1)
    bank.add(acc_invalid_2)
    bank.add(acc_invalid_3)
    bank.add(acc_invalid_4)
    bank.add(acc_invalid_5)


    if bank.transfer('Douglass', 'Edouard', 1000.0) is False:
       print('Failed')
       bank.fix_account('Douglass')
       bank.fix_account('Smith Jane')
    ## ...
    if bank.transfer('Sherlock Holmes', 'James Watson', 1000.0) is False:
        print('Failed')
    else:
        print('Success')