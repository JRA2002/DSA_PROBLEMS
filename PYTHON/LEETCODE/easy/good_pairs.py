'''You are given 2 integer arrays nums1 and nums2 of lengths 
n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible 
by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.'''

def good_pairs(nums1, nums2, k):
    count = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] % (nums2[j] * k) == 0:
                count += 1

    return count

nums1 = [1,2,4,12]
nums2 = [2,4]
res = good_pairs(nums1, nums2, 3)
print(res)