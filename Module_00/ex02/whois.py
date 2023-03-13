import sys

if len(sys.argv) > 1:
    
    number = sys.argv[1];

    if number[0] == "-":
        number.lstrip("-")
    if len(sys.argv) == 2 and number.isdigit():
        if int(sys.argv[1]) == 0:
            print("Es un cero")
        elif int(sys.argv[1]) % 2 == 0:
            print("Esto es par")
        else:
            print("Es impar")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
    elif not sys.argv[1].isdigit():
        print("AssertionError: argument is not an integer")


