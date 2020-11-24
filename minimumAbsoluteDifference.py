#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):

    arr.sort()
    soma = sys.maxsize 
    
    for i in range(len(arr)-1):
        aux = abs(arr[i] - arr[i+1])
        
        if aux < soma:
            soma = aux
    
    print("soma:", soma)
    return soma


if __name__ == '__main__':
   
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

