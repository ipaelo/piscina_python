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