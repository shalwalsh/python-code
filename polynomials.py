def create():
    user_input = input("Enter polynomial:")
    polynomial = {}
    polynomial_first_stage = user_input.split()
    for i in polynomial_first_stage:
        polynomial_stage_two = i.split("x")
        polynomial[polynomial_stage_two[1]] = polynomial_stage_two[0]
        print('%.2f' % float(polynomial_stage_two[0]) + "x" + polynomial_stage_two[1], end = " ")

def derivative(polynomial, order=1):
    derivative = {}
    print(derivative)
    #n = int(input("Enter order of derivative:"))
    #for key, value in polynomial:
     #   for i in range(n):
      #      print(float(polynomial_stage_two[0])*float(polynomial_stage_two[1]) + x + (float(polynomial_stage_two[1])-1))
            
create()
derivative()
        
            
        
        
    