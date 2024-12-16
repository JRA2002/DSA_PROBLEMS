'''Given an array nums of integers, return how many of them contain an even number of digits.'''


def find_numbers(nums: list):
    count = 0
    for num in nums:
        pair = 0
        while num >= 10:
            pair += 1
            num = num // 10
        if pair%2 != 0:
            count += 1
    return count

def find_numbers2(nums: list):
    count = 0
    for num in nums:
        if (num >=10 and num <= 99) or (num >=1000 and num <= 9999) or num == 100000:
            count += 1
    return count

nums = [11,1,10]
res = find_numbers2(nums)
print(res)