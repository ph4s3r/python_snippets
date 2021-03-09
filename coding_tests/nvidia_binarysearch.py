https://www.hackerrank.com/codepair/gnciwpxoazbupacxyndmhvofpeqvymyc/questions/1?b=eyJpbnRlcnZpZXdfaWQiOjE3NjE5NDcsInJvbGUiOiJpbnRlcnZpZXdlciIsInNob3J0X3VybCI6Imh0dHBzOi8vaHIuZ3MvODI3YWZhIiwiY2FuZGlkYXRlX3VybCI6Imh0dHBzOi8vaHIuZ3MvMDZiZTYzIn0%3D

curl https://hr.gs/827afa -v

"""
Binarysearch
# Test array 
#arr = [ 2, 3, 4, 10, 40 ]
#x = 10
# Returns index of x in arr if present, else -1
"""


def search(arr, x):
    
    l = len(arr)
    l2 = l//2
    arr = tuple(arr)
    #print("searching in arr:", arr)
    if arr[l2] == x:
        return 1
    elif l2 == 0:
        return -1
    elif x > l2:
        if search(arr[l2:], x) == 1:
            return 1
        else:
            return -1
    elif x < l2:
        if search(arr[:l2], x) == 1:
            return 1
        else:
            return -1

if __name__ == "__main__" :
    
    arr = [ 2, 3, 4, 10, 40 ]
    x = 11
    if search(arr, x) == 1:
        print(arr.index(x))
    else:
        print(-1)

