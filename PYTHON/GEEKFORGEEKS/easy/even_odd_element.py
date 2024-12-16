'''Given an array arr[], the task is to arrange the array such that odd elements occupy the odd positions and even elements occupy the even positions. The order of elements must remain the same. Consider zero-based indexing. After printing according to conditions, if remaining, print the remaining elements as it is.'''

def arrange_odd_even(arr: list):
    even = []
    odd = []
    for num in arr:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)

    n = len(arr)
    le = len(even)
    lo = len(odd)
    i = 0
    j = 0
    k = 0
    while k <= n-1 :
        if i <= le-1:
            arr[k] = even[i]
            i += 1
            k += 1
        if j <= lo-1:
            arr[k] = odd[j]
            j += 1
            k += 1
    return arr

arr = [3,7,4,1]

res = arrange_odd_even(arr)
print(res)