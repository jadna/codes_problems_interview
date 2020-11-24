#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    
    jumps = 0
    n = len(c)
    i = 0

    while i < n-1:

        if(i+2 < n and c[i+2] == 0):
            i = i+2
            jumps += 1
        else:
            i = i+1
            jumps += 1
        
    print(jumps)
    return jumps

    
if __name__ == '__main__':
   
    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
