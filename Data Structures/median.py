# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 18:45:00 2017

@author: George
"""

a = [1,3,7,8]
half = (len(a)/2)

if len(a) == 1:
    print(float(a[0]))

if len(a) == 2:
    print((a[0] + a[1]) / 2)

if len(a) % 2 == 0:

   print (( a[int(half) - 1] + a[int(half)]) / 2)
   print (int(half) - 1)

else:
   
    print (a[int(half)])
   