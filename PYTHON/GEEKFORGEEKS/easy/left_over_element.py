'''Given an array arr, the size is reduced by 1 element at each 
step. In the first step, the maximum element would be removed, 
while in the second step, the minimum element of the remaining 
array would be removed, in the third step again the maximum,
 and so on. Continue this till the array contains only one 
 element. And find the final element remaining in the array.'''



def leftElement(arr) -> int:
        # code here
        arr.sort()
        i = 0
        j = len(arr) - 1
       
        
        while i <= j:
            if i == j:
                return arr[0]
            else:
                arr.pop(j)
                j -= 1
            if i == j:
                return arr[0]
            else:
                arr.pop(i)
                j -= 1
                
        
#optimal approach

def find_left_over2(arr: list):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return arr[n//2 - 1]
    else:
        return arr[n//2]

   
arr = [8, 1, 2, 9, 4, 3, 7, 5]
res = find_left_over2(arr)
print(res)