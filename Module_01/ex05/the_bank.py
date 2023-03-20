# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    the_bank.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: itorres- <itorres-@student.42malaga.com    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/17 10:48:56 by itorres-          #+#    #+#              #
#    Updated: 2023/03/20 14:21:33 by itorres-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Account(object): 
	ID_COUNT = 1
	def __init__(self, name, **kwargs): 
		self.__dict__.update(kwargs)

		self.id = self.ID_COUNT 
		Account.ID_COUNT += 1 
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0

		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
		
		def transfer(self, amount): 
			self.value += amount

class Bank(object):
	def __init__(self):
		self.accounts = []
	def add(self, new_account):
		""" Add new_account in the Bank
			@new_account: Account() new account to append
            @return   True if success, False if an error occured
        """
		if isinstance(new_account,Account) and new_account not in self.accounts:
			self.accounts.append(new_account)

	def corrupted(self, account):
		if len(account.__dict__) % 2 == 0:
			return True
		if (not(hasattr(self, 'name') and type(self.__dict__['name']) == str)):
			return True
		if 'id' not in account.__dict__.keys:
			return True	
		if 'value' not in account.__dict__.keys:
			return True
		zip = 0
		addr = 0
		for a in account.__dict__.keys:
			if a.startswith('b'):
				return True
			if a.startswith('zip'):
				zip = 1
			if a.startswith('addr'):
				addr = 1
		if zip == 0 or addr == 0:
			return True
		if not isinstance(account.name,str):
			return True
		if not isinstance(account.id,int):
			return True
		if not isinstance(account.value,int) or not isinstance(account.value,float):
			return True
		return 0


	
	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
		"""
	
		if amount < 0:
			return False
		existe_or = 0
		existe_de = 0
		
		for cuenta in self.accounts:
			if cuenta.name == origin:
				existe_or = cuenta
			if cuenta.name == dest:
				existe_de = cuenta

		if existe_or == 0 or existe_de == 0:
				print("Alguna cuenta no existe")
				return False
			
		if amount <= 0 or existe_or.value < amount:
				print("No hay fondos")
				return False

		if existe_or.name != existe_de.name:
				existe_or.value = existe_or.value - amount
				existe_de.value = existe_de.value + amount
				print("Transferencia realizada")
				return True
	

	def fix_account(self, name):
		""" fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """
		if not isinstance(name,str):
			return False		
		existe = 0
		for cuenta in self.accounts:
			if cuenta.name == name:
				existe = cuenta
		if existe == 0 or not isinstance(name,str):
			print("La cuenta no existe")
			return False
		if  not hasattr(cuenta, 'id'):
			existe.__setattr__('id', Account.ID_COUNT) 
			Account.ID_COUNT = Account.ID_COUNT + 1
		if not hasattr(cuenta, 'value'):
			existe.__setattr__('value', 0) 
		zip = 0
		addr = 0
		for a in existe.__dict__.keys():
			if a.startswith('b'):
				existe.__dict__.pop(a)
			if a.startswith('zip'):
				zip = 1
			if a.startswith('addr'):
				addr = 1
		if zip == 0:
			existe.__setattr__('zip', 00000)			
		if addr == 0:
			existe.__setattr__('address', "Sin dirección")
		if len(existe.__dict__.keys()) % 2 == 0:
			if (hasattr(existe, 'aborrar')):
				existe.__delattr__('aborrar')
			else:
				existe.__setattr__('aborrar', 'aborrar')
	
		if self.corrupted(existe):
			return False
		else:
			print("Cuenta corregida")
			return True
