# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:49:16 2021

@author: HP
"""

def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
  

print("The gcd is : ", end="")
print(hcf(a, b))