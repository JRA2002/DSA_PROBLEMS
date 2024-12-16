'''Given an array arr of n elements that is first strictly increasing and 
then maybe strictly decreasing, find the maximum element in the array.

Note: If the array is increasing then just print the last element will be the maximum value.'''

def peak_element(arr):
    lista = []
    for i in range(1,len(arr) - 1):
        if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
            lista.append((arr[i]))
    return lista

arr = [10, 20, 15, 2, 23, 90, 67]
res = peak_element(arr)
print(res)