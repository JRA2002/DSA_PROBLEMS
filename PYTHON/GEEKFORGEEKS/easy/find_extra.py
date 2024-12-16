'''You have given two sorted arrays arr1[] & arr2[] of distinct 
elements. The first array has one element extra added in between.
 Return the index of the extra element.

Note: 0-based indexing is followed.'''

def find_index(n, a, b):
    for i in range(n):
        if arr1[i] not in b:
            return i
    return -1


# optimal approach

def find_index1(n, a, b):
    suma1 = sum(arr1)
    suma2 = sum(arr2)

    num = suma1 - suma2
    for i in range((n)):
        if arr1[i] == num:
            return i
    return -1


arr1 = [2,4,6,8,9,10,12]
n = len(arr1)
arr2 = [2,4,6,8,10,12]

res = find_index(n, arr1, arr2)
print(res)