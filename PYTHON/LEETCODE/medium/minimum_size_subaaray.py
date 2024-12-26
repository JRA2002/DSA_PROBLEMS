'''Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.'''

def min_length(target: int , nums: list):
    minL = len(nums) + 1
    l = 0
    suma = 0
    for i in range(len(nums)):
        suma += nums[i]
        while suma >= target:
            minL = min(minL, i - l + 1)
            suma -= nums[l]
            l += 1
            
    if minL == len(nums)+1:
        return 0
    return minL

target = 7
nums = [2,3,1,2,4,3]

print(min_length(target, nums))