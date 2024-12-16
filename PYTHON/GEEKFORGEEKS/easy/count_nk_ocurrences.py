'''Given an array arr of size N and an element k. The 
task is to find the count of elements in the array 
that appear more than n/k times.'''

def count_occurences(arr, n, k):
    dict1 = {}
    for num in arr:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    count = 0
    for i,v in dict1.items():
        if v > n/k:
            count += 1

    return count
    

arr = [3,1,2,2,1,2,3,3]
n = len(arr)
k = 4

res = count_occurences(arr, n, k)
print(res)