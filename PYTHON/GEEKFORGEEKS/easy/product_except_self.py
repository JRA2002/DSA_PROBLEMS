'''Given an array nums[], construct a Product Array nums[] 
such that nums[i] is equal to the product of all the elements 
of nums except nums[i].'''
# brute force approach

def product_except_self(nums):
    res = []
    prod = 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j:
                prod = nums[j] * prod
        res.append(prod)
        prod = 1
    return res

# optimal solution
def product_except_self1(nums: list):
    res = []
    prod = 1
    zeros = nums.count(0)
    if zeros > 1:
        return [0] * len(nums)
    for i in nums:
        if i != 0:
            prod = prod * i
    for i in nums:
        item = prod // i
        print(item)
        res.append(item)
    return res
nums = [12,0]
res = product_except_self1(nums)
print(res)