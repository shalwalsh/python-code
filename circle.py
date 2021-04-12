#Program that calculates the circumfrence and area of a circle of a given radius
#Will return Invalid Input if given a negative value

import math
Radius = float(input("Please enter the radius of a circle:"))
Circumfrence = 2*R*math.pi 
Area = math.pi*R**2 
if R < 0: 
    print("Invalid input!")
else: 
    print("A circle with radius", R, "has circumfrence", C, "and area", A)
    
