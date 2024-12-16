'''Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then return the maximum of pos and neg.
Note that 0 is neither positive nor negative.'''

def maximum_count2(nums: list):
    i = 0
    n = len(nums)
    j = n - 1
    pos = n
    if nums[0] == 0 and nums[j] == 0:
        return 0
    if n == 1:
        return 1
    
    while i <= j:
        m = (i + j) // 2
       
        if nums[m] > 0 and (nums[m-1] <= 0 or m == 0):
            pos = m
            break
        elif nums[m] > 0 and nums[m-1] > 0:
            j = m - 1
        else:
            i = m + 1

    i = 0
    j = n - 1
    neg = -1
    while i <= j:
        m = (i + j) // 2
        
        if nums[m] < 0 and (m == n - 1 or nums[m+1] >= 0):
            neg = m
            break
        elif nums[m] < 0 and nums[m+1] < 0:
            i = m + 1
        else:
            j = m - 1
    
    return max(neg+1,n-pos)

nums = [1,2,3]

res = maximum_count2(nums)
print(res)