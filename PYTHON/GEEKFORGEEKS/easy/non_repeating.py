'''Find the first non-repeating element in a given array 
arr of integers and if there is not present any non-repeating 
element then return 0

Note: The array consists of only positive and negative
 integers and not zero.'''

def find_non(arr):
    dict1 = {}
    res = []
    for num in arr:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    
    for k,v in dict1.items():
        if v == 1:
            res.append(k)
            
    for num in arr:
        if num in res:
            return num
    return 0
arr = [4, -8, 1, -4, -3, -8, -3, -10, 3, -3, 10]
res = find_non(arr)
print(res)