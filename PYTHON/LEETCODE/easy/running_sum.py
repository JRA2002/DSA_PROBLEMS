'''Given an array nums. We define a running sum of 
an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.'''

def running_sum(nums):
    # start with 1 because we want to add the previous number
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums

nums = [3,2,3,4]
res = running_sum(nums)
print(res)