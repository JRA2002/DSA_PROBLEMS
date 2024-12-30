'''Given two integer arrays nums1 and nums2, return an array of their 
intersection
. Each element in the result must be unique and you may return the result in any order.'''

def intersection(nums1: list, nums2: list):
    set1 = set(nums1)
    return list(set1.intersection(set(nums2)))

nums1 = [1,2,2,1]
nums2 = [2,2]

print(intersection(nums1, nums2))
