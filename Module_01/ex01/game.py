class GotCharacter:
	def __init__(self, first_name, is_alive):
		
		if type(first_name) is not str:
			return(print("El nombre no es un string"))
		if type(is_alive) is not bool:
			return(print("Debe valer True or False"))
		self.first_name = first_name
		self.is_alive = True

class Stark(GotCharacter):
	"""A class representing the Stark family. Or when bad things happen to good people."""
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive) 
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		self.is_alive = False
