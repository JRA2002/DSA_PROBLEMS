'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''

def product_except_self(nums: list):
    bef = 1
    aft = 1
    n = len(nums)
    ans = [0] * n

    
    ans[0] = bef
    for i in range(1, n):
        bef *= nums[i-1]
        ans[i] = bef 
    
    ans[n-1] = aft * ans[n-1] 
    
    for i in range(n-2, -1, -1):
        aft *= nums[i+1]
        ans[i] = aft * ans[i]

    return ans
        

nums = [1,2,3,4]

print(product_except_self(nums))