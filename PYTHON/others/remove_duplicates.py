'''Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.'''

def remove_duplicates(arr):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] not in new_arr:
            new_arr.append(arr[i])
    return new_arr

arr = [1, 2, 1, 1, 3, 2]
res = remove_duplicates(arr)
print(res)

# N --> lenght of array
# Time Complexity: O(N)
# Auxiliary Space: O(N)