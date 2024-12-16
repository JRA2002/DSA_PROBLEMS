'''Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]'''

def valid_mountain_array(arr):
        i = 0
        j = len(arr) - 1
        
        while i < j :
            if arr[i] < arr[i+1]:
                i += 1
            elif arr[i] == arr[i+1]:
                 return False
            else:
                break
        if i == 0:
            return False
        if i < j:
            while i < j:
                if arr[i] > arr[i+1]:
                    i += 1
                else: 
                    return False
            return True
        else:
            return False


            
arr = [1,2,3,2,1,7,8]
res = valid_mountain_array(arr)
print(res)