'''Given an array arr[] of size n and an integer x, return 1 if 
there exists a pair of elements in the array whose absolute
 difference is x, otherwise, return -1.'''

def pair_difference(n, x, arr: list):
    arr.sort()
    i = 0
    j = 1
    while i < j and j < n:
        if i != j and abs(arr[i] - arr[j]) == x:
            return 1
        elif abs(arr[i] - arr[j]) > x:
            i += 1
            
        else: 
            j += 1
    return -1

# Time Complexity:O(N*LogN)
# Auxiliary Space: O(1)
        



# optimal approach usin N space

def difference(n, x, arr):
    res = set()

    for i in range(n):
        if (arr[i] - x) in arr or (arr[i] + x) in arr:
            return 1
        res.add(arr[i])
    return -1

arr = [1,1,1,2,7,10 ]
n = len(arr)
x = 9
res = difference(n, x, arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(N)