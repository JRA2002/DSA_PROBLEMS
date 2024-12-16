'''Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.'''

def duplicate_zeros(arr: list):
    i = 0
    j = len(arr) - 1
    while i <= j:
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i += 2
        else:
            i += 1 
        print(arr)
    return arr

arr = [0,4,1,0,0,8,0,0,3]

res = duplicate_zeros(arr)
print(res)