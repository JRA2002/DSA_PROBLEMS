'''Given a string, find the smallest window length with all distinct characters of the given string. For eg. str = “aabcbcdbca”, 
then the result would be 4 as of the smallest window will be “dbca” .'''

def smallest_arr(arr, k):
    if len(arr) < k:
        return 0
    lista = []
    set1 = set(arr)
    for i in range(len(arr) - k + 1):
        new_arr = arr[i:k+i]
        lista.append(new_arr)
        count = 0
        for j in set1:
            if j in new_arr:
                count += 1
        if count == 4:
            return True
        
    return False
arr = 'aabcbcdbca'
res = smallest_arr(arr, 4)

print(res)