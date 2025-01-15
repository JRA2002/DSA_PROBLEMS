'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.'''

def contain_nearby_duplicates(nums: list, k: int):
    mapa = {}

    for i in range(len(nums)):
        if nums[i] not in mapa:
            mapa[nums[i]] = i
        else:
            if i - mapa[nums[i]] <= k:
                return True
            else:
                mapa[nums[i]] = i
    return False

nums = [1,2,3,1,2,3]
k = 2

print(contain_nearby_duplicates(nums, k))