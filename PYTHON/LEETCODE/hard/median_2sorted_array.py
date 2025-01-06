'''Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).'''

def find_median_array(nums1: list[int], nums2: list[int]):
    m = len(nums1)
    n = len(nums2)
    ans = [0] * (m+n)

    i = 0
    j = 0
    k = 0

    while i < m and j < n:
        if nums1[i] < nums2[j]:
            ans[k] = nums1[i]
            i += 1
        else:
            ans[k] = nums2[j]
            j += 1
        k += 1
    # in case left array have single element
    while i < m:
        ans[k] = nums1[i]
        i += 1
        k += 1
    # in case right array have single element
    while j < n:
        ans[k] = nums2[j]
        j += 1
        k += 1

    l = 0
    r = (m+n) - 1
    m = (l+r) // 2
    
    if (m - l) == (r - m):
        return ans[m]
    elif (m - l) < (r - m):
        return (ans[m] + ans[m+1]) / 2

nums1 = [1,2]
nums2 = [3,4]

print(find_median_array(nums1, nums2))