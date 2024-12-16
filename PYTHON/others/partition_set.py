'''The partition problem is to determine whether a given 
set can be partitioned into two subsets such that the sum 
of elements in both subsets is the same. '''

def exist_num(arr):
    suma = 0
    for i in range(len(arr)):
        suma += arr[i]
    
    if suma / 2 in arr:
        
        return True
    else:
        return False
    

arr = [1, 5, 3]
res = exist_num(arr)
print(res)