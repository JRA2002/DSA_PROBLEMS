'''reverse an array using recursion'''

def reverse(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr, start + 1, end - 1)

    return arr


arr = [10, 20, 15, 2, 23, 90, 67]
start  = 0
end  = len(arr) - 1
res = reverse(arr, start, end)
print(res)
