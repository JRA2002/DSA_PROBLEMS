'''An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.'''

def is_monotic(nums: list):
    if nums[0] < nums[-1]:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                return False
        return True
    for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                return False
    return True

nums = [1,3,2]

res = is_monotic(nums)
print(res)