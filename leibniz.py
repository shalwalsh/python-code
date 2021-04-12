n = int(input("Please enter the number of terms:")) #input has to be integer since can't do half a new term
X = 1. #since first term doesn't follow formula, i'm starting the variable there. also putting decimal so it prints 1.0 like sample does

for i in range(1,n): #range ends before n so it'll print out correct number of terms
    Y = (((-1)**(i))/(2*i+1)) #this is formula for each new term
    X = X + Y #so that the value printed is the sum

print("The approximate value of pi is", 4*X) #sum multiplied by four since i didn't do that in the original 