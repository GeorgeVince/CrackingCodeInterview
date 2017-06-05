# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 17:19:33 2017

@author: George
"""

class MyQueue(object):
    
    def __init__(self):
        self.queue = []
    
    def peek(self):
        return self.queue[0]
          
    def pop(self):
        popped = self.queue[0]
        self.queue = self.queue[1:len(self.queue)]
        return popped
        
    def put(self, value):
        self.queue.insert(len(self.queue), value)
        

queue = MyQueue()
queue.put(42)
queue.pop()
queue.put(14)
queue.put(28)


print (queue.pop())
print (queue.peek())


"""
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
"""