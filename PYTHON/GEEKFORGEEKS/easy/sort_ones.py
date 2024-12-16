'''Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.'''

def sort_one_twos(arr):
    l = 0
    h = len(arr) - 1
    m = 0

    while m <= h:
        if arr[m] == 0:
            arr[l], arr[m] = arr[m], arr[l]
            l +=1
            m += 1
        elif arr[m] == 1:
            m += 1
        else:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
    return arr

arr = [0,2,1,2,0]
res = sort_one_twos(arr)
print(res)