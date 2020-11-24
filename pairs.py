#!/bin/python3

import math
import os
import random
import re
import sys

def pairs(k, arr):

    print("target:", k)
  
    answer = 0
    array = ()

    for v in arr:
        print("v:", v)
        if k/v in arr and k%v == 0:
            array = ()
            print(k/v)
            print(k%v)
            answer += 1
            array = (v, k/v)            
    
    print(array)
    return answer

if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)
