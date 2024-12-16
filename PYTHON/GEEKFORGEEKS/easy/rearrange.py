def rearrange(arr, n):
    j = n - 1

    for i in range(j,-1,-1):
        if arr[i] > 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

arr = [6,-2,-4,3,-2,-2,8]
n = len(arr)
res = rearrange(arr, n)
print(res)