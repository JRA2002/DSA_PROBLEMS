'''Given an unsorted array arr[] of integers and a key which is
 present in this array. You need to write a program to find the 
 start index( index where the element is first found from left 
 in the array ) and end index( index where the element is first 
 found from right in the array ) return an array of length 2 with
   elements start index and end index.(0 based indexing is used)

If the key does not exist in the array then return -1 for both 
start and end index in this case.'''

def find_index(arr, key):
    res = []
    for i in range(len(arr)):
        if arr[i] == key:
            res.append(i)
    if len(res) == 1:
        res = res*2
        return res
    elif len(res) > 1:
        return [res[0],res[-1]]
    else:
        return [-1,-1]
    
arr = [7,8,2,3,8,4,1,8,6] 
key = 8

res = find_index(arr, key)
print(res)