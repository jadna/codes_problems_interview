#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    imp_const = []
    luck = 0
    
    for i in contests:
        print("contests:", contests)
        if i[1] == 1:
            print(i[1])
            print(i[0])
            imp_const.append(i[0])
            print("imp_const:", imp_const)
        else:
            luck += i[0]
            print("luck", luck)
            
    imp_const.sort(reverse=True)
    print("imp_const:", imp_const)

    luck += sum(imp_const[:min(k, len(imp_const))])

    # winning the remaining contests
    luck -= sum(imp_const[k:])

    print(luck)
    return luck

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

