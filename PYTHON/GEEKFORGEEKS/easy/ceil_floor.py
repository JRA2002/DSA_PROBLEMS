'''Given an unsorted array arr[] of integers and an integer x, 
find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or 
equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or 
equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. 
Return -1 for floor or ceiling if the floor or ceiling is not present.'''

def get_ceil_floor(x : int, arr :list):
    if x < min(arr):
        f = -1
    else:
        f = min(arr)
    for i in arr:
        if i <= x and f <= i:
            f = i

    if x > max(arr):
        c = -1
    else:
        c = max(arr)
    
    for i in arr:
        if i >= x and c >= i:
            c = i
    return [f,c]
x = 17
arr = [36 ,82, 88 ,56, 21 ,17, 73, 86]

res = get_ceil_floor(x, arr)
print(res)