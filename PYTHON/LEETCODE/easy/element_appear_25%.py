'''Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.'''
from collections import Counter
import math
def find_special_integer(arr: list):
    n = len(arr)
    
    if n == 1:
        return arr[0]
    dict1 = Counter(arr)
    
    for k,v in dict1.items():
        if v > n//4:
            return k
        
#  optimal approach

def find_special_integer2(arr: list):
    size = len(arr)//4
    for i in range(len(arr)-size):
        if arr[i] == arr[i+size]:
            return arr[i]
    return -1

arr = [1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]

res = find_special_integer2(arr)
print(res)