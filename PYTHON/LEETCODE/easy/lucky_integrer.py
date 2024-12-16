'''Given an array of integers arr, a lucky integer is an 
integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there 
is no lucky integer return -1.'''

def find_lucky(arr):
    dict1 = {}
    for num in arr:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    maxi = 0
    for key in dict1:
        if key == dict1[key] and key > maxi:
            maxi = key
    if maxi > 0:
        return maxi
    return -1
    

arr = [1,2,2,3,3,3]
res = find_lucky(arr)
print(res)