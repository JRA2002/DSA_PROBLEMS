'''Given an array arr. Return the modified array in such a way that if the current and next numbers are valid numbers and are equal then double the current number value and replace the next number with 0. After the modification, rearrange the array such that all 0's are shifted to the end.

Note:

Assume ‘0’ as the invalid number and all others as a valid number.
The sequence of the valid numbers is present in the same order.'''

def modify_array(arr: list):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] == arr[i+1]:
            arr[i] = arr[i]*2
            arr[i+1] = 0
    
    i = 0
    j = 1
    
    while i <= n-1 and j <= n-1:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
           
        elif arr[i] == 0 and arr[j] == 0:
            j += 1
        else:
            i += 1
            j += 1

    return arr

arr = [14, 13, 13, 20, 20, 13, 19, 11, 18, 17, 17, 11, 17, 15, 13, 13, 10, 12, 19]

res = modify_array(arr)
print(res)