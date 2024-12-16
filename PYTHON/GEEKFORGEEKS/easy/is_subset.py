'''Given two arrays: a1[0..n-1] of size n and a2[0..m-1] 
of size m, where both arrays may contain duplicate elements.
The task is to determine whether array a2 is a subset of
array a1. It's important to note that both arrays can be
sorted or unsorted. Additionally, each occurrence of a
duplicate element within an array is considered as a 
separate element of the set'''

def is_subset(a1 : list, a2:list, n ,m):
    #User function Template for python3

    hasht = {}
    for i in range(n):
        if a1[i] in hasht:
            hasht[a1[i]] += 1
        else:
            hasht[a1[i]] = 1
    for i in a2:    
        if i in hasht:
            if hasht[i] == 0:
                return False
            hasht[i] -= 1
        else:
            return False
    return True
    
a1 = [1,2,2,5,6,7,8,8,8]
a2 = [1,2,2,5,8,8,8,8]
n = len(a1)
m = len(a2)
res = is_subset(a1, a2, n,m)
print(res)
