

"This is just a merge sort, tested on Hackerrank`s https://www.hackerrank.com/challenges/big-sorting challenge"


def split(a):
    
    if len(a) < 2:
        return a
    
    mid =len(a) // 2
    
    #split: splitting the array to two halves if there is more than 1 item in the array
    #split returns a sorted array by running a merge on two halves
    #merge: putting together two halves into one with sorting 
    
    return merge(
        left=split(a[:mid]),
        right=split(a[mid:])
    )
    
def merge(left, right):
    
    result = []
    for i in range(0,len(left)+len(right)):
        if len(left) == 0:
            result.append(right.pop(0))
        elif len(right) == 0 or left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    return result
