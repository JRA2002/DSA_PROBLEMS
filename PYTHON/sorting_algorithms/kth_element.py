'''Kth Largest Element in an Array - Quick Select Algorithm'''

def find_kthelement(nums: list, k: int):
    k = k - 1

    def quickselect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        if p > k:
            return quickselect(left, p - 1)
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return nums[p]
        
    return quickselect(0, len(nums) - 1)

nums = [4,1,8,2,9,5]
res = find_kthelement(nums, 2)
print(res)
print(nums)

        
