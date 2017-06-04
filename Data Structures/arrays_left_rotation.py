# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 17:55:22 2017

@author: George

https://www.hackerrank.com/challenges/ctci-array-left-rotation

"""

def array_left_rotation(a, n, k):
    
    
  alist = list(a)
  b = alist[k:]+alist[:k]
  return b
        

#n, k = map(int, input().strip().split(' '))
#a = list(map(int, input().strip().split(' ')))

n = 5
k = 4
a = [1, 2, 3, 4, 5]

answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

