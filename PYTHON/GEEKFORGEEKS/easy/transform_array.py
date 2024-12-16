'''Given an array arr[] containing integers, zero is considered an invalid number, and the rest of the other numbers are valid. If the two nearest valid numbers are equal, then double the value of the first one and make the second number 0. At last, move all the valid numbers on the left.'''

def transform_array(arr: list):
    n = len(arr)
    for i in range(n-1): 
        j = i+1
        if arr[j] == 0:
            while j < n-1 and arr[j] == 0:
                j += 1
        if arr[i] == arr[j] and arr[i] != 0:
            arr[i] = arr[i]*2
            arr[j] = 0
    i = 0
    j = 1
    while i <= n-1 and j <= n-1:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[i] == 0 and arr[j] == 0:
            j += 1
        else:
            i += 1
            j += 1
    return arr
arr = [2, 4, 5, 0, 0, 5, 4, 8, 6, 0, 6, 8]

res = transform_array(arr)
print(res)