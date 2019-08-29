#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):  
    max_val = 0
    summed_glass = []
    print(arr)

    for i in range(2, len(arr)):
        for j in range(2, len(arr[0])):
            hour_glass = [
                arr[i-2][j-2],arr[i-2][j-1],arr[i-2][j],
                arr[i-1][j-1],
                arr[i][j-2],arr[i][j-1],arr[i][j],
            ]
            
            summed_glass.append(sum(hour_glass))

        
    return(max(summed_glass))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
