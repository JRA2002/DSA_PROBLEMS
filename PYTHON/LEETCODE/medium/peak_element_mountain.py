'''You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.'''

def peak_index_mountain(arr: list):
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r) // 2
        print(l,m,r)
        if (arr[m-1] < arr[m] and arr[m] > arr[m+1]):
            return m
        elif arr[m-1] > arr[m]:
            r = m - 1
        else:
            l = m + 1

    return m+1

arr = [3,9,8,6,4]

print(peak_index_mountain(arr))