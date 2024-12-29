'''You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1. The array can have negative integers too.'''

def missing_number(arr: list):
    res = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        if arr[i] >= 0 and arr[i] < len(res):
            res[arr[i]] = 1 

    for i in range(1, len(res)):
        if res[i] == 0:
            return i
        
    return i + 1

arr = [1,2,3,4]

print(missing_number(arr))