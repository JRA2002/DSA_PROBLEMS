'''Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) 
where 0 <= i < j < n, such that nums[i] == nums[j] and (i * j) is divisible by k.'''

def count_pairs(nums: list, k: int):
    n = len(nums)
    r = 2
    count = 0
    while r <= n:
        for i in range(n - r + 1):
            if nums[i] == nums[i+r-1] and i*(i+r-1) % k == 0 and i < i+r-1:
                count += 1
                print((i,i+r-1))
        r += 1
    return count


nums = [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3]
k = 7

res = count_pairs(nums, k)
print(res)