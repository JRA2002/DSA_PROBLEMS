'''Given two arrays arr1[] and arr2[] of size m and n respectively, 
the task is to determine whether arr2[] is a subset of arr1[].
 Both arrays are not sorted, and elements are distinct.'''

def subset_array(arr1, arr2):
    if len(arr2) < len(arr1):
        for i in arr2:
            if i in arr1:
                continue
            else:
                return False
    else:
        for i in arr1:
                if i in arr2:
                    continue
                else:
                    return False
    return True

    
arr1 = [10, 5, 2, 23, 19]
arr2 = [19, 5, 3]
res =  subset_array(arr1, arr2)
print(res)

# Time Complexity: O(N)
# Auxiliary Space: O(1)