'''Given an array A[] consisting of only 0s, 1s, and 2s. The task is to sort 
the array, i.e., put all 0s first, then all 1s and all 2s in last'''

def national_flag(arr: list):
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
            


arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
res = national_flag(arr)
print(res)