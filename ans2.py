# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:47:10 2021

@author: HP
"""

def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)
    return si
      
simple_interest(8, 6, 8)