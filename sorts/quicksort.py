"""

The below exercise was written based on the book:

'Dr. Basant Agarwal_ Benjamin Baka - Hands-On Data Structures and Algorithms with Python_ ...
... Write complex and powerful code using the latest features of Python 3.7, 2nd Edition-Packt Publishing (2018)'


The code still does not work properly, just became more and more complicated...

"""

import random

def quicksort(a):

    # find a pivot element - let it be the first in the array
    print("\n\na quicksort function was called on", a)
    if len(a) == 1:
        print("returned a 1-element array")
        return a
    elif len(a) == 2:
        if a[0] > a[1]:
            a[0], a[1] = a[1], a[0]
        print("returned a 2-element sorted array")
        return a
    pivot = a.pop(0)
    print("pivot", pivot, "removed from array", a)

    # start the left and right pointers at left and right

    n = len(a)
    l = 0
    r = n - 1

    # Search for the first smaller element than pivot from the right
    # (we want to move smaller elements from the right to left, right?
    # And the greatest element from the left

    while l < r:
        while r >= 0 and a[r] > pivot:
            if r == 0:
                print("the pivot", pivot, "is already the smallest elem, calling quicksort on array without pivot")
                a = quicksort(a)
                a.insert(0, pivot)
                print("returned a with the pivot added back:", a)
                return a
            r -= 1

        while l < n and a[l] < pivot:
            if l == n - 1:
                print("the pivot", pivot, "is already the greatest elem, calling quicksort on array without pivot")
                a = quicksort(a)
                a.append(pivot)
                print("returned a with the pivot added back:", a)
                return a
            l += 1

        # Then exchange them, the pythonic way

        print("swapped", a[r], a[l], "where l and r are", l, r)
        a[r], a[l] = a[l], a[r]
        l += 1
        r -= 1
        print(a)

        # At the end of cycle, insert pivot back into the list (0th elem)
        # and swap with the left pointer value (a small element)

    print("putting the swapped element at the left pointer to position 0")
    a.insert(0, a.pop(l-1))
    # print("at this point elems of the a left from  pivot are smaller, thus to the right everything should be bigger")
    print(a)

    # Calling quicksort for a[:pivot] and a[pivot+1:]
    # But if there is only 1 element in a, then return a

    pivot_list = [pivot]
    return quicksort(a[:l]) + pivot_list + quicksort(a[l:])


if __name__ == '__main__':

    # arr2 = [45, 23, 87, 12, 72, 4, 54, 32, 52]
    arr = [random.randint(1, 100) for x in range(10)]

    print("the result of quicksort is:", quicksort(arr))

    # a = [random.randint(1, 10000) for i in range(15)]
    # myrand = a[random.randint(0, len(a)-1)]
    # print("a:", a, "picking a random element:", myrand, "that is the %d-th element in the array", a.index(myrand))



