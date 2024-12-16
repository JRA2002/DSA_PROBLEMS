'''Given an array arr of n positive integers. The task is to swap every ith element of the array with (i+2)th element.'''

def swap_elements(arr: list, n):
    for i in range(n-2):
        arr[i], arr[i+2] = arr[i+2], arr[i]
        print(arr)
    return arr
arr = [1,2,3,4,5]
n = len(arr)

res = swap_elements(arr, n)
print(res)