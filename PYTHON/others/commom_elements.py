'''Given three sorted arrays in non-decreasing order, print all common elements in these arrays.

Note: In case of duplicate common elements, print only once.'''

def commom_elements(arr1, arr2, arr3):
    for i in arr1:
        if i in arr2 and i in arr3:
            print((i))

arr1 = [1, 5, 10, 20, 30]
arr2 = [5, 13, 15, 20]
arr3 = [5, 20]

commom_elements(arr1, arr2, arr3)