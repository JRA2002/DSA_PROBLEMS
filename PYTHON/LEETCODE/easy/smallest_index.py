'''Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.'''

def smallest_index(nums: list):
    n = len(nums)
    for i in range(n):
        if nums[i] == (i%10):
            return i
    return -1

nums = [4,3,2,1]

res = smallest_index(nums)
print(res)