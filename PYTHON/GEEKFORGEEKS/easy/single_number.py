'''Given an array arr[] of positive integers where every element appears even times except for one. Find that number occurring an odd number of times.'''

def single_number(arr: list):
    hmap = {}

    for num in arr:
        if num not in hmap:
            hmap[num] = 1
        else:
            hmap[num] += 1
    for k,v in hmap.items():
        if v%2 != 0:
            return k
   
# better approach
# using bit manipulation

def single_number2(arr: list):
    xor = 0
    for num in arr:
        xor = xor ^ num
    return xor

# optimal approach
arr = [1, 1, 2, 2, 2]
res = single_number2(arr)
print(res)