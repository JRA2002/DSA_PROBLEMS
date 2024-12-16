'''Given an array of N integers, and an integer K, the task is to find 
the number of pairs of integers in the array whose sum is equal to K.'''

def count_pairs(arr, target):
    k = 2
    count = 0
    while k <= len(arr):
        for i in range(len(arr) - k + 1):
            new = arr[i:k+i]
            a = new[0]
            b = new[-1]
            if a+b == target:
                count += 1
        k += 1
    return count


arr =  [1, 5, 7, -1, 5]
target = 6
#res = count_pairs(arr, target)
#print(res)


# count pairs with given sum using Hashing

def count_hashing(arr, target):
    count = 0
    freq = {}
    for num in arr:
        if (target - num) in freq:
            count += freq[target - num]
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return count


res = count_hashing(arr, target)
print(res)

# Time complexity: O(N) 
# Auxiliary Space: O(N)