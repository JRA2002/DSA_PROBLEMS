'''Given an array arr[] and an integer K, the task is to calculate the sum of all subarrays of size K.'''
def sum_subarrays(arr, k):
    if len(arr) < k:
        return 0
    lista = []
    for i in range(len(arr) - k + 1):
        new_arr = arr[i:k+i]
        suma = sum(new_arr)
        lista.append(suma)

    return lista

arr = [1, 2, 3, 4, 5, 6]
res = sum_subarrays(arr, 3)

print(res)
