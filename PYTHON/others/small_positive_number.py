'''Given an unsorted array arr[] with both positive and negative 
elements, the task is to find the smallest positive number 
missing from the array.

Note: You can modify the original array.'''

def small_positive(arr: list, n):

    ptr = 0

    # Check if 1 is present in array or not
    for i in range(n):
        if arr[i] == 1:
            ptr = 1
            break

    # If 1 is not present
    if ptr == 0:
        return(1)

    # Changing values to 1
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = 1
    print(arr)
    # Updating indices according to values
    for i in range(n):
        arr[(arr[i] - 1) % n] += n
        print(arr)
    print(arr)
    # Finding which index has value less than n
    for i in range(n):
        if arr[i] <= n:
            return(i + 1)

    # If array has values from 1 to n
    return(n + 1)


arr = [1,2,3,6]
n = len(arr)
res = small_positive(arr, n)
print(res)

# Time Complexity: O(N)
# Auxiliary Space: O(1)