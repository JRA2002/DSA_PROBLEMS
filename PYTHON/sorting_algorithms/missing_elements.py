'''Given an array, arr[0..n-1] of distinct elements and a range [low, high], find all 
numbers that are in a range, but not the array. The missing elements should be printed in sorted order.'''

def missing_elements(arr: list, low, high):

    newa = []
    for i in range(low, high + 1):
        if i not in arr:
            newa.append(i)
    return newa


arr = [1, 3, 5, 4]
res = missing_elements(arr, 1, 10)
print(res)
