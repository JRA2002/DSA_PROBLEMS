'''Given an array of integers, find the length of the longest 
sub-sequence such that elements in the subsequence are 
consecutive integers, the consecutive numbers can be in any order.'''

def longest_sub(arr: list):
    arr.sort()
    n = len(arr)//2
    count = 1
    for i in range(len(arr) - 1):
        if arr[i]+1 == arr[i+1]:
            count += 1
        
    return count

arr = [1, 9, 3, 10, 4, 20, 2]
res = longest_sub(arr)
print(res)