# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 23:10:10 2021

@author: HP
"""

n = 9735
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)