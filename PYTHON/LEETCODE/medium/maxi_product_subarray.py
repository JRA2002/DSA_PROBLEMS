'''Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.'''

def maximum_prod_subarray(nums: list):
    curMax = 1
    curMin = 1
    res = max(nums)

    for num in nums:

        temp = num * curMax
        curMax = max(num * curMax, num, curMin * num)
        curMin = min(temp, num, curMin * num)

        res = max(res, curMax)
    
    return res

nums = [2,3,0,4]

print(maximum_prod_subarray(nums))