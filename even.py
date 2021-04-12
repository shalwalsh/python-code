m = int(input("Enter first number:")) #first input (both input are integers)
n = int(input("Enter second number:")) #second input
s = 0 #so that s starts at zero

if m > n or m < 0 or n < 0: #output if m is less than n or either value is negative
    print("Invalid input!")
else: #output if all inputs are valid
    print("Sequence:", end=" ") #so that sequence is only printed once and there's no new line
    for i in range(m+1,n):
        if i%2 == 0: #all even numbers in range
            print(i, end=",") #no new line, only comma
            s = s + i #this will create the sum updated with i
    print(" ") #so that sum is printed on a new line
    print("Sum:", s) #sum output
    
            
   
           
    
        