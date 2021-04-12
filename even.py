#Program that prints out even numbers within a specified range, as well as their sum
#Both input parameters must be positive integers, with the first being lesser than the second

m = int(input("Enter first number:")) 
n = int(input("Enter second number:")) 
s = 0 #so that s starts at zero

if m > n or m < 0 or n < 0: 
    print("Invalid input!")
else: 
    print("Sequence:", end=" ") 
    for i in range(m+1,n):
        if i%2 == 0: 
            print(i, end=",") 
            s = s + i 
    print(" ") 
    print("Sum:", s)
