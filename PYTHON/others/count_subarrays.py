'''Given an array arr[] of size n containing 0 and 1 only. 
The problem is to count the subarrays having an equal number of 0s and 1s.'''

def count_subarrays(arr: list):
    k = 2
    count = 0
    while k <= len(arr):
        for i in range(len(arr) - k + 1):
            new = arr[i:k+i]
            a = new.count(0)
            b = new.count(1)
            if a == b:
                count += 1
        k += 1
    return count
arr = [1,0,0,1,0,1,1]
res = count_subarrays(arr)
print((res))

# Time Complexity:O(N*LogN)
# Auxiliary Space: O(N)
