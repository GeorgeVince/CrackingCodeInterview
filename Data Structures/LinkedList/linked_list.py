# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:33:40 2017

@author: George

Simple Linked List

"""
from node import Node

class LinkedList():
    
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def makeCircle(self):
        lastNode = self.head
        while lastNode.getNext() != None:
                lastNode = lastNode.getNext()
        
        lastNode.setNext(self.head) 
    
    def has_cycle(self):
        slow = self.head
        fast = self.head
        
        while (fast != None and fast.getNext() != None):
            slow = slow.getNext()
            fast = fast.getNext().getNext()
            
            if (slow == fast):
                return True
            
        return False
    

    
    def __str__( self ):
        s=""
        current = self.head
        
        while current != None:
            if current.getData() != None:
                s += str(current.getData())
                s += ", "
                print (s)
            
            current = current.getNext()
        
        return s[:-2]