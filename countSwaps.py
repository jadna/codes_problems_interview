#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):

    count = 0
    n = len(a)

    for i in range(len(a)):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
                count += 1

    print("Array is sorted in {} swaps.".format(count))
    print("First Element: {}".format(a[0]))
    print("First Element: {}".format(a[-1]))


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
