'''Given an array arr of distinct elements of size n, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 

Note: Modify the given arr[] only, If your transformation is correct, the output will be 1 else the output will be 0. '''

def zigzag_array(n: int, arr: list):
    i = 1
    flag2 = False
    flag1 = True
    while i < n - 1:
        if arr[i-1] > arr[i] and flag2 == False and flag1 == True:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i += 1
            flag2 = True
            flag1 = False
        if arr[i] < arr[i+1] and flag2 == True:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            i += 1
            flag2 = False
            flag1 = True
        
    

arr = [4, 7, 3, 8, 2]
n = len(arr)

res = zigzag_array(n, arr)
print(res)
