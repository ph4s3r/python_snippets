
"""

Coderbyte - Array addition II - this was an actual interview challenge sent to me by TwoSigma/Citadel HR

"""


from itertools import combinations
import time

def mycomb(arr, n):
    #Let`s return all the possible combinations of numbers stored in an array
    #comb array will store the n-long subsets of the array, i.e. n=2: ((1,2), (1,3), (2,3))
    #comb = []
    #l = len(arr)
    #for i in range(l):
    #    j = i+1
    #    for j in range(l):
    comb = combinations(arr, n)

    # Print the obtained combinations
    for i in list(comb):
        print(i)

def ori_combinations(arr, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(arr)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def perm(a):
    a = sorted(a, reverse=True)
    print(a)
    t = a[0]
    print(t)
    a = a[1:len(arr)]

    for j in range(2, len(a)):
        c = combinations(a, j)
        for i in list(c):
            if sum(i) == t:
                print("t, current set and the sum of the set:", t, i, sum(i))
                return True
    return False


if __name__ == '__main__':

    start_time = time.time()
    #arr = [10, 23, 6, 4, 261, 3, 1, -4, 55, 197, 590, 89, 63, 52, 20]
    arr = [1,2,3,4,5,6]
    #print(perm(arr))
    for value in ori_combinations(arr, 4):
        print(value)
    print("--- %s msec ---" % ((time.time() - start_time)*1000))

