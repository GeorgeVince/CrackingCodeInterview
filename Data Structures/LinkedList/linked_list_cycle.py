# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 09:15:09 2017

@author: George
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
"""

from linked_list import LinkedList

myList = LinkedList()

myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)
myList.add(5)

myList.makeCircle()
print (myList.has_cycle())
