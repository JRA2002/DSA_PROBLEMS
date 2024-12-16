'''You are given an array arr[] of positive integers. Your task is to find the maximum value that can be obtained by performing a bitwise AND operation on any two different elements in the array.
Note: AND refers to the bitwise '&' operator.'''

def maxi_and(arr: list):
    maxi = max(arr)
    return maxi

arr = [3,1,1,8,1,9,3,9,8,4]

res = maxi_and(arr)
print(res)