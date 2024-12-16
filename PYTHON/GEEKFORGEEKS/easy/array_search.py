'''Given an array, arr of n integers, and an integer 
element x, find whether element x is present in
 the array. Return the index of the first occurrence
   of x in the array, or -1 if it doesn't exist.'''

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return  i
    return -1

arr = [10, 8, 30, 4, 5]
x = 5
res = search(arr, x)
print(res)