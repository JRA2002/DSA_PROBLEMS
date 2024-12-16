'''You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.'''

def sum_squares(nums: list):
    n = len(nums)
    res = 0
    for i in range(n):
        if n%(i+1) == 0:
            res = res + nums[i] * nums[i]
    return res
nums = [1,2,3,4]

res = sum_squares(nums)
print(res)