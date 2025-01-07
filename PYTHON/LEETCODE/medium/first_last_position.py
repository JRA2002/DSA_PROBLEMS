'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''

def search_range(nums: list, target: int):
    l = 0
    r = len(nums) - 1
    s = -1
    e = -1

    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            temp = m
            if m > 0 and nums[m-1] == target:
                while m >= 0 and nums[m] == target:
                    m -= 1
                s = m + 1
            else:
                s = m

            if temp + 1 < len(nums) and nums[temp+1] == target:
                while temp < len(nums) and nums[temp] == target:
                    temp += 1
                e = temp - 1
            else:
                e = temp

            return [s, e]
        elif nums[m] > target:
            r -= 1
        else:
            l += 1
    
    return [s,e]

nums = [8,8,8,8]
target = 8

print(search_range(nums, target))