# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:57:07 2019

@author: bilal
"""

division = 34
todivi = 21
ans = division % todivi
while ans:
    division = todivi
    todivi = ans
    ans = division % todivi

print("Your gcd is ", todivi)
    