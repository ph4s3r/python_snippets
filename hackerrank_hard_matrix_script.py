
#https://www.hackerrank.com/challenges/matrix-script


#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

    
# My code starts right from here
d = ""

#read the input into the output-conform string
for i in range(m):
    for j in range(n):
        d += matrix[j][i]

nc = ("!","@","#","$","%","&")
o = d
l = 0 # chars to temporarily trim from beginning
r = 0 # chars to temporarily trim from end
#print("original matrix:", d)
m = len(d)

#listize the matrix string to charray
d = list(d)

# trim trailing non-alphanimerics
while not str.isalnum(d[-1]):
    d.pop(-1)
    r += 1

# trim leading non-alphanimerics
while not str.isalnum(d[0]):
    d.pop(0)
    l += 1

#convert back the list to string
d = ''.join([str(elem) for elem in d]) 

#print("trimmed matrix:", d)
#print("chars trimmed from beginning / end:", l, r)

# replace all non alphanumerics to a single space
for nachar in nc:
    d = d.replace(nachar, " ")

#convert multiple spaces to single - just run a few times to make sure (in lack of better idea)
for i in range(len(d)):
    d = d.replace("  ", " ")
    
#put back leading and trailing characters that were removed
d = o[0:l] + d + o[-r:len(o)]

print(d)

