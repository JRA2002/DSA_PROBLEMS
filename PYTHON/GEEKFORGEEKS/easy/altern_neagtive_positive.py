'''Given an unsorted array arr containing both positive 
and negative numbers. Your task is to create an array of 
alternate positive and negative numbers without changing 
the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0
 (zero) should be considered a positive element.'''

def rearrange(arr):
    neg = []
    pos = []
    n = len(arr)
    
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])
    i = 0
    k = 0
    j = 0
    while i < len(pos) and j < len(neg):
        arr[k] = pos[i]
        i += 1
        k += 1
        arr[k] = neg[j]
        j += 1
        k += 1
    while i < len(pos):
        arr[k] = pos[i]
        i += 1
        k += 1
    while j < len(neg):
        arr[k] = neg[j]
        j += 1
        k += 1    
    return arr
        

arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
res = rearrange(arr)
print(res)