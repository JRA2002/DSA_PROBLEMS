'''Given an array arr consisting of only 0's and 1's in random order. 
Modify the array in-place to segregate 0s onto the left side and 
1s onto the right side of the array.'''

def segregate_zeros_ones(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        
        if arr[i] == 1 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[j] == 0:
            i += 1
        elif arr[i] == 1:
            j -=1
        else:
            i += 1
            j -= 1
    return arr

arr = [0, 0,1,1,0,0,1,0, 1, 1, 0]
res = segregate_zeros_ones(arr)
print(res)