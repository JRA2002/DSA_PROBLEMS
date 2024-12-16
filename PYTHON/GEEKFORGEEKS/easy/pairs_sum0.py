'''Given an integer array arr, return all the unique pairs 
[arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

Note: The pairs must be returned in sorted order, the solution 
array should also be sorted, and the answer must not contain 
any duplicate pairs.'''

def getPairs(arr: list):
        # code here
        arr.sort()
        i = 0
        j = len(arr) - 1
        res = []
        while i < j:
            
            if arr[i] + arr[j] > 0:
                j -= 1
            elif arr[i] + arr[j] == 0:
                res.append([arr[i],arr[j]])
                i += 1
                j -= 1
            else:
                i += 1
        return res

arr = [4 ,8, 4, 2, 0, -10, 7, 3 ,-7]
res = getPairs(arr)
print(res)