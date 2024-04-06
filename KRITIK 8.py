def gradient_descent(x0, y0,f, grad_f, alpha, num_iterations):
    x,y = x0, y0 # Initialize x and y with the initial point
    for i in range(num_iterations):
# obtain the gradient of f at (x, y)
        grad_x, grad_y = grad_f(x,y) # YOUR CODE HERE
# Update x and y by taking a step in the
# opposite direction of the gradient
        x =x0- alpha * grad_x
        y = y0- alpha * grad_y
    return x, y

#code from greg defining function
def fun_1(x,y):
    return x**2+y**2
#partial derivative fofrmula in respect to x then in respect to y 
def grad_f_1(x,y):
    grad_x = 2*x
    grad_y = 2*y
    return grad_x, grad_y

#run through test 1 using the initial point, learning rate (alpha), and number of iterations
x0,y0=0.1,0.1
alpha=0.1
num_iterations=10
x_final,y_final= gradient_descent(x0,y0,fun_1,grad_f_1,alpha,num_iterations) #running the given numbers through the function given above
print("the coordinates of the final point after gradient descent is:",x_final, y_final) #basic print statement

#run through test 2 using the initial point, learning rate (alpha), and number of iterations
x0,y0= -1,1
alpha=0.01
num_iterations=100
x_final,y_final= gradient_descent(x0,y0,fun_1,grad_f_1,alpha,num_iterations)  #running the given numbers through the function given above
print("the coordinates of the final point after gradient descent is:",x_final, y_final)

#code given from greg
import numpy as np
def fun_2(x,y):
    return 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)
#taking the formula of the partial derivative in respect to x then in respect to y 
def grad_f_2(x,y):
    grad_x = 2 * x * np.exp(-x**2 - (y - 2)**2) + 4 * x * np.exp(-x**2 - (y + 2)**2)
    grad_y = 2 * (y - 2) * np.exp(-x**2 - (y - 2)**2) + 4 * (y + 2) * np.exp(-x**2 - (y + 2)**2)
    return grad_x, grad_y

#run through test 1 using the initial point, learning rate (alpha), and number of iterations
x0,y0=0,1
alpha=0.01
num_iterations=10000
x_final,y_final= gradient_descent(x0,y0,fun_2,grad_f_2,alpha,num_iterations)
print("the coordinates of the final point after gradient descent is:",x_final, y_final)

#run through test 2 using the initial point, learning rate (alpha), and number of iterations
x0,y0=0,-1
alpha=0.01
num_iterations=10000
x_final,y_final= gradient_descent(x0,y0,fun_2,grad_f_2,alpha,num_iterations)
print("the coordinates of the final point after gradient descent is:",x_final, y_final)

#graphing code from greg
import numpy as np
from mpl_toolkits import mplot3d #for 3D plots
import matplotlib.pyplot as plt #usual matplotlib
%matplotlib widget
X=np.linspace(-5,5,100)
Y=np.linspace(-5,5,100)
x,y=np.meshgrid(X,Y)
z= 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
#x,y z are variable names.
