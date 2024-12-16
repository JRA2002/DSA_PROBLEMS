'''Given two integer arrays a of size n and b of size m, the task is to find the numbers which are present in the first array a, but not present in the second array b.

Note: Numbers to be returned should in order as they appear in array a'''

def find_missing(a,b,n,m):
    hashmap = {}
    ans = []
    for num in b:
        if num not in hashmap:
            hashmap[num] = 1
    
    for num in a:
        if num not in hashmap:
            ans.append(num)
    return ans

a = [1, 2, 3, 4, 5, 10]
n = len(a)
b = [2, 3, 1, 0, 5]
m = len(b)

res = find_missing(a, b, n, m)
print(res)