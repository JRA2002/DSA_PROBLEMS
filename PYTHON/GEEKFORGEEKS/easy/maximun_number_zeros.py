'''Given an array arr[] of integers, the task is to find the number that has the maximum number of zeroes. If there are no zeroes then print -1.

Note: If there are multiple numbers with the same (max) number of zeroes then print the Maximum number among them.'''

def max_zeros(arr: list):
    hashmap = {}
    for num in arr:
        count = 0
        temp = num
        while num % 10 == 0:
            count += 1
            num = num // 10
        hashmap[temp] = count
    maxi = 0
    maxi_num = -1
    for k,v in hashmap.items():
        if v > maxi:
            maxi = v
            maxi_num = k
        elif maxi == v and k > maxi_num and v != 0:
            maxi_num = k
            maxi = v
    
    return maxi_num
    

arr = [12,3,4]

res = max_zeros(arr)
print(res)

