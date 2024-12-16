'''You are given an array a, of n elements. Find the minimum 
index based distance between two distinct elements of the 
array, x and y. Return -1, if either x or y does not exist in the'''

def min_distance(arr, n, x, y):
    res = 1000
    ey = 1000
    ex = 2000
    if x not in arr or y not in arr:
        return -1
    for i,v in enumerate(arr):
        if v == x:
            ex = i
            print(ex)
        if v == y:
            ey = i
            print(ey)
        diff = abs(ey - ex)
        res = min(diff,res)
    
    return res

arr = [2,8 ,19, 4, 9, 1]
n = len(arr)
x = 9
y = 19

res = min_distance(arr, n, x, y)
print(res)