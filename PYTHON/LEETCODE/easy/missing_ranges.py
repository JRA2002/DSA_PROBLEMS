"Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges."

def find_ranges(nums: list, lower, upper):
    k = 2
    n = len(nums)
    if n == 0:
        return [[lower,upper]]
    
    res = []
    if nums[0] > lower:
        res.append([lower, nums[0] - 1])
    
    for i in range(n - k + 1):
        print(nums[i+1])
        if nums[i]+1 == nums[k+i-1]:
            continue

        if nums[k+i-1]-1 == nums[i]:
            continue
        else:
            if nums[i]+1 != nums[k+i-1]-1:
                res.append([nums[i]+1,nums[k+i-1]-1])
            else:
                res.append([nums[i]+1])
                
    if nums[-1] < upper:
        res.append([nums[-1]+1, upper])
        
    print(res)

nums = [3,7,67]
lower = 0
upper = 99
res = find_ranges(nums, lower, upper)
print(res)