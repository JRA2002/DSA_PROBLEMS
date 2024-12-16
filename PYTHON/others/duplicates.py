'''Given an array of n elements that contains elements from 0 to n-1, 
with any of these numbers appearing any number of times. Find these 
repeating numbers in O(n) and use only constant memory space.'''

def duplicates(arr, n):
    dict1 = {}
    for i in range(n):
        if arr[i] not in dict1:
            dict1[arr[i]] = 1
        else:
            print(arr[i], sep=' ')
    

arr = [1, 2, 3, 6, 3, 6, 1]
n = len(arr)
duplicates(arr, n)