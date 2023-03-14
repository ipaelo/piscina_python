import sys
import string   

def text_analyzer(cadena = None):
    """Esta función cuenta caracteres, mayúsculas, minúsculas, signos de puntuación  y espacios."""
    if cadena == None:
        print("¿Qué texto quieres analizar") 
        cadena = input()          
    if not isinstance(cadena, str): 
        print("Error: No es una cadena")
    else: 
        print("Este texto tiene ",len(cadena)," caracteres\n")
        print("-", len([c for c in cadena if c.isupper()]), " mayúsculas\n") 
        print("-", len([c for c in cadena if c.islower()]), " minúsculas\n") 
        print("-", len([c for c in cadena if c.isspace()]), " espacios\n")
        i = 0
        for c in cadena:
         if c in string.punctuation:
                i = i+1
        print("-", i, " son signos de puntuación\n") 
         
if __name__ == "__main__":
        if len(sys.argv) < 2:
             cadena = None
        else:
             cadena = sys.argv[1]
        text_analyzer(cadena)