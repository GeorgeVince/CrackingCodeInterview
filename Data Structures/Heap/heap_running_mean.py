# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:14:42 2017

@author: George
"""

#!/bin/python3

import sys
import heapq

class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def __getitem__(self,i): return self.h[i].val
  
class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)
    
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
    
upper = MinHeap()
lower = MaxHeap()
n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)
   addItem(a_t)
   print(median())