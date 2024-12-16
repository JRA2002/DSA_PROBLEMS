'''Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.'''


def find_kth_positive(arr: list, k: int):
    maxi = arr[-1]
    for i in range(1,maxi):
        if i not in arr:
            k -= 1
        if k == 0:
            return i
    if k != 0:
        return maxi+k
    
# optimal solution

def find_kth_positive2(arr: list, k: int):
    left = 0
    right = len(arr)
    while left < right:
        midd = (left+right)//2
        if arr[midd] - midd - 1 < k:
            left = midd + 1
        else:
            right = midd
    return right + k
        


arr = [1,2,3,4]
k = 2

res = find_kth_positive2(arr, k)
print(res)