'''Given an array of size N and an integer K, return the count of distinct numbers in all windows of size K. '''

def count_distinct(arr, k):
    if len(arr) < k:
        return 0
    lista = []
    for i in range(len(arr) - k + 1):
        new_arr = arr[i:k+i]
        set1 = set(new_arr)
        count = 0
        for _ in set1:
            count += 1
        lista.append(count)
    return lista

arr = [1, 2, 1, 3, 4, 2, 3]
arr.sort()
res = count_distinct(arr, 4)
print(res)