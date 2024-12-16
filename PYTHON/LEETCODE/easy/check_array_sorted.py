'''Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.'''

def check_array(nums: list):
    original = nums.copy()
    original.sort()
    n = len(nums)
    print(original,nums)
    for x in range(n):
        if original[x%n] == nums[0]:
            print(original[x%n])
            return True
    return False


nums = [2,1,3,4]
res = check_array(nums)
print(res)
