import matplotlib.pyplot as plt
import numpy as np 


def gradient_descent (f, learning_rate, initial_point): 
    def deriv(f,base_point): #estimate the derivative of the function f at base_point 
        return (f(base_point+10**(-5))-f(base_point-10**(-5)))/(2*(10**(-5)))
    x_coords= [initial_point] #store the x_n's
    y_coords=[f(initial_point)] #store the y_n's


    for i in range (200):
       point=deriv(f,x_coords[-1])
       x_coords.append((-learning_rate *point )+x_coords[-1])
       y_coords.append(f(x_coords[-1]))
    

    plot_range=np.linspace(min(x_coords)-0.5, max(x_coords)+0.5,1000)
    function_range=[f(i) for i in plot_range]
    
    plt.plot(plot_range, function_range, label ='f(x)=x^2')
    plt.plot(x_coords, y_coords, 'o-', label = 'The gradient descent path')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show

    return round (x_coords[-1],3),round(y_coords[-1], 3) #from instructions 
   
min_point= gradient_descent(lambda x: x**2, 0.1,2)
print("min point:", min_point)