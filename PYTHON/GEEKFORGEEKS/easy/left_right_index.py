'''Given a sorted array with possibly duplicate elements. The task is to find indexes of first and last occurrences of an element X in the given array.

Note: If the element is not present in the array return {-1,-1} as pair.'''

def indexes(v: list, x: int):
    l = 0 
    r = len(v) - 1

    while l <= r:
        m = (l+r) // 2
        if v[m] == x:
            tmp = m
            while m >= 0 and v[m] == x:
                m -= 1

            first = m + 1

            while tmp < len(v) and v[tmp] == x:
                tmp += 1

            last = tmp - 1

            return [first, last]
        elif v[m] > x:
            r = m - 1
        else: 
            l = m + 1

    return [-1, -1]



v = [2,3,4]
x = 4

print(indexes(v, x))