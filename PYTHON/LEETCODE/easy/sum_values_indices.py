'''You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose 
corresponding indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.'''

def binary_indices(nums, k):
    def number_bits(num, k):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
                if count > k:
                    return False
            if count == k:
                return True
                
    suma = 0
    for num in range(len(nums)):
        res = number_bits(num, k)
        if res:
            suma += nums[num]
    return suma


nums = []
nums.insert(0, 0)
nums.insert(1, 2)
nums.insert(1, 5)
print(nums)