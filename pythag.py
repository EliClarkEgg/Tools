from math import *

def Codes():
    print("1: 2 legs")
    print("2: a leg and the hypotenuse")
    print("3: a leg and all angles")

print("To see the codes type 'Codes'")
code = input("What is your code?")

if code == "Codes":
    Codes()
elif code == "1":
    FirstLeg = input("What is the measure of the first leg?")
    SecondLeg = input("What is the measure of the other leg?")
    Hypotenuse
