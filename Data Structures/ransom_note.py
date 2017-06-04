# -*- coding: utf-8 -*-
import collections
"""
Created on Sun Jun  4 21:44:07 2017

@author: George

https://www.hackerrank.com/challenges/ctci-ransom-note
"""

def ransom_note(magazine, ransom): 
#www.stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work
    mag_dict = collections.defaultdict(int)
    
    for word in magazine:
       mag_dict[word] += 1
    
    for word in ransom:
        mag_dict[word] -= 1
        if mag_dict[word] < 0: return False
        
    return True
        

   

m, n = 6, 4
magazine = "give me one grand today night hello abc".strip().split(' ')
ransom = "give one grand today abc".strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")
