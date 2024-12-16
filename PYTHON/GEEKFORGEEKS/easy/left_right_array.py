'''Given an array arr[], determine if it can be rearranged such that each element is equal to the number of elements to its left or the number of elements to its right. Return true if the condition is met, otherwise return false.'''

def left_right(arr: list):
        n = len(arr)
        
        if n < max(arr):
            return False
        for i in range(n):
            temp = arr[arr[i]]
            arr[arr[i]] = arr[i]
            arr[i] = temp

        if arr[0] == arr[n-1] or arr[n-1] == n-1:
            return True
        return False

arr = [1, 6, 5, 4, 3, 2, 1]

res = left_right(arr)
print(res)