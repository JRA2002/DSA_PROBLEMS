'''Given an array arr[] of size N containing equal number of odd and even numbers. Arrange the numbers in such a way that all the even numbers get the even index and odd numbers get the odd index.
Note: There are multiple possible solutions, Print any one of them. Also, 0-based indexing is considered.'''

def rearrange(arr):
    i = 0
    j = 1
    n = len(arr)
    while i < n and j < n:
        if arr[i]%2 != 0 and arr[j]%2 == 0 :
            arr[i], arr[j] = arr[j], arr[i]
            i += 2
            j += 2
         
        elif arr[i]%2 == 0 and arr[j]%2 != 0 :
            i += 2
            j += 2
            
        elif arr[i]%2 == 0 and arr[j]%2 == 0:
            i += 2
        elif arr[i]%2 == 0 and arr[j]%2 != 0:
            i += 2
        elif arr[i]%2 != 0 and arr[j]%2 != 0:
            j += 2
    return arr
arr = [2,4,6,1,3,5]
n = len(arr)

res = rearrange(arr)
print(res)