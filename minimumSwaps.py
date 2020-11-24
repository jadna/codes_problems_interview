#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):

    count = 0

    for i in range(len(arr)-1):
        for j in range(i, len(arr)):

            print("i: {}, j: {}".format(i, j))
            print("arr[i]: {}, arr[j]: {}".format(arr[i], arr[j]))

            if arr[i] > arr[j]:
                count += 1
    print(count)
    return count
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)
