'''Given an integer array nums, return true if any value 
appears at least twice in the array, and return false if 
every element is distinct.'''
from collections import defaultdict

#using hashmap
def contain_duplicates(nums):
    hashm = defaultdict(int)
    for num in nums:
        if num in hashm:
            hashm[num] += 1
        else:
            hashm[num] = 1

    for k,v in hashm.items():
        if v > 1:
            return True
    return False
    
# using sorting
def contain_duplicates_sort(nums: list):
    nums.sort()
    res = False
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return res

nums = [1,2,31,1,2]
res = contain_duplicates_sort(nums)
print(res)