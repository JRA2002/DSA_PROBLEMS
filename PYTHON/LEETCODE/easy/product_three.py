'''Given an integer array nums, find three numbers whose product is maximum and return the maximum product.'''

def maximum_product(nums):
    k = 3

    while k <= len(nums):
        for i in range(len(nums) - k + 1):
            new = nums[i:k+i]


nums = [-1,-2,-3,-4]
res = maximum_product(nums)
print(res)