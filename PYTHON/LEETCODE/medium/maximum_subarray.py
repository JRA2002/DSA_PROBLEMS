'''Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.'''

def maximum_subarray(nums: list):
    
    maxA = nums[0]
    suma = 0
  
    for i in range(len(nums)):
        suma = suma + nums[i]
        if suma > maxA:
            maxA = suma
       
        if suma <= 0:
            suma = 0
           
    return maxA

nums = [-2,1,-3,4,-1,2,1,-5,4]

print(maximum_subarray(nums))