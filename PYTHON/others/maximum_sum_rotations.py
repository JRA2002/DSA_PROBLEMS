'''Given an array arr[] of n integers, find the maximum 
that maximizes the sum of the value of i*arr[i] where i varies from 0 to n-1.'''

def maximum_sum(arr):
    
    n = len(arr) - 1
    j = n
    maxi = 0

    while j != 0:
        temp = arr[0]
        suma = 0

        for i in range(len(arr)):
            suma += i*arr[i]
        if suma > maxi:
            maxi = suma
        for i in range(n):
            arr[i] = arr[i+1]
        arr[n] = temp
        
        j -= 1
    print(maxi)

arr = [8, 3, 1, 2]
maximum_sum(arr)

# Time complexity: O(N) 
# Auxiliary Space: O(1)

arr = [9, 9.40, 9.50, 11, 15, 18]
dep = [9.10, 12, 11.20, 11.30, 19, 20]
arr.sort()
dep.sort()

print(arr)
print(dep)

# Time complexity: O(N)
# Auxiliary Space: O(1)

