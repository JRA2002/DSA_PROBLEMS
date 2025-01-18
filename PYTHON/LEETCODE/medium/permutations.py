'''Given an array nums of distinct integers, return all the possible 
permutations
. You can return the answer in any order.'''

def permute(nums: list):
    ans = []
    aux = []

    def backtrack():
        if len(aux) == len(nums):
            ans.append(aux[:])
            return
        
        for num in nums:
            if num not in aux:
                aux.append(num)
                backtrack()
                aux.pop()

    backtrack()

    return ans

nums = [1,2,3]






