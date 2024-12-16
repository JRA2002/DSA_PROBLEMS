'''Given an unsorted array of integers, sort the array into a
 wave array. An array arr[0..n-1] is sorted in wave form if:
arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..'''

def wave(arr):
    i = 0
    j = len(((arr))) - 1
    while i < j :
        if arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
        i += 2
    return arr

arr = [3,5,7,1,2,99,10]
res = wave(arr)
print(res)

# Time Complexity: O(N)
# Auxiliary Space: O(1)