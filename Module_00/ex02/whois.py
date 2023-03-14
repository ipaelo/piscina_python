import sys

if len(sys.argv) > 1:
    
    number = sys.argv[1];

    if number[0] == "-":
        number.lstrip("-")
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


