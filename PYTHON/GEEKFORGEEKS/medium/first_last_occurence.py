'''Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.'''

def firstAndLast(arr: list, x):
        i = 0
        n = len(arr)
        j = n - 1
        ans = [-1,-1]
        while i <= j:
            midd = (i+j)//2
            if arr[midd] == x:
                temp = midd
                while midd >= 0 and arr[midd] == x:
                    midd -= 1
                ans[0] = midd+1
                while temp < n and arr[temp] == x:
                    temp += 1
                ans[1] = temp-1
                return ans
            elif arr[midd] > x:
                j = midd - 1
            else:
                i = midd + 1
        return ans


arr = [1, 3, 5, 5, 5, 5, 7, 123, 125]
x = 7

res = firstAndLast(arr, x)
print(res)