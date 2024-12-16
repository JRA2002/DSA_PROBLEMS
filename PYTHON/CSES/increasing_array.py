n = int(input())
nums = list(map(int, input().split()))

count = 0
i = 0
while i < len(nums) - 1:
    if nums[i] > nums[i+1]:
        count += nums[i] - nums[i+1]
        nums[i+1] = nums[i]
    i += 1
print(count)