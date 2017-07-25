# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 19:47:38 2017

@author: georg
"""
import math

def factorial(num):
    if num == 0:
        return 1
    else: 
        return num * factorial(num - 1)
    
def poisson(k, _lambda):
    return (_lambda**k) * (math.exp(1)**(-_lambda)) / factorial(k)

print (round(poisson(5,2.5),3))
