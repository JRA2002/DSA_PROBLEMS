'''Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.'''
def permutations(nums):
    result = []
    # base case
    if len(nums) == 1:
        return [nums[:]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        perms = permutations(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        
        print(nums)
        nums.append(n)
        print(nums)

nums = {3:1, 2:2, 1:3}
res = max(nums)
print(res)
    