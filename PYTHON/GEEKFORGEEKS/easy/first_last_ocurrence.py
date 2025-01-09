'''Given an element x and a sorted array, arr[], find the indices of first and last occurrences of the x's in the array.

Note: If the number x is not found in the array, return an array containing -1 only.'''

def first_last(x: int, arr: list):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r) // 2
        if arr[m] == x:
            tmp = m
            while m >= 0 and arr[m] == x:
                m -= 1
            first = m + 1

            while tmp < len( arr) and arr[tmp] == x:
                tmp += 1
            last = tmp - 1

            return [first, last]
        
        elif arr[m] > x:
            r = m - 1
        else:
            l = m + 1

    return [-1]

x = 4
arr = [2,3,4,4,4]

print(first_last(x, arr))
