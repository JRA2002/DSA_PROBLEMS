'''You are given an array of integers arr[]. Your task is to reverse the given array.

Note: Modify the array in place.'''

def reverse_array(arr: list):
    l = 0
    r = len(arr) - 1

    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr

arr = [1, 4, 3, 2, 6, 5]

print(reverse_array(arr))