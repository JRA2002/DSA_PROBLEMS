'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''

def shuffle(nums, n):
    i = 0
    j = n
    nums1 = []
    while i < n and j < 2*n:

        print(nums[i])
        print(nums[j])
        nums1.append(nums[i])
        nums1.append(nums[j])
        i += 1
        j += 1
    return nums1
nums = [2,5,1,3,4,7]
res = shuffle(nums, len(nums) // 2)
print(res)

# Time Complexity:O(N)
# Auxiliary Space: O(N)
