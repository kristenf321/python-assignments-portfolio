import numpy as np
import math

def f(x):
    return np.exp(x)
c=0
E=0.01
d=0.00001
x1=c
x2=c
deltax=10**(-2)

def fprime(x,deltax,f):
    return (f(x+deltax)-f(x-deltax))/2*deltax

def Lapprox(x,c,deltax,f):
    return f(c)+fprime(c,deltax,f)*(x-c)


   
#Determining distinct value for x1
for i in range(0,100):
    x1=x1-d
    if abs(f(x1)-Lapprox(x1,c,deltax,f)) <= E:
        ansx1=x1
    else:
        ansx1= "Value for x1 cannot be found within a reasonable range"

#Determining distinct value for x2
for i in range(0,100):
    x2=x2+d
    if abs(f(x2)-Lapprox(x2,c,deltax,f)) <= E:
        ansx2= x2
    else:
        ansx2= "Value for x2 cannot be found within a reasonable range"

Y=round(ansx1,3)
M=round(ansx2,3)
print(Y,M)
print("x1 and x2")