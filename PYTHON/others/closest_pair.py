'''Given a sorted array and a number x, find a pair in an array whose sum is closest to x.'''
def closest(arr, x):
    if len(arr) == 1:
        return arr[0]
    
    j = len(arr) - 1
    i = 0
   
    while i < j:
        if x > arr[j] + arr[i]:
            pair = (arr[i], arr[j])
        i += 1

    print(pair)
    closest(arr[:-1], x)

arr = [1, 3, 4, 7, 10]
closest(arr, 15)

# Time Complexity:O(N)
# Auxiliary Space: O(N)