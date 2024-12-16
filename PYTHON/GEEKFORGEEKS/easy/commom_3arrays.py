'''You are given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
If there are no such elements return an empty array. In this case, the output will be -1.

Note: can you handle the duplicates without using any additional Data Structure?'''

def commom_elements(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)

    res = []

    for i in set1:
        if i in set2 and i in set3:
            res.append(i)
    if res:
        return res
    return -1

arr1 = [1,4, 5,6,7,8,9] 
arr2 = [2,3,6, 7,10,11] 
arr3 = [3, 4,6,7,13]

res = min(1,2,1)
print(res)


        