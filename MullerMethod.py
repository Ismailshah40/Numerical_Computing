# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:34:24 2020

@author: bilal
"""

import math; 
import numpy as np
MAX_ITERATIONS = 10000; 
  
# Function to calculate f(x) 
def f(x): 
   return np.cos(x)-1.3*x; 
  
a = 0; 
b = 1; 
c = 2; 
res = 0; 
i = 0; 
while (True): 
      d1 = f(a) - f(c);  
      d2 = f(b) - f(c); 
      h1 = a - c;  
      h2 = b - c; 
      a0 = f(c); 
      a1 = (((d2 * pow(h1, 2)) - (d1 * pow(h2, 2))) /((h1 * h2) * (h1 - h2))); 
      a2 = (((d1 * h2) - (d2 * h1)) / ((h1 * h2) * (h1 - h2))); 
      x = ((-2 * a0) / (a1 + abs(math.sqrt(a1 ** 2 - 4 * a0 * a2)))); 
      y = ((-2 * a0) / (a1 - abs(math.sqrt(a1 ** 2 - 4 * a0 * a2)))); 
  
        # Taking the root which is  
        # closer to x2 
      if (x >= y): 
         res = x + c; 
      else: 
         res = y + c; 
         m = res * 100; 
         n = c * 100; 
         m = math.floor(m); 
         n = math.floor(n); 
         if (m == n): 
            break; 
         a = b; 
         b = c; 
         c = res; 
         if (i > MAX_ITERATIONS): 
            print("Root cannot be found using"); 
            break; 
         i += 1;      
         if (i <= MAX_ITERATIONS): 
             print("The value of the root is", res); 
         print('iteration',i)
  
# Driver Code 


