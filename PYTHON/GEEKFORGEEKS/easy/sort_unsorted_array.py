'''Given an unsorted array arr[]. Find the subarray arr[s...e] such that sorting this subarray makes the whole array sorted.

Note: If the given array is already sorted then return [0, 0].'''

def print_unsorted(arr: list):
    n = len(arr)
    s = 1
    e = n-1
    count = 0
    for i in range(n-1):
        if arr[i] < arr[i+1]:
            count += 1
        if count > 0:
            return [0,0]
    s = 1
    e = n-1
    flag1 = True
    flag2 = True
    while flag1 and flag2:
        if min(arr[s:e]) != arr[s] and flag1==True:
            flag1 = False
        else:
            s += 1
        if max(arr[s:e]) != arr[e] and flag2 == True:
            flag2 = False
        else:
            e -= 1
    return [s,e]

    
    

arr = [0, 1, 15, 25, 6, 7, 30, 40, 50]

res = print_unsorted(arr)
print(res)