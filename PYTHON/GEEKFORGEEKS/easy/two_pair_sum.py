'''Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.'''

def get_pairs(arr: list):
    arr.sort()

    l = 0
    r = len(arr) - 1
    ans = set()
    res = []

    while l < r:
        if arr[l] + arr[r] == 0:
            ans.add((arr[l], arr[r]))
            l += 1
            r -= 1
        elif arr[l]+arr[r] > 0:
            r -= 1
        else:
            l += 1
            
    for tup in ans:
        res.append(list(tup))
    res.sort()

    return res




arr = [6, 1, 6, 0, 4, -9, -1, -10, -6, -6]

print(get_pairs(arr))