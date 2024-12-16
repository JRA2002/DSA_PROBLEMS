'''Given an array that contains both positive and negative 
integers, the task is to find the product of the maximum product subarray. '''


def maxi_product(arr):
    max_new = arr[0]
    max_actual = 1
    start = 0
    end = 0
    s = 0
    
    for i in range(len(arr)):
        max_actual = max_actual * arr[i]
        if max_new <= max_actual:
            max_new = max_actual
            start = s
            end = i
        if max_actual == 0:
            max_actual = 1
            s = 1 + i
    return max_new,start,end

arr = [6, -3, -10, 0, 2]
res = maxi_product(arr)
print(res)