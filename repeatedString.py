#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    count_a = 0
    result = 0
        
    for i in s:
        if i == "a":
            count_a += 1
    
    print(count_a)
    a = (n//len(s))
    b = n%len(s)

    if b == 0:
        result = count_a * a
    else:
        aux = 0
        for i in range(b):
            if s[i] == "a":
                aux += 1

        result = count_a*a + aux
        
    return result



if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

