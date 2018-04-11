from math import sqrt

def quadratic(a, b, c):
    a1 = a * a
    b1 = 2 * (b * c)
    a2 = a * 2
    try:
        b2 = sqrt(b1)
    except(ValueError):
        print("B or C has a negative value.")

    try:
        if (b2).is_integer():
            aP = a1 + b2
            aN = a1 - b2
            x1 = aP / a2
            int(x1)
            x2 = aN / a2
            int(x2)
            print("x = " + str(x1) + ", " + str(x2))
        elif not (b2).is_integer():
            exact = input("B is not an integer. Would you like the exact answer?")
            if exact == "yes":
                print("x = (" + str(a1) + " ± √" + str(b1) + ") ÷ " + str(a2))
            elif exact == "no":
                aP = a1 + b2
                aN = a1 - b2
                x1 = aP / a2
                int(x1)
                x2 = aN / a2
                int(x2)
                print("x = " + str(x1) + ", " + str(x2))
            else:
                print("Please answer 'yes', or 'no'.")
        else:
            print("Couldn't check if √b is an integer.")
    except(UnboundLocalError):
        exit(0)


INPUT_A = input("What is a?")
#it tells the user how to find the equation if their input includes find
if ("find") in INPUT_A:
    print("ax^2 + bx + c = 0")
else:
    int(INPUT_A)
    INPUT_B = input("What is b?")
    int(INPUT_B)
    INPUT_C = input("What is c?")
    int(INPUT_C)
    quadratic(int(INPUT_A), int(INPUT_B), int(INPUT_C))
