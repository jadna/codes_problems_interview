#!/bin/python

import math
import os
import pdb

import random
import re
import sys



#
# Complete the 'acharMinimoDeDias' function below.
#
# The function is expected to return an INTEGER.
# The function accepts FLOAT_ARRAY duracoes as parameter.
#

def acharMinimoDeDias(duracoes):
    # Write your code here
    long = []
    quick = []
    for d in duracoes:
        if d > 1.99:
            long.append(d)
        else:
            quick.append(d)
    dias = len(long)
    maiores = []
    menores = []
    for q in quick:
        if q >= 1.5:
            maiores.append(q)
        else:
            menores.append(q)

    find = False
    for maior in maiores:
        for index, value in enumerate(menores):
            if maior + value <= 3:
                dias += 1
                find = True
                menores.pop(index)
                break
        if not find:
            dias += 1
        find = False
    i = 0
    j = 0
    while(j < len(menores)):
        if i >= 3:
            i = 0
        if i > 3.0:
            j = j - 1
        i += menores[j]
        if i >= 3.0:
            dias += 1
        j += 1
    if i > 0:
        dias += 1

    return dias
        # #print("i: ", i)
        # if i+1 < len(duracoes) and (duracoes[i] +  duracoes[i+1]) <= 3.0:
        #     dias += 1
        #     i = i+2
        #     '''print(i)
        #     print("Dias: ",dias)'''

        # else:
        #     if duracoes[i] <= 3.0:
        #         dias += 1
        #         i = i+1
        #     else:
        #         print(i)
        #         #print("Dias1: ",dias)

    #return dias
      

if __name__ == '__main__':

    duracoes = []
    # duracoes = [1.01,1.01,1.01,1.4,2.4]
    # duracoes = [1.01,1.991,1.32,1.4]
    # duracoes = [1.90, 1.04, 1.25, 2.5, 1.75]
    # duracoes = [2.02,2.95,1.14,2.13,1.86,1.45,1.5,2.77,1.55,1.49,1.2,2.89,2,1.75,2.56,2.05,2.19,1.11,1.81,2.45,1.37,2.67,1.63,1.89,1.76,2.05,2.98,2.53,2.15,1.21,2.43,2.21,2.15,2.85,1.28,2.17,1.52,1.33,2.14,2.93,1.39,2.83,1.19,1.21,1.09,1.77,2.93,2.53,1.4,2.49,2.81,2.05,2.48,2.47,1.95,1.41,2.12,2.45,1.68,1.57,1.66,1.69,1.68,2.93,1.27,1.77,2.97,1.89,2.15,1.37,1.35,2.05,1.12,1.37,2.89,2.05,1.11,2.23,2.6,1.33,1.42,1.31,1.89,2.33,1.94,1.47,2.29,2.61,2.92,2.45,1.89,1.49,2.34,2.63,1.82,2.53,1.59,2.03,1.92,1.65,2.17,2.67,1.43,1.17,1.61,2.51,2.48,2.25,1.56,2.39,2.12,2.61,2.76,1.93,1.71,2.57,2.77,2.47,2.36,2.05,1.5,1.25,1.98,1.41,1.46,1.63,2.67,1.57,2.25,1.31,1.41,2.45,1.47,2.93,1.46,1.73,1.82,2.07,1.86,1.05,2.29,1.35,1.98,1.97,2.4,1.53,2.65,2.29,1.12,1.35,1.45,2.77,2.61,2.63,1.96,2.25,2.14,1.87,1.94,2.93,2.88,2.19,2.02,2.53,1.38,1.27,2.11,1.49,2.2,1.83,1.32,2.25,1.65,2.37,2.57,2.29,2.29,1.09,2.99,1.01,1.73,1.89,2.47,1.09,2.69,2.71,2.73,1.69,1.31,1.23,2.36,2.29,1.1,1.99,1.44,2.89,1.32,1.93,1.72,1.17]
    duracoes = [1.01, 1.01, 1.01, 1.4, 2.4]

    result = acharMinimoDeDias(duracoes)
    print(result)

    

    