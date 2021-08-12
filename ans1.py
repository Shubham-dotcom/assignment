# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:35:23 2021

@author: HP
"""

credits = int(input("Enter the credits: "))

if credits >=7500:
    print("Tera Leader")
    
    if credits >=6000 and credits <7500:
        print("Gega Leader")
        
        if credits >=4500 and credits <6000:
            print("Mega Leader")
            
        else:
            print("Rising Star")
    


