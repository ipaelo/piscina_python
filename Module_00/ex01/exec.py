import sys
 

if len(sys.argv) > 1:
    var1 = " ".join(sys.argv[1:]).swapcase()
    print(var1[::-1])
