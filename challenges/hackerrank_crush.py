#!/bin/python3

"""

https://www.hackerrank.com/challenges/crush

"""


def arrayManipulation(n, queries):

    arr = [0] * n

    for a, b, k in queries:
        for j in range(a-1, b):
            arr[j] += k

    return max(arr)


if __name__ == '__main__':

    numzeros = 4000

    numqueries = 30000

    querylist = []
    # querylist = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
    # querylist = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

    fptr = open("arrayman_input04.txt", 'r')

    for _ in range(numqueries):
        querylist.append(list(map(int, fptr.readline().rstrip().split())))

    result = arrayManipulation(numzeros, querylist)

    print(result)

    fptr.close()