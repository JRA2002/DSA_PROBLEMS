'''Given an array arr[] of size N-1 with integers in the 
range of [1, N], the task is to find the missing number from the first N integers.'''

def missing_integer(arr, n):
    for i in range(1, n + 1):
        if i not in arr:
            return i
    return 0

arr = [2,1,5,4,6,7]
n = len(arr) - 1
res = missing_integer(arr, n)
print(res)