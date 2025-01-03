'''You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.'''

def single_non_duplicate(nums: list):
        n = len(nums)
        if n == 1:
            return nums[0]

        l = 0
        r = n - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            elif nums[m] == nums[m+1]:
                m += 1
            else:
                m -= 1
                
            if (r-m)%2 == 0:
                r -= 2
            else:
                l -= 2


nums = [1,1,2,2,3,3,4,4,5]

print(single_non_duplicate(nums))