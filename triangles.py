from math import *

choice = input("sin or tan or cos?")

if choice == "sin":
    number = input("What number?")
    print(sin(int(number)))
    input()
elif choice == "tan":
    number = input("What number?")
    print(tan(int(number)))
    input()
elif choice == "cos":
    number = input("What number?")
    print(cos(int(number)))
    input()
else:
    print("u s e  l o w e r  c a s e  l e t t e r s")
