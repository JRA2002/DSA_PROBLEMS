'''Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.'''

def find_min(nums: list):
    n = len(nums)
    i = 0
    j = n - 1
    if nums[0] < nums[n-1] or n == 1:
        return nums[0]
    while i <= j:
        m = (i+j)//2
      
        if nums[m+1] < nums[m]:
            return nums[m+1]
        elif nums[m-1] > nums[m]:
            return nums[m]
        elif nums[i] < nums[m]:
            i = m + 1
        else:
            j = m - 1
    
    

nums = [11,13,15,17]

res = find_min(nums)
print(res)