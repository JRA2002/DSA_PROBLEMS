'''Given an integer array nums and an integer k, return the 
number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.'''
from collections import defaultdict

def absolute_difference(nums: list, k):
    dict1 = defaultdict(int)
    count = 0
    for num in nums:
        count += dict1[num-k]
        count += dict1[k-num]
        dict1[num] += 1
    return count

nums = [1,2,3,4,7,19]
k = 1
res = absolute_difference(nums, k)
print(res)