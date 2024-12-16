''''Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.'''

def find_closest_number(nums: list):
        mini = abs(nums[0])
        old = nums[0]
        for i in range(len(nums)):
            if abs(nums[i]) < mini:
                mini = abs(nums[i])
                old = nums[i]
                
            if abs(nums[i]) == mini and nums[i] > old:
                mini = nums[i]
                old = nums[i]

        return old    


nums = [-4,-2,-1,1,8]

res = find_closest_number(nums)
print(res)