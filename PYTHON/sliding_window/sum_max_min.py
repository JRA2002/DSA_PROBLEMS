'''Given an array of both positive and negative integers, the task 
is to compute sum of minimum and maximum elements of all sub-array of size k.'''

def sum_min_max(arr, k):
    if len(arr) < k:
        return 0
    suma = 0
    for i in range(len(arr) - k + 1):
        new_arr = arr[i:k+i]
        print(new_arr)
        mini = min(new_arr)
        maxi = max(new_arr)
        suma = mini + maxi + suma
    return suma

arr = [2, 5, -1, 7, -3, -1, -2]
res = sum_min_max(arr, 4)

print(res)