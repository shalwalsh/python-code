import math #to use value of pi
R = float(input("Please enter the radius of a circle:")) #this is where user will input their radius, i put float so it will work with decimals
C = 2*R*math.pi #formula for circumfrence
A = math.pi*R**2 #formula for area
if R < 0: #if radius is negative
    print("Invalid input!")
else: #so any other input will give results
    print("A circle with radius", R, "has circumfrence", C, "and area", A) #output phrase
    