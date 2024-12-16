'''Given a sorted array arr[] (may be distinct or may contain duplicates) 
of size N that is rotated at some unknown point, the task is to find 
the minimum element in it. '''

def minimum_element(arr):
    mini = arr[0]

    for i in range(1,len(arr)):
        if arr[i] < mini:
            mini = arr[i]

    return mini
arr = [5, 6, 1, 2, 3, 4]
res = minimum_element(arr)
print(res)

# Time complexity: O(N) 
# Auxiliary Space: O(1)
