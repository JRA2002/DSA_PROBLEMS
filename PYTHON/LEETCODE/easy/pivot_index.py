'''Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly 
to the left of the index is equal to the sum of all the numbers strictly 
to the index's right.

If the index is on the left edge of the array, then the left sum is 0 
because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.'''

def pivot_index(nums):
    sl = 0
    sr = sum(nums)
    n = len(nums) - 1
    for i in range(len(nums)):
        if i == 0:
            sl = 0
        else:
            sl = sl + nums[i-1]

        if i == n:
            sr = 0
        else:
            sr = sr - nums[i]

        if sl == sr:
            return i+1
    return -1


nums = [1,3,5,2,2]
res = pivot_index(nums)
print(res)