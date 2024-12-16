'''You are given an integer array nums consisting of n elements, 
and an integer k.

Find a contiguous subarray whose length is equal to k that has 
the maximum average value and return this value. Any answer with 
a calculation error less than 10-5 will be accepted.'''

def maximum_average(nums: list, k):
    
    cur_sum = sum(nums[:k])
    
    max_sum = cur_sum

    for i in range(len(nums) - k):
        l = nums[i]
        r = nums[k+i]
        
        cur_sum = cur_sum - l + r
       
        if cur_sum > max_sum:
            max_sum = cur_sum

    return max_sum/k

nums = [6]
k = 1
res = maximum_average(nums, k)
print(res)