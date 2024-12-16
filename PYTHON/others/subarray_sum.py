'''Given a 1-based indexing array arr[] of integers and an 
integer sum. You mainly need to return the left and right 
indexes(1-based indexing) of that subarray. In case of multiple subarrays, 
return the subarray indexes which come first on moving from left to right. 
If no such subarray exists return an array consisting of element -1.'''

def subarray_sum(arr, suma):
    if arr[0] == suma:
        return 0
    k = 2
    lista = []
    while k < len(arr):
        for i in range(len(arr) - k + 1):
            new_arr = arr[i:k+i]
        
            if sum(new_arr) == suma:
                lista.append((i, k+i))
                return lista
        k += 1
    return -1
arr = [1, 4, 0, 0, 3, 10, 5]
res = subarray_sum(arr, 7)
print(res)

