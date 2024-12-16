'''Given an array with N distinct elements, convert the given array to a reduced form where all elements are in range from 0 to N-1. The order of elements is same, i.e., 0 is placed in place of smallest element, 1 is placed for second smallest element, and N-1 is placed for the largest element.

Note: You don't have to return anything. You just have to change the given array.'''

def convert(arr: list, n):
    hashmap = {}
    copy = arr.copy()
    arr.sort()
    for i in range(n):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = i
    
    i = 0
    for num in copy:
        arr[i] = hashmap[num]
        i += 1
    
# optimal approach

def convert2(arr: list, n):
    
    ans = []
    for i in range(n):
        ans.append((arr[i], i))
    ans.sort()
   
    for i in range(n):
        arr[i] = ans[i][1]
    
arr = [5, 10, 40, 30, 20]
n = len(arr)

res = convert2(arr, n)
print(res)