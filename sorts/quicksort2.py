# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def quicksort(a):

    #find a pivot element - let it be the first in the array

    pivot = a.pop(0)

    #start the left and right pointers at left and right

    n = len(a)
    l = 0
    r = n - 1

    #Search for the first smaller element than pivot from the right (we want to move smaller elements from the right to left, right?
    #And the greatest element from the left


    while l < r:
        while r >= 0 and a[r] > pivot:
            if r == 0:
                print("the pivot", pivot, " is already the smallest element")
                a.insert(0, pivot)
                return 0
            r -= 1

        while l < n and a[l] < pivot:
            if l == n - 1:
                print("the pivot", pivot, " is already the greatest element")
                a.append(pivot)
                return 0
            l += 1

        #Then exchange them, the pythonic way

        print("swapped", a[r], a[l])
        a[r], a[l] = a[l], a[r]
        l += 1
        r -= 1

        #At the end of cycle, insert pivot back into the list (0th elem) and swap with the left pointer value (a small element)
        a.insert(0, pivot)
        a[0], a[l] = a[l], a[0]


    return a


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    arr2 = [45, 23, 87, 12, 72, 4, 54, 32, 52]
    arr = [random.randint(1, 100) for x in range(10)]
    print(arr2)
    print(quicksort(arr2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
