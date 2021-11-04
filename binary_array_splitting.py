
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

