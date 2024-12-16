def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        j = i
        while j > 0 and arr[j-1] > curr:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = curr
    return arr
arr = [4,1,1,2,3,6,7,8]
res = insertion_sort(arr)
print(res)
