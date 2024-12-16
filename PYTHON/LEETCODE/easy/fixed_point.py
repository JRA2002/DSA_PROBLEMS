'''Given an array of distinct integers arr, where arr is sorted in ascending order, return the smallest index i that satisfies arr[i] == i. If there is no such index, return -1.'''

# optimal approach

def find_point(arr: list):
    #usamos binary search porque esta arr esta ORDENADO
    # y nos pide BUSCAR ALGO
    i = 0      #indice izquierdo
    n = len(arr)
    j = n - 1   # indice derecho

    while i <= j:
        midd = (i+j)//2
        if midd == arr[midd]:
            return midd
        elif midd > arr[midd]:
            i = midd + 1
        else:
            j = midd - 1

    return -1

arr = [0,2,5,8,17]
res = find_point(arr)
print(res)