'''Given an array arr[ ], your task is to find the minimum number of increment operations required to make all the elements of the array unique. i.e.- no value in the array should occur more than once. In one operation, a value can be incremented by 1 only.'''
from collections import Counter
def min_increments(arr: list):
    n = len(arr)
    count = 0
    map = Counter(arr)
    for i in range(n):
        if map[arr[i]] != 1:
            while arr.count(arr[i]) != 1:
                arr[i] = arr[i] + 1
                count += 1
    return count


# optimal approach
def min_increments2(arr: list):
    n = len(arr)
    arr.sort()
    ans = 0
    for i in range(1,n):
        if arr[i] <= arr[i-1]:
            ans += arr[i-1] - arr[i] + 1
            arr[i] = arr[i-1] + 1
    return ans


arr = [1,2,2,1,4,3]

res = min_increments2(arr)
print(res)