'''Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b'''

def closest_elements(arr: list, k: int, x: int):
    l = 0
    r = len(arr) - k

    while l < r:
        m = (l + r)//2
        
        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m
        
    return arr[l:l+ k]



arr = [1,2,3,4,5]
k = 4
x = -1

res = closest_elements(arr, k, x)
print(res)