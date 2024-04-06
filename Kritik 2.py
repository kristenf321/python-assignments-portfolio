import math
import numpy as np
def roots(f,a,b):
    if f(a)*f(b) >= 0:
        #f(a) cannot equal the sign of f(b)
        print ("Not looking for roots in interval where f(b) and f(a) are same signs")
    else:
        a=a
        b=b
        while abs(b-a)>=0.0000000001:
            M=(a+b)/2
            if f(b)*f(M)<0:
                a=M
            else:
                b=M
        return round ((a+b)/2,10)

f=lambda x: math.exp(x) + np.log(x)
approximate_roots= roots(f,0,1)
print(approximate_roots)

f=lambda x:math.atan(x)-x**2
approximate_roots=roots(f,0,2)
print(approximate_roots)