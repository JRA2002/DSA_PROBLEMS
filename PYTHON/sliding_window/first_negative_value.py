'''Given an array and a positive integer k, find the first negative integer 
for each window(contiguous subarray) of size k. If a window does not contain 
a negative integer, then print 0 for that window.'''

def first_negative(arr, k):
    if len(arr) < k :
        return -1
    lista = []
    for i in range(len(arr) - k + 1):
        new_arr = arr[i:k+i]
        mini = min(new_arr)
        if mini < 0:
            lista.append(mini)
        else:
            lista.append(0)
    return lista

arr = [-8, 2, 3, -6, 10]
res = first_negative(arr, 2)
print(res)