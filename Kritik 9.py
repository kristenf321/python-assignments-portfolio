import sympy as sp
#gregs code
x, y = sp.symbols('x y')

# Define a function
f = sp.exp(x)*sp.sin(y) + y**3
# Differentiate f with respect to x
df_dx = sp.diff(f, x)
# Differentiate f with respect to y
df_dy = sp.diff(f, y)

#print statement
print ("The first partial derivative with respect to x is", (df_dx))
print ("The first partial derivative with respect to y is", (df_dy))


#b)
#from greg
x, y = sp.symbols('x y')

# Define a function
f= (x**2)*y + x*(y**2)
# Differentiate f with respect to x
df_dx = sp.diff(f, x)
# Differentiate f with respect to y
df_dy = sp.diff(f, y)


#create functions for partial of x and partial of y gradient
x=1
y=-1
def grad_fx_at_point(x,y):
    return 2*x*y +y**2

def grad_fy_at_point(x,y):
    return x**2 + 2*x*y
print ("The gradiant at point (1,-1) is:", (grad_fx_at_point(x,y), grad_fy_at_point(x,y)))

#magnitude of gradient taken by adding, squaring, and square rooting
def magnitude(grad_fx_at_point, grad_fy_at_point):
    return sp.sqrt((grad_fx_at_point)**2 + (grad_fy_at_point)**2)
print ("The magnitude of the gradient at point (1,-1) is:", (magnitude(x,y)))

#c) 

x, y = sp.symbols('x y')

# Define the function
f = sp.log(x**2+y**2)
# Differentiate f with respect to x
df_dx = sp.diff(f, x)
# Differentiate f with respect to y
df_dy = sp.diff(f, y)

#differentiate the first partial derivative of x with respect to x
d2f_dx2 = sp.diff(df_dx, x)
# Differentiate the first partial derivative of y with respect to y
d2f_dy2 = sp.diff(df_dy, y)
#differentiate the first partial derivative of y with respect to x
d2f_dxdy= sp.diff(df_dy, x)

print ("The second partial derivative with respect to x is", (d2f_dx2))
print ("The second partial derivative with respect to y is", (d2f_dy2))
print ("The mixed partial derivative with respect to x is", (d2f_dxdy))


#d)
#Import the necessary libraries:
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

'''#Define the function using SymPy:
x, y = sp.symbols('x y')
j = x**3 - 3*x*y + y**3

#Convert the SymPy expression to a numerical function:
j_func = sp.lambdify((x, y), j, 'numpy')

#Create a grid of x and y values and evaluate j on this grid:
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)

#Plot the contour:
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()'''


#e)
#Import the necessary libraries:
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Define the function using SymPy:
x, y = sp.symbols('x y')
j = sp.exp(x+y) +x*y**2

#Convert the SymPy expression to a numerical function:
j_func = sp.lambdify((x, y), j, 'numpy')

#Create a grid of x and y values and evaluate j on this grid:
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x_vals, y_vals)
Z = j_func(X, Y)

#Plot the contour:
plt.contourf(X, Y, Z, levels=50, cmap='viridis')
plt.colorbar()
plt.title('Contour plot of $j(x, y) = e^(x+y) + xy^2$')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.show()


