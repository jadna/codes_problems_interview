import math
import os
import random
import re
import sys
from collections import defaultdict

#!/bin/python3
# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    socks = defaultdict(int)
    pairs = 0
    ar.sort()
    for i in ar:
        print("i:{}".format(i))
        socks[i] += 1
    
    print("socks:{}".format(socks))
         
    for qnt in socks.values():

        pairs += qnt // 2
        print(qnt // 2)
        print("ele:{}".format(qnt))
        print("pairs:{}".format(pairs))
      
    return pairs

    
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #
    # fptr.close()
