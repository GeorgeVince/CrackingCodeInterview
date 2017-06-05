# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:09:47 2017

@author: George
"""

class Stack:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push (self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)