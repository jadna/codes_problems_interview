#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the rotLeft function below.
def rotLeft(a, d):

    aux = a[d:] + a[:d]
    print(aux)

    return aux

if __name__ == '__main__':
    
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)
