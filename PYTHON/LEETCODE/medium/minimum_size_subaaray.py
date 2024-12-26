'''Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

def min_length(target: int , nums: list):
    minL = len(nums) + 1
    l = 0
    r = 0
    suma = 0
    while l <= len(nums) - 1 and l <= r and r <= len(nums) - 1:
        
        if suma < target:
            r += 1
        else:
            minL = min(minL, r-l+1)
            suma = suma - nums[l] + nums[r]
            l += 1
        print(nums[l], nums[r])

    return minL

target = 7
nums = [2,3,1,2,4,3]

print(min_length(target, nums))