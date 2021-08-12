# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:34:59 2021

@author: HP
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1)+"* ",end="")
    if i>=1:
        print(" "*(2*i-1)+"* ",end="")
    print()