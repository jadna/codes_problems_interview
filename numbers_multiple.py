import math
import os
import random
import re
import sys



def numbers_multiple(n):

    for x in range(1, n+1):

        if(x%3 == 0 and x%7 == 0):
            print("JeffBezos")
        elif(x%3 == 0):
            print("Jeff")
        elif(x%7 == 0):
            print("Bezos")
            #print("Bezos", x)
        else:
            print(x)


if __name__ == '__main__':
    
    n = int(input().strip())

    numbers_multiple(n)