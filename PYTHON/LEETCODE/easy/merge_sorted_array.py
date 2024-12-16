'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.'''

def merge_sorted_array(nums1: list, m, nums2: list, n):
    
    if m == 0:
        nums1 = nums2
    else:
        nums0 = nums1[:m]
        i = 0
        j = 0
        k = 0
        print(nums0,nums2)
        while i < m and j < n:
            if nums2[j] >= nums0[i]:
                nums1[k] = nums0[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
            
        while i < m:
            nums1[k] = nums0[i]
            k += 1
            i += 1

        while j < n:
            nums1[k] = nums2[j]
            k += 1
            j += 1
    print(nums1)

nums1 = [2,0]
m = 1
nums2 = [1]
n = len(nums2)

res = merge_sorted_array(nums1, m, nums2, n)
print(res)

def plus_one(digits: list):
        n = len(digits) - 1
        k = 1
        for i in range(n,-1,-1):
            k, digits[i] = divmod(digits[i]+k, 10)
        
        if k > 0:
            digits = [k] + digits
        return digits
