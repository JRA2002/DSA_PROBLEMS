'''You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.'''

def target_indices(nums: list, target: int):
    nums.sort()
    res = []

    for i in range(len(nums)):
        if nums[i] == target:
            res.append(i)

    i = 0
    j = len(nums) - 1
    
    
    return res




nums = [1,2,5,2,3]
target = 2

print(target_indices(nums, target))