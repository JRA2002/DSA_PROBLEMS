'''You are given a number k and array arr. Your task is to rearrange the elements of array arr according to the absolute difference with k, i.e., an element having minimum difference comes first, and so on.
Note: If two or more elements are at equal distances arrange them in the same sequence as in the given array.'''

def sort_by_difference(arr: list, k: int):
    map = {}
    copy = arr.copy()
    n = len(arr)

    for i in range(n):
        if i not in map:
            map[i] = abs(arr[i] - k)
    map = dict(sorted(map.items(), key=lambda item: item[1]))
    
    i = 0
    for key in map.keys():
        arr[i] = copy[key]
        i += 1
    return arr

k = 4
arr = [1, 3, 7, 8, 3, 2, 5]

res = sort_by_difference(arr, k)
print(res)