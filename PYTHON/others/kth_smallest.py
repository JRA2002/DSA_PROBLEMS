'''Given an array arr[] of N distinct elements and a number K, 
where K is smaller than the size of the array. Find the Kth 
smallest element in the given array.'''


def kth_smallest(nums, k): 
    k = k - 1

    def quickselect(left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]
        if p > k:
            return quickselect(left, p - 1)
        elif p < k:
            return quickselect(p + 1, right)
        else:
            return nums[p]
        
    return quickselect(0, len(nums) - 1)

arr = [10, 20, 15, 2, 23, 90, 67]
start  = 0
end  = len(arr) - 1
res = kth_smallest(arr, 3)
print(res)