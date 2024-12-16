'''Given two unsorted arrays arr1[]  and arr2[], the task is to find all pairs whose sum equals x from both arrays.

Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.'''

def all_pairs(target, arr1: list, arr2: list):
    hashmap = {}
    ans = []
    
    for num in arr1:
        if num not in hashmap:
            hashmap[num] = 1
        else:
            hashmap[num] += 1
    print(hashmap)
    arr2.sort(reverse=True)
    for num in arr2:
        if (target - num) in hashmap:
            ans.append((target-num, num))
            while hashmap[target-num] != 1:
                ans.append((target-num, num))
                hashmap[target-num] -= 1
             
    return ans

    w

target = 9
arr1 = [1, 2, 4, 5, 7, 4]
arr2 = [5, 6, 3, 4, 8, 4]

res = all_pairs(target, arr1, arr2)
print(res)