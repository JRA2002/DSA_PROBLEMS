'''Given a sorted array arr[] of positive integers. The task is to find the closest value in the array to the given number k. The array may contain duplicate values.

Note: If the difference with k is the same for two values in the array return the greater value.'''

def find_closest(n, k, arr: list):
    i = 0
    j = n - 1

    while i <= j:
        midd = (i+j)//2
        if arr[midd] > k:
            j = midd - 1
        else:
            i = midd + 1
   
    if k < arr[midd]:
        if abs(arr[midd] - k) <= abs(arr[midd-1] - k):
            return arr[midd]
        return arr[midd-1]
    else:
        if midd == n-1:
            return arr[midd]
        elif abs(arr[midd] - k) >= abs(arr[midd+1] - k):
            return arr[midd+1]
        return arr[midd]


k = 13
arr = [6,8,10,12]
n = len(arr)

res = find_closest(n, k, arr)
print(res)