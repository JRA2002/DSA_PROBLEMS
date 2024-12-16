'''You are given an array of size N. Rearrange the given 
array in-place such that all the negative numbers occur 
before all non-negative numbers.
(Maintain the order of all -ve and non-negative numbers 
as given in the original array).'''
def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

def merge(arr, l, m, r):
        i = l  # Initial index of 1st subarray
        j = m + 1  # Initial index of IInd

        while i <= m and arr[i] < 0:
            i += 1

        # arr[i..m] is positive

        while j <= r and arr[j] < 0:
            j += 1

        # arr[j..r] is positive

        # reverse positive part of left sub-array (arr[i..m])
        reverse(arr, i, m)

        # reverse negative part of right sub-array (arr[m+1..j-1])
        reverse(arr, m + 1, j - 1)

        # reverse arr[i..j-1]
        reverse(arr, i, j - 1)

def rearrangePosNeg(arr, l, r):
        if l < r:
            m = l + (r - l) // 2

            # Sort first and second halves
            rearrangePosNeg(arr, l, m)
            rearrangePosNeg(arr, m + 1, r)

            merge(arr, l, m, r)

def rearrange(n, arr):
    rearrangePosNeg(arr, 0, n - 1)
    return arr

# Time Complexity: O(Nlog(N))
# Auxiliary Space: O(log(N))



# brute force approach

def rearrange_1(n, arr):
    for i in range(n):
            key = arr[i]
            if key < 0:
                  continue
            j = i - 1
            while j >= 0 and arr[j] >= 0:
                
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
    return arr  

# Time Complexity: O(N*N)
# Auxiliary Space: O(1)  


arr = [-1 ,-1 ,0, 0, 1,1]
n = len(arr)
res = rearrange_1(n, arr)
print(res)
    