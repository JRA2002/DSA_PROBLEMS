'''Given an array of integers nums which is sorted in ascending 
order, and an integer target, write a function to search target 
in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.'''

def binary_search(nums, target):
    i = 0
    j = len(nums) - 1
    while i  < j:
        midd = (i+j)//2
        if nums[midd] == target:
            return midd
        if nums[midd] > target:
            j = midd - 1
        else:
            i = midd + 1
    return -1

nums = [-1,0,3,5,9,12]
res = binary_search(nums, 9)
print(res)        