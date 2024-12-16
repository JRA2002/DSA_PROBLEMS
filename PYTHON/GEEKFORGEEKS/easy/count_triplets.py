'''Given an array Arr consisting of N distinct integers. 
The task is to count all the triplets such that sum of 
two elements equals the third element.'''

def count_triplets(arr : list, n):
    arr.sort()

    i = 0
    k = n - 1
    j = k - 1
    
    count = 0
    while k > 0:
        while i < j:
            if arr[i] + arr[j] == arr[k]:
                count += 1
                i += 1
                j -= 1
            elif arr[i] + arr[j] > arr[k]:
                j -= 1
            else:
                i += 1
        k -= 1
        i = 0
        j = k - 1
        
    return count

arr = [1, 5, 3, 2, 4]
n = len(arr)
res = count_triplets(arr, n)
print(res)