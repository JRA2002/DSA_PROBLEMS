'''Given an array arr of only 0's and 1's. The array is sorted in 
such a manner that all the 1's are placed first and then they are 
followed by all the 0's. Find the count of all the 0's.'''

def count_zeros(arr):
    if arr[0] == 0:
        return len(arr)
    i = 0
    j = len(arr) - 1
    
    while i <= j:
        midd = (i+j)//2
        if arr[midd] == 1:
            if arr[midd+1] == 1:
                i = midd + 1
            else:
                return j - (midd+1) + 1
        else:
            j = midd - 1
    return 0

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
res = count_zeros(arr)
print(res)