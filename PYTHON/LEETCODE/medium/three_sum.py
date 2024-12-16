'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''

def find_sum(nums: list):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
             continue
        l = i + 1
        r  = len(nums) - 1
        while l < r :
                suma = nums[i] + nums[l] + nums[r]
                if suma > 0:
                    r -= 1
                elif suma < 0:
                    l += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1  
    return  res

nums = [-2,0,0,2,2]
res = find_sum(nums)
print(res)
