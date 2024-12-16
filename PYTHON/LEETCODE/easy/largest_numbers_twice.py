'''You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.'''

def largest_number(nums: list):
    maxi = [0,0]
    for i in range(len(nums)):
        if nums[i] > maxi[0]:
            maxi[0] = nums[i]
            maxi[1] = i
    nums.remove(maxi[0])
    new_maxi = max(nums)
    if maxi[0]//2 >= new_maxi:
        return maxi[1]
    return -1

nums = [1,2,3,4]

res = largest_number(nums)
print(res)