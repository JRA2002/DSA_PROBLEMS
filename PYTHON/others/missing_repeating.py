'''Given an unsorted array of size n. Array elements are 
in the range of 1 to n. One number from set {1, 2, …n} is
missing and one number occurs twice in the array. Find 
these two numbers.'''

def missing_repeating(arr):
    n = len(arr) - 1
    miss = 0
    rep = 0
    
    for i in range(1, n + 1):
        if i not in arr:
            miss = i
            break
    for i in range(len(arr) - 1):
        if arr[i] == arr[i+1]:
            rep = arr[i]
            break
        
    return miss, rep

arr = [4, 3, 6, 2, 1, 1]
res = missing_repeating(arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)