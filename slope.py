y1 = input("What is y1?")
y2 = input("What is y2?")
x1 = input("What is x1?")
x2 = input("What is x2?")

Slope = (int(y1) - int(y2)) / (int(x1) - int(x2))
b = int(y1) - (int(Slope) * int(x1))

if b > 0:
    sign = "+ "
elif b == 0:
    sign = " "
else:
    sign = "- "

print("Y = " + str(Slope) + "X " + sign + str(b))
