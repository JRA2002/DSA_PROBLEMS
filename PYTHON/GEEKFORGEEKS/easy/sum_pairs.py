'''Given two unsorted arrays arr1[]  and arr2[], the task is to find all pairs whose sum equals x from both arrays.

Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.'''

def get_pairs(x: int, arr1: list, arr2: list):
    arr1.sort()
    for num in arr1:
        if (x - num) in arr2:
            print(num,x-num)

x = 6
arr1 = [1, 2, 4, 5, 7] 
arr2 = [5, 1, 3, 4, 8]

res = get_pairs(x, arr1, arr2)
print(res)