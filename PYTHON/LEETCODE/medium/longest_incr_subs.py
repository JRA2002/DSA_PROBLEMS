'''Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.'''

def lengthOfLIS(nums: list):
    dp = [1] * len(nums)
  

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], 1+dp[j])
    return dp[0]

nums = [0,1,0,3,2,3]

print(lengthOfLIS(nums))