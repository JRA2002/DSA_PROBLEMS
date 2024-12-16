def minmax(arr, n):

    if n == 1:
        return arr[0]
    return max(arr[n - 1], minmax(arr, n - 1))

arr = [1,2,3,4,5,6]
n = len(arr)
res = minmax(arr, n)
print(res)