'''Given an unsorted array arr[ ] having both negative and positive integers. 
The task is to place all negative elements at the end of the array without 
changing the order of positive elements and negative elements.'''

def move_negative(arr: list):
    neg = []
    pos = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    i = 0
    k = 0
    j = 0
    while i < len(pos):
        arr[k] = pos[i]
        i += 1
        k += 1
        
    while j < len(neg):
        arr[k] = neg[j]
        j += 1
        k += 1    
    return arr

arr = [1, -1, 3, 2, -7, -5, 11, 6 ]
res = move_negative(arr)
print(res)