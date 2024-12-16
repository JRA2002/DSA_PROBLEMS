'''Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.'''

def max_distance(arr):
    dict1 = {}
    dict2 = {}
    for i in range(len(arr)-1,-1,-1):
        if arr[i] not in dict1:
            dict1[arr[i]] = i
    for i in range(len(arr)):
        if arr[i] not in dict2:
            dict2[arr[i]] = i
    maxi = 0
    for num in arr:
        if dict1[num] - dict2[num] >= maxi:
            maxi = dict1[num] - dict2[num]

    return maxi

arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]

res = max_distance(arr)
print(res)