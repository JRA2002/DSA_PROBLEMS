'''Given an array of integers of size N, the task is to find the first non-repeating element in this array. '''

from collections import defaultdict
def non_repeating(arr: list):
    dict1 = defaultdict(int)
    for i in arr:
        if dict1[i]:
            dict1[i] += 1
        else:
            dict1[i] = 1
            
    for i in arr:
        if dict1[i] == 1:
            print(i)
            break
    
    
arr = [9, 4, 9, 6, 7, 4]
non_repeating(arr)