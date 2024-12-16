'''Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that is 
missing from the array.'''

def missing_number(nums):
    n = len(nums)
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
        print(ans)
    print('------')
    for num in nums:
        ans ^= num
        print(ans)
nums = [0,1,2,3,4]
missing_number(nums)