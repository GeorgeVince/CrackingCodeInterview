# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:13:21 2017

@author: George
"""

def is_matched(expression):
    stack = []
    pairs = {'(':')', '[':']','{':'}'}
    
    for x in expression:
        if pairs.get(x):
            stack.append(pairs[x])
        else:
            if len(stack) == 0 or x != stack[len(stack) - 1]:
                return False
            stack.pop()
        
    return len(stack) == 0
            
expression = "{[]}{{}}"
print (is_matched(expression))