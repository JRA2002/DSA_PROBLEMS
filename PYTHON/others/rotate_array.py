'''Given an array, the task is to cyclically rotate the array clockwise by one time.'''

def rotate(arr):
    k = len(arr) - 1
    temp =  arr[k]
    for i in range(k, -1, -1):
        arr[i] = arr[i-1]
        if i == 0:
            arr[i] = temp
    return arr
#arr = [2,3,4,5,6,7,8,9]
#res = rotate(arr)
#print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)

def rotate_two_pointers(arr):
    i = 0 # begin
    j = len(arr) - 1  # last item of array

    while i != j :
        arr[i], arr[j] = arr[j], arr[i]
        i += 1

    return arr

arr = [2,3,4,5,6,7,8,9]
res = rotate_two_pointers(arr)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(1)

