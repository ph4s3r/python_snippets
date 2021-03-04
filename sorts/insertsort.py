
 "This is just an insert sort, tested on Hackerrank`s https://www.hackerrank.com/challenges/big-sorting challenge"

def insertSort_swaps(a, n):
    
    for i in range(1, n):
            j = i
            while a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j] #SWAP
                #print("swapped", a[j], a[j-1], "at position i:", i)
                if j == 1:
                    break
                else:
                    j = j-1

    return a



def insertSort_shifts(a, n):
    
    for i in range(2, n):
        key = a[i]
        j = i - 1
        while j>=0 and a[j] > key:
            a[j+1] = a[j] #shifting elements right, to make a place for key
            j = j - 1
        if i != j+1:
            a[j+1] = key #after elements shifted, key is inserted.
        #If things are ordered, and the while loop does not run
        #i = j+1 so we inserting the element which is already there
    
    return a
    
    

def bigSorting(unsorted):
    
    n = len(unsorted)
    if n == 1:
        return unsorted
    a = []
    for num in unsorted:
        a.append(int(num))
    
    #Insertion sort, need to work for the first element as well
    
    if a[0] > a[1]:
        a[0], a[1] = a[1], a[0]
    
    if n == 2:
        return unsorted 
        
    a = insertSort(a, n)

    for i in range(n):
        a[i] = str(a[i])
    return a
