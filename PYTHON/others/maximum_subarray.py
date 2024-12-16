'''Given an array arr[] of size N. The task is to find 
the sum of the contiguous subarray within a arr[] with the largest sum. '''

# Kadane Algorithm

def maxi_sum(arr):
    max_new = arr[0]
    max_actual = 0
    start = 0
    end = 0
    s = 0
    
    for i in range(len(arr)):
        max_actual = max_actual + arr[i]
        if max_new < max_actual:
            max_new =  max_actual
            start = s
            end = i
        if max_actual < 0:
            max_actual = 0
            s = 1 + i
    return start, end

arr = [-2,-3,4,-1,-2,1,5,-3]
res = maxi_sum(arr)
print(res)

# Time Complexity: O(N)
# Auxiliary Space: O(1)
