'''Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.'''

def find_difference(nums1: list, nums2: list):
    return [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]

#another approach

def find_difference2(nums1: list, nums2: list):
    only_nums1 = set()
    exists_nums2 = set()

    for num in nums2:
        exists_nums2.add(num)

    for num in nums1:
        if num not in exists_nums2:
            only_nums1.add(num)
    ans1 = list(only_nums1)
    only_nums1 = set()
    exists_nums2 = set()
    for num in nums1:
        exists_nums2.add(num)

    for num in nums2:
        if num not in exists_nums2:
            only_nums1.add(num)
    ans2 = list(only_nums1)  

    return [ans1, ans2]
    

nums1 = [1,2,3,3]
nums2 = [1,1,2,2]

res = find_difference2(nums1, nums2)
print(res)