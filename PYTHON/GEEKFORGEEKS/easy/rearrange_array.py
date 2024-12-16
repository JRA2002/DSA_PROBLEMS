'''Given an array arr[] containing integers,  your task is to print 
the array in the order – smallest number, largest number, 2nd 
smallest number, 2nd largest number, 3rd smallest number, 3rd 
argest number and so on.'''

def rearrange_array(arr):
        arr.sort()
        res = arr[:]
        n = len(arr)
        k = 0
        i = 0
        j = n - 1
        while k < n:
            arr[k] = res[i]
            if k+1 < n:
                arr[k+1] = res[j]
            k += 2
            i += 1
            j -= 1
        return arr

arr = [1, 9, 2, 8, 3, 7, 4, 6, 5]
res = rearrange_array(arr)
print(res)
