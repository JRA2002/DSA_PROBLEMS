'''Given an array arr[] where each element represents 
the max number of steps that can be made forward from 
that index. The task is to find the minimum number of 
jumps to reach the end of the array starting from index 0.'''

def jumps(arr):
    i = 0 
    res = True
    count = 0 
    while res:
        if arr[i]:
            i = i + arr[i]
            count += 1
        if i >= len(arr) - 1:
            res = False
    return count

arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
res = jumps(arr)
print(res)