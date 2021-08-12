# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:14:11 2021

@author: HP
"""


n = int(input("Enter a number of n: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,"",end="")
    print()
        