import math

r = input("What is the radius? ")

if r.isnumeric() ==  False:
    print("This is not a positive number.")
elif float(r) < 0:
    print("This is not a positive number.")
else:
    r = float(r)
    a = math.pi * math.sqrt(r)
    c = 2 * math.pi * r
    print("The radius was: ", r, "units")
    print("The area is: ", a, "square units")
    print("The circumference is: ", c, "units")