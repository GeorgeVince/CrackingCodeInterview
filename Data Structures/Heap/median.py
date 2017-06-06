# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:58:27 2017

@author: George
"""

from heap import MinHeap
from heap import MaxHeap


upper = MinHeap()
lower = MaxHeap()
     
def addItem(item):
    target = lower if len(lower) <= len(upper) else upper
    target.heappush(item)
    balanceLists()
        
def balanceLists():
    if len(lower) > 0 and len(upper) > 0:
        if lower[0] > upper[0]:
            lowerHead = lower.heappop()
            upperHead = upper.heappop()          
            lower.heappush(upperHead)
            upper.heappush(lowerHead)
            
def median():
    if (len(upper) + len(lower)) % 2 != 0:
        return float(lower[0])
    else:
        return float((upper[0] + lower[0]) / 2)
        
    
def printHeaps():
    print ("lower")
    print ("HEAD: " ,lower[0])
    for i, n in enumerate(lower):
        print (n)
    
    print("upper") 
    print ("HEAD: " ,upper[0])   
    for i, n in enumerate(upper):
        print (n)
        
addItem(1)
addItem(7)
addItem(8)

printHeaps()