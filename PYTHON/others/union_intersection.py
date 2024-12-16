'''Given two sorted arrays, find their union and intersection.'''
def union_inter(arr1: list, arr2: list):
    union = []
    for i in arr2:
        if i not in arr1:
            arr1.append(i)
        else:
            union.append(i)
    print(union)
    print(arr1)

#arr1 = [1, 3, 4, 5, 7]
#arr2  = [2, 3, 5, 6]

#union_inter(arr1, arr2)

# Time complexity: O(N * M) 
# Auxiliary Space: O(M+N)

# using 2 pointers , more efficient approach
def next_distinct(arr, x):
    while x < len(arr) - 1 and arr[x] == arr[x+1]:
        x += 1
    return x + 1

def union(arr1, arr2, m, n):
    i = 0
    j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
           print(arr1[i], sep=' ')
           i = next_distinct(arr1, i)
        elif arr1[i] > arr2[j]:
           print(arr2[j], sep=' ')
           j = next_distinct(arr2, j)
        else:
            print(arr2[j], sep=' ')
            j = next_distinct(arr2, j)
            i = next_distinct(arr1, i)

    while i < m:
        print(arr1[i], sep=' ')
        i += 1

    while j < n:
        print(arr2[j], sep=' ')
        j += 1

arr1 = [1, 3, 3, 5, 5]
arr2  = [2, 3, 3, 6]
union(arr1, arr2, 5, 4)

# Time Complexity:O(m+n), where m & n are the sizes of the arrays.
# Auxiliary Space: O(1)
           
