'''Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.'''

def rotate_array(nums: list, k: int):
    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    k = k % len(nums)

    reverse(0, len(nums) - 1)
    reverse(0,k - 1)
    reverse(k, len(nums) - 1)
    
    return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate_array(nums, k))