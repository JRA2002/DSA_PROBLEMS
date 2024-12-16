'''Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr'''

def minimum_value(arr: list):
    arr.sort()
    n = len(arr)
    if n <= 2:
        return [arr]
    ans = []
    mini = arr[-1]
    for i in range(n - 1):
        mini = min(abs(arr[i+1] - arr[i]), mini)
    print(mini)
    for i in range(n - 1):
        if abs(arr[i+1] - arr[i]) == mini:
            ans.append([arr[i], arr[i+1]])

    return ans


arr = [-10, 23]
res = minimum_value(arr)
print(res)
