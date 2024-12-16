'''Given a sorted array Arr[](0-index based) consisting of N distinct integers and an integer k, the task is to find the index of k, if its present in the array Arr[]. Otherwise, find the index where k must be inserted to keep the array sorted.'''

def search_insert(Arr, N, k):
    i = 0
    j = N - 1
    while i <= j:
        midd = (i+j)//2
        if Arr[midd] == k:
            return midd
        elif Arr[midd] > k:
            j = midd - 1
        else:
            i = midd + 1
    
    if Arr[midd] > k:
        return midd
    return midd+1

Arr = [1, 3, 5, 6]
k = 4
N = len(Arr)

res = search_insert(Arr, N, k)
print(res)