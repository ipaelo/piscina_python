class Evaluator:
	def zip_evaluate(coefs, words):
		if len(coefs) != len(words):
			return(-1)
		print(zip(coefs*len(words))) 

	def enumerate_evaluate(coefs, words):
		if len(coefs) != len(words):
			print("ERROR")