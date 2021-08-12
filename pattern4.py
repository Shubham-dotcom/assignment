# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:34:10 2021

@author: HP
"""

n = int(input("Enter a number of n: "))
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1):
        print("* ",end="")
    print()
for i in range(n-1):
    print(" "*(i+1),end="")
    for j in range(n-i-1):
        print("* ",end="")
    print()