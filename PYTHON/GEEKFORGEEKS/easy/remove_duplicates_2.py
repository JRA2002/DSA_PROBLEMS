'''Given a sorted array arr. Return the size of the modified array which contains only distinct elements.
Note:
1. Don't use set or HashMap to solve the problem.
2. You must return the modified array size only where distinct elements are present and modify the original array such that all the distinct elements come at the beginning of the original array.'''

def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    i = 0

    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    
    return i + 1

arr = [2,2,3,4,2]
res = remove_duplicates(arr)
print(res)