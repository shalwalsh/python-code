import numpy as np
import matplotlib.pyplot as plt
import math


def my_cos(x):
    function = 1
    factorial = 2 * 1
    i = 1
    while True:
        new_term = ((-1) ** i) * ( x ** (2*i)) / factorial
        function += new_term
        old_factorial = factorial
        factorial = old_factorial * (i+2) * (i+3)
        i += 1
        
        if new_term < 0.000001:
            break
    return function
x_values = np.arange(0, 20, 1)
print([my_cos(x) for x in x_values], [np.cos(x) for x in x_values])
plot_func = [x * 0.2 + 0.4 * my_cos(x) for x in x_values]
y_values = plot_func

plt.scatter(x_values, [my_cos(x) for x in x_values])
plt.show()
        
    
    
    