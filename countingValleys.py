#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    
    num_valleys, curr_level = 0, 0
    for step in path:
        
        if curr_level == 0 and step == 'D':
            print("Entrou aqui")
            num_valleys += 1
        if step == 'U':
            curr_level += 1
        else:
            curr_level -= 1
        
        print("step: {}".format(step))
        print("curr_level: {}".format(curr_level))
        print("num_valleys: {}".format(num_valleys))

    return num_valleys
    
if __name__ == '__main__':

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)
    print(result)

    
