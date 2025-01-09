'''Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.'''

def third_largest(arr: list):
    f = -1
    s = -1
    t = -1

    for num in arr:
        if num > t:
            t = num
        if t > s:
            t, s = s, t
        if s > f:
            s, f = f, s

    return t

arr = [2, 4, 1, 3, 5]

print(third_largest(arr))