#Given three temperatures, this program outputs their maximum, minimum, and average

temp_1 = float(input("Enter first sensor reading:")) #input formulas, with float so they can be decimals
temp_2 = float(input("Enter second sensor reading:"))
temp_3 = float(input("Enter third sensor reading:"))

if -70 < temp_1 < 50: 
    #any condition where first temperature is valid
    if -70 < temp_2 < 50:
        if -70 < temp_3 < 50: 
            #output if all three temperatures are in range
            X = max(temp_1, temp_2, temp_3)
            Y = min(temp_1, temp_2, temp_3)
            Z = (temp_1 + temp_2 + temp_3)/3
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
        else: #output if temperature 3 is only one out of range
            X = max(temp_1, temp_2)
            Y = min(temp_1, temp_2)
            Z = (temp_1 + temp_2)/2
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
    else:
        if -70 <temp_3 < 50: 
            #output if temperature 2 is only one out of range
            X = max(temp_1, temp_3)
            Y = min(temp_1, temp_3)
            Z = (temp_1 + temp_3)/2
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
        else: 
            #output if both temperatures 2 and 3 are out of range
            X = temp_1
            Y = temp_1
            Z = temp_1
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
else: 
    #when temperature 1 is out of range
    if -70 < temp_2 < 50: 
        if -70 < temp_3 < 50: 
            #output if temperature 2 and 3 are in range
            X = max(temp_2, temp_3)
            Y = min(temp_2, temp_3)
            Z = (temp_2 + temp_3)/2
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
        else: 
            #output if only temperature 2 is in range
            X = temp_2
            Y = temp_2
            Z = temp_2
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
    else: 
        #output if only temperature 3 is in range
        if - 70 < temp_3 < 50:
            X = temp_3
            Y = temp_3
            Z = temp_3
            print("Today, the maximum temperature was", X, "degrees, the minimum temperature was", Y, "degrees, and the average temperature was", Z, "degrees Celsius.")
        else: 
            #output if all are out of range
            print("Broken sensor!")
