'''Given an array arr of n elements that is first strictly 
increasing and then maybe strictly decreasing, find the 
maximum element in the array.
Note: If the array is increasing then just print the last 
element will be the maximum value.'''

def find_maximum(arr, n):
    i = 0
    while i < n:
        r1 = arr[i]
        if i+1<n:
            r2 = arr[i+1]
        if r1 > r2:
            return r1
        i += 1
    return arr[-1]

arr = [11, 45, 47, 50, 5]
n = len(arr)
res = find_maximum(arr, n)
print(res)