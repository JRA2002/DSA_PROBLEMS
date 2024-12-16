'''Given an array of positive and negative numbers, the task 
is to find if there is a subarray (of size at least one) with 0 sum.'''

def subarray_zero(arr):
    if 0 in arr:
        return True
    k = 2
    while k <= len(arr):
        for i in range(len(arr) - k + 1):
            new = arr[i:k+i]
            
            if sum(new) == 0:
                print(new)
                return True
        k += 1
    return False

arr = [-3, 2, 3, 1, 6]
res = subarray_zero(arr)
print(res)