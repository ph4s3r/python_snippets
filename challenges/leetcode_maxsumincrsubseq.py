
"""
My solution to the Max Sum Increasing Subsequence problem

https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

https://leetcode.com/problems/maximum-subarray/

"""


def enrich(arr, subarr):

    minn = subarr[0]
    subarr = subarr[::-1]
    starting_index = arr.index(minn)
    for i in reversed(range(starting_index)):
        if arr[i] < minn:
            subarr.append(arr[i])
            minn = arr[i]

    return subarr[::-1]

def createSubArray(arr):

    local_subarray = []
    local_subarray.append(arr[0])
    jumps = 0

    for i in range (1, len(arr)):
        if arr[i] >= arr[i-1-jumps]:
            local_subarray.append(arr[i])
            jumps = 0
        else:
            jumps += 1

    return local_subarray


if __name__ == '__main__':

    #arr = [10, 70, 20, 30, 50, 11, 30]
    arr = [10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]
    #arr = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #arr = [8, 12, 2, 3, 15, 5, 7]

    arrays = []
    jumps = 0
    result = []

    arrays.append(createSubArray(arr))
    print("new array added:", arrays[-1])

    #create as many subarrays as many breaks in incremental sequences
    for i in range (1, len(arr)):
        if arr[i] >= arr[i - 1 - jumps]:
            jumps = 0
        else:
            arrays.append(createSubArray(arr[i:]))
            print("new array added:", arrays[-1])
            jumps = len(arrays[-1])

    # trace back if there is a smaller element missed (...)
    for idy, array in enumerate(arrays):
        arrays[idy] = enrich(arr, array)

    # gen lengths
    for array in arrays:
        result.append((sum(array), array))

    # add to the data struct and find the longest
    longest = 0
    longest_idx = 0
    for idx, res  in enumerate(result):
        if res[0] > longest:
            longest = res[0]
            longest_idx = idx

    print(result[longest_idx])
