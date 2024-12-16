'''Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.'''

def array_transform(arr: list):
    hash_index = {}
    n = len(arr)
    for i in range(n):
        if i not in hash_index:
            hash_index[i] = arr[i]
    
    arr.sort()
    hash_table = {}
    j = 1

    for i in range(n):
        if arr[i] not in hash_table:
            hash_table[arr[i]] = j
            j += 1
  
    for k,v in hash_index.items():
        arr[k] = hash_table[v]

    return arr

#optimal approach

def array_transform2(arr: list):
    hash_rank = {}
    copy = arr.copy()
    copy.sort()

    rank = 1
    for i in range(len(copy)):
        if copy[i] not in hash_rank:
            hash_rank[copy[i]] = rank
            rank += 1

    for i in range(len(arr)):
        copy[i] = hash_rank[arr[i]]
    return copy

arr = [20,10,20,10]

res = array_transform2(arr)
print(res)