'''Given an array arr of positive integers. The task is to return the maximum of j - i subjected to the constraint of arr[i] < arr[j] and i < j.'''

def maximum_index(arr: list):

    lmin = []
    rmax = []
    n = len(arr)
    mini = arr[0]
    for i in range(n//2 + 1):
        if arr[i] < mini:
            mini

arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]

res = maximum_index(arr)
print(res)