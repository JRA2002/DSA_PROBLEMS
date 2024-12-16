'''Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.'''

def subsets(nums: list):
    res = []
    subset = []

    def dfs(i):
        if len(nums) <= i:
            res.append(subset.copy())
            return

        # when agregate nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        print('yes',subset,i)
        # no aggregate nums[i]
        subset.pop()
        print('pop', subset,i)
        dfs(i + 1)
    dfs(0)
    return res

nums = [1,2,3]
res = subsets(nums)
print(res)
