'''Given a sorted array arr[] of size N and a number X, 
you need to find the number of occurrences of X in given array.

Note: Expected time complexity is O(log(n)) '''

def concurrence(arr, target):
    # using binary search
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        midd = (left + right) // 2
        if arr[midd] == target:
            i = midd
            j = midd
            count = 1
            while target == arr[i+1]:
                count += 1
                i += 1
            while target == arr[j-1]:
                count += 1
                j -= 1

            return count
        elif arr[midd] < target:
            left = midd + 1
        else:
            right = midd - 1
    return -1

arr = [2,4,6,6,6,12,15]
res = concurrence(arr, 6)
print(res)