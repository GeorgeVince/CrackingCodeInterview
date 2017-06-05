# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:31:53 2017

@author: George
"""


class Node():
    
    def __init__(self, node_value):
        self.data = node_value
        self.next = None
      
    def getData(self):
        return self.data
        
    def getNext(self):
        return self.next
    
    def setData(self, data):
        self.data = data
    
    def setNext(self, node):
        self.next = node
        
        