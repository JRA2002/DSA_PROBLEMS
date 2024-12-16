'''The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums. 

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.'''

def xor_subset(arr):
    res = 0
    for i in range(len(arr)):
        res = res ^ (arr[i])
        print(res)
    return res
# pendiente
def xor_subset_totals(nums):
    suma = sum(nums)
    k = 2
    while k <= len(nums):
        for i in range(len(nums) - k + 1):
            new = nums[i:k+i]
            res = xor_subset(new)
            
            suma += res
        k += 1
    
    return suma

nums = [3,4,5,6,7,8]
res = xor_subset(nums)
print(res)