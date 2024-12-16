'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the 
majority element always exists in the array.'''

# moore algorithm
def majority(nums: list):
    count = 0
    candit = 0

    for num in nums:
        if count == 0:
            candit = num
        if candit == num:
            count += 1
        else:
            count -= 1

    return candit

nums = [2,2,1,1,1,2,2]
print(majority(nums))