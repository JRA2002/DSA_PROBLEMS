'''You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.'''

def difference_sum(nums):
        sumaE = sum(nums)
        sumaD = 0
        for num in nums:
            if num > 9:
                while num != 0:
                    res = num % 10
                    sumaD += res
                    num = num // 10
            else:
                sumaD += num
        result = abs(sumaE - sumaD)
        return result

nums = [1,15,6,3]
res = difference_sum(nums)
print(res)