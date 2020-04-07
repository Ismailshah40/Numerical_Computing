# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:55:43 2020

@author: bilal
"""
'''Newton Raphson'''
'''
import numpy as np
from scipy.misc import derivative
def f(x):
    return np.cos(x) - 1.3 * x

x = 2
h = 0.0001
iteration = 0
while abs(h) >= 0.0001:
    h= f(x)/derivative(f,x)
    x = x-h
    iteration = iteration+1
print("No. of iteration",iteration)
print("The root is",x)
'''
#import numpy as np
#from scipy.misc import derivative
#def f(x):
#    return 2*x*np.cos(2*x) - (x+1)*2
#
#x = 1
#h = 0.0001
#iteration = 0
#while abs(h) >= 0.0001:
#    h= f(x)/derivative(f,x)
#    x = x-h
#    iteration = iteration+1
#print("No. of iteration",iteration)
#print("The root is",x)



#import numpy as np
#x1 = -2
#x2 = 4
#E = 0.0001
#def f(x):
#    f = 2*x*np.cos(2*x)-(x+1) * 2
#    return f
#iteration = 0; xm = 0; x0 = 0; c = 0;
#if (f(x1)*f(x2) < 0):
#    while abs(E) >= 0.0001:
#        x0= ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1)));  
#        c = f(x1) * f(x0);
#    
#        x1 = x2;  
#        x2 = x0; 
#        iteration = iteration + 1
#        
#        xm = ((x1 * f(x2) - x2 * f(x1)) / (f(x2) - f(x1))); 
#              
#        if(abs(xm - x0) < E): 
#                break; 
#else: 
#    print("not find root");  
#print("Root of the given equation =", x0);  
#print("No. of iterations = ", iteration); 
#
#    
import math
a = math.sqrt(2)
print(a)














