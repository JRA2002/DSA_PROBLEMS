'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''

def sorted_squares(nums: list):
    n = len(nums)
    for i in range(n):
        nums[i] = nums[i]*nums[i]
    nums.sort()
    return nums

nums = [-4,-1,0,3,10]

# optimal approach

def sorted_squares2(nums: list):
    n = len(nums)
    res = []
    
    i = 0
    j = n - 1
    while i <= j:
        if nums[i]*nums[i] > nums[j]*nums[j]:
            res.append(nums[i]*nums[i])
            i += 1
        else:
            res.append(nums[j]*nums[j])
            j -= 1
        
    return res[::-1]
res = sorted_squares2(nums)
print(res)
