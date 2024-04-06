
import numpy as np # numerical package so we can use special math constants and functions
#plot function
import matplotlib.pyplot as plt #package so we can plot the function
variance = 5 #pick a value for sigma
mean=4   #Pick a value for mu

#define function
def normal_density(mean, variance, x):
    return (1/(np.sqrt(2*np.pi*(variance**2)))*np.exp((-(x-mean)**2)/(2*variance**2)))
print(normal_density(1,1,0))

x = np.linspace(0, 10, 100)
plt.plot(x, normal_density(mean, variance, x), color = "red") #Use linspace to make a line connecting point
plt.xlabel("x") #Labelling x axis
plt.ylabel("y") #Labelling y axis
plt.title("Normal Density")
plt.show()

#INTEGRATE THE DENSITY FUNCTION TO GET PROBABILITY

import numpy as np
#integrating function from 162 (lower bound) to 190(upper bound)
a = 162
b = 190

# assigning values given for mean and variance
mean = 171
variance_squared = 50.41

# define function for normal density 
def normal_density(x, mean, variance_squared):
    return 1 / (np.sqrt(2 * np.pi * variance_squared)) * np.exp(-(x - mean)**2 / (2 * variance_squared))

# use trapezoidal rule to numerically integrate and assign 1000 points for good estimation
def integration(func, a, b, num_intervals=1000):
    x_values = np.linspace(a, b, num_intervals + 1)
    y_values = func(x_values)
    integral_value = np.trapz(y_values, x_values)
    return integral_value

# Define the normal density function now to use the given variables
def normal_density_function(x):
    return normal_density(x, mean, variance_squared)

# Calculate the probability using numerical integration
probability = integration(normal_density_function, a, b)

print(f'The probability or proportion of a with a height between {a} cm and {b}cm is: {probability}')

