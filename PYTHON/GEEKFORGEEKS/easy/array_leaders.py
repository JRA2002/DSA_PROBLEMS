'''Given an array arr of n positive integers, your task is to 
find all the leaders in the array. An element of the array is 
considered a leader if it is greater than all the elements on 
its right side or if it is equal to the maximum element on its 
right side. The rightmost element is always a leader.'''

def leaders(n, arr):
        #Code here
        
        i = 0
        j = n
        maxi = arr[-1]
        while i < j:
                
                if arr[j - 1] >= maxi:
                        maxi = arr[j-1]
                        print(maxi)
                j -= 1
        
arr = [16 ,17, 4, 3, 5, 2]
n = len(arr)
leaders(n, arr)

# Time Complexity:O(N)
# Auxiliary Space: O(1)
