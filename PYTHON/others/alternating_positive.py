'''Given an array having positive and negative numbers, our task 
is to arrange them in an alternate fashion such that every positive
number is followed by a negative number and vice-versa maintaining 
the order of appearance. The number of positive and negative numbers 
need not to be equal. If there are more positive numbers then they have 
to appear at the end of the array , same condition for negative numbers also .'''

def rearrange(arr: list):
    neg = []
    pos = []
    n = len(arr)
    
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    i = 0
    k = 0
    j = 0
    while i < len(pos) and j < len(neg):
        arr[k] = pos[i]
        i += 1
        k += 1
        arr[k] = neg[j]
        j += 1
        k += 1
    while i < len(pos):
        arr[k] = pos[i]
        i += 1
        k += 1
    while j < len(neg):
        arr[k] = neg[j]
        j += 1
        k += 1    
    return arr


arr = [35, -43, 29, 32, 29 ,-37, 46 ,39, -3, -43,-19, 32, 43, 27 ,28, 11 ,43, -21, -35 ,-25, -2, 36, -13, -6, 2, -45, -37, -4, -37, 35, -46 ,5, -13, 10, 41 ,-34, -30 ,28 ,-47, -9 ,26, 21 ,-44, 17, 16 ,-5, 39, 14, -35, 24, -9, 12 ,-15, 31, -32, 32, 47, 16, -30]
res = rearrange(arr)
print(res)
