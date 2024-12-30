'''A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.'''

def peak_element(nums: list):
    l = 0   
    r = len(nums) - 1

    while l <= r:
        m = (l+r)//2
        if nums[m] > nums[m+1]:
            return m
        elif nums[m] < nums[r]:
            r = m - 1
        elif nums[m] > nums[l]:
            l = m + 1
    


nums = [1,2,3,4,3,6]

print(peak_element(nums))