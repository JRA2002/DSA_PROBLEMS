'''Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.'''

def unique_occurrences(arr: list[int]) -> bool:
    hash_map = {}
    for i in range(len(arr)):
        if arr[i] not in hash_map:
            hash_map[arr[i]] = 1
        else:
            hash_map[arr[i]] += 1
    set1 = set()
    l = 0
    for v in hash_map.values():
        l += 1
        set1.add(v)
    if len(set1) == l:
        return True
    return False

#optimal approach

def unique_concurrences2(arr: list):
    pass

arr = [1,2]
res = unique_occurrences(arr)
print(res)