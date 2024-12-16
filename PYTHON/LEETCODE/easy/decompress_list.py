'''We are given a list nums of integers representing a list 
compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i],
 nums[2*i+1]] (with i >= 0).  For each such pair, there are freq elements
   with value val concatenated in a sublist. Concatenate all the sublists 
   from left to right to generate the decompressed list.

Return the decompressed list.'''

def decompress_list(nums: list):
    midd = len(nums) // 2
    result = []
    for i in range(0,len(nums),2):
        res = [nums[i+2-1]] * nums[i]
        result.extend(res)
        
nums = [1,2,3,4,5,6]
res = decompress_list(nums)
print(res)