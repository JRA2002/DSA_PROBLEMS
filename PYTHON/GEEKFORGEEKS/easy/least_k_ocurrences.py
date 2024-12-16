'''Given an array arr. Return the element that occurs at least k number of times.

Note:

If there are multiple answers, please return the first one.
If there is no element found, return -1.'''

def least_k_ocurrences(arr: list, k: int):
    dict1 = {}

    for num in arr:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num] += 1
        if dict1[num] == k:
            return num
        
    return -1
    
    

arr = [993,432,758,467,424,434,457,349,417,177,580,771,396,486,268,151,210,417,119,871,169,134,232]
k = 21

res = least_k_ocurrences(arr, k)
print(res)


