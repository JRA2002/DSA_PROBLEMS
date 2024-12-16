'''Given two sorted arrays having some elements in common. 
Find the sum of the maximum sum path to reach from the 
beginning of any array to the end of any of the two arrays. 
We can switch from one array to another array only at common elements. 

Note: The common elements do not have to be at the same indexes. 
And individual arrays have distinct elements only (no repetition 
within the array).'''

def sum_paths(arr1, arr2):
    sum1 = 0
    num = 0
    for i in arr2:
        if i in arr1:
            num = i
            break
        sum1 = sum1 + i
    print(sum1)
    index = 0
    for i in range(len(arr1)):
        if arr1[i] == num:
            index = i
            break
    print(sum(arr1[index:]))
    result = sum(arr1[index:]) + sum1
    return result

arr1 = [2, 3, 7, 10, 12, 15, 30, 34]
arr2 = [1, 5, 7, 8, 10, 15, 16, 19]
res = sum_paths(arr1, arr2)
print(res)