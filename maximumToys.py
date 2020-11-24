#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    tol =0

    prices.sort()
    for i in prices:
        if i <= k:
            k -= i
            tol += 1
                
    print("tol:", tol)

    return tol

if __name__ == '__main__':
    
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
