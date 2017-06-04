# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:54:25 2017


https://www.hackerrank.com/challenges/ctci-making-anagrams

@author: George
"""

def number_needed(a, b):
    
    tally = [0] * 26
    
    for letter in a:
        index = (ord(letter) - ord('a'))
        tally[index] += 1

    
    for letter in b:
        index = (ord(letter) -  ord('a'))
        tally[index] -= 1
    
    result = 0
    for x in range(0, len(tally)):
        pass
        result += abs(tally[x])
        
    return result

#a = input().strip()
#b = input().strip()

a = "abc"
b = "abcde"

print(number_needed(a, b))
