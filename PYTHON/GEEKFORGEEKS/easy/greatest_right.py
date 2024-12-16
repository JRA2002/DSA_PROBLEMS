'''You are given an array arr. Replace every element with the next
 greatest element (the greatest element on its right side) in the 
 array. Note: There is no element next to the last element, so replace it with -1.'''

def next_greatest(arr):
    
        i = 0
        n = len(arr)
        while i < n:
            if i == n - 1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
            i += 1
        return arr
    

# optimal approach

def next_greatest1(arr):
    
        n = len(arr) - 1
        maxi = -1
        
        while n >= 0:
            if arr[n] > maxi:
                maxi = arr[n]
            arr[n] = maxi
            n -= 1
            
        arr.append(-1)
        arr.pop(0)
    
        return arr
        
arr = [16, 17 ,4, 3, 5, 2]      
res = next_greatest(arr)
print(res)