
#Find Two Unique Numbers from Array in O(n) Time

#Nvidia interview question


"""

Let's assume all numbers except two occur twice in an array. How do you get those two numbers to occur only once? For example, only two numbers, 4 and 6, in the array {2, 4, 3, 6, 3, 2, 5, 5} occur once, and the other numbers occur twice. Therefore, the output should be 4 and 6.
This question was asked in the NVIDIA interview coding round.

Explanation:

Let’s solve this problem into two steps:

Find the unique number in the array,

when there is exactly one unique number
when there are exactly two unique numbers
See one by one.

Find the unique number in the array when there is exactly one unique number.
If there is a single unique element in the array, you can easily find the duplicates using the XOR operation.

Things you should understand to solve this problem.

XOR operation
Bitwise operation
You can learn bitwise operations in Python.

XOR is a logical operation that returns 0 if both numbers are the same. When you XORed a number with zero, it returns the same number.

Suppose we have the following array of the numbers [2, 4, 3, 3, 2, 5, 5] which has exactly one unique number (4).

Performing XOR operation:

= 2^4^3^3^2^5^5
= 2^2^3^3^5^5^4
=0^0^0^4
=4

"""


def findUnique(arr):
    out = 0
    for i in arr:
        out = i ^ out
    return out


def createSubArray(arr, num):
    num = (-1) * num
    arr1 = []
    arr2 = []
    for i in arr:
        if "{0:b}".format(i)[num] == "0":
            arr1.append(i)
        else:
            arr2.append(i)
    return arr1, arr2


def findFirstBit1FromLast(num):
    strNum = "{0:b}".format(num)
    for i in range(0, len(strNum)):
        if strNum[len(strNum) - 1 - i] == "1":
            return i + 1

if __name__ == '__main__':

    arr = [2, 4, 3, 6, 3, 2, 5, 5]
    temp = findUnique(arr)
    bitLoc = findFirstBit1FromLast(temp)
    arr1, arr2 = createSubArray(arr, bitLoc)
    print(findUnique(arr1))
    print(findUnique(arr2))


