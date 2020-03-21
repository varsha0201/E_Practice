#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:08:22 2020

@author: varsha
"""

num = int(input("Number:"))
factorial = 1

if num < 0:
    print("Must be positive")
elif num == 0:
    print("Factorial ==1")
else:
    for i in range(1, num+1):
        factorial = factorial * i
        
print(factorial)

