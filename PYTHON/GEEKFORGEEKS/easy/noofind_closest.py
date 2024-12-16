'''Given a sorted array arr[] of positive integers.
 The task is to find the closest value in the array 
 to the given number k. The array may contain duplicate values.

Note: If the difference with k is the same for two values 
in the array return the greater value.'''

def find_closest(n, k, arr):
    i = 1
    
    while i < (k):
        a = k - i
        b = k + i
       
        if a not in arr and b not in arr:
            i += 1
  
        elif a in arr and b in arr:
            return max(a,b)
        elif a in arr:
            return a
        else: 
            return b


    
k = 7
arr = [1, 3, 3, 3, 4, 6, 7, 9, 9, 9, 12, 19]
n =  len(arr)

res = find_closest(n, k, arr)
print(res)