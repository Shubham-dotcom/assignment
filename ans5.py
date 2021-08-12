# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:08:20 2021

@author: HP
"""

def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
 

n = 345289467
print("Number of digits : % d" % (countDigit(n)))