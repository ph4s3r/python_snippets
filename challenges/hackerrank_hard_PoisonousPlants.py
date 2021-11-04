#!/bin/python3

"""

https://www.hackerrank.com/challenges/poisonous-plants

"""


import math
import os
import random
import re
import sys

# Complete the poisonousPlants function below.
def poisonousPlants(p):
    
    day = 0
    plantdied = True    # using a flag to signify if any plant died, 
                        # starting with True just to start the loop 
    
    while plantdied and len(p) > 1:
        plantdied = False
        for i in reversed(range(1, len(p))):
            if p[i] > p[i-1]:
                # print("plant with pesticide level", p[i], "died")
                p.pop(i)
                plantdied = True
                # print("plants look like this:", p)
        if plantdied:
            day += 1
        # print("day++")

    return day
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
