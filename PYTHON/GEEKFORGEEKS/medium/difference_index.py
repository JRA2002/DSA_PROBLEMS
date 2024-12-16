'''Given an unsorted array arr[ ] of size n, you need to find the maximum difference of 
absolute values of elements and indexes, i.e., for i <= j, calculate maximum of | arr[ i ] - arr[ j ] | + | i - j |. '''

def find_maximum(arr, n):
        max1 = arr[0]
        min1 = arr[0]
        min2 = arr[0]
        max2 = arr[0]
        for i in range(1,n):
            max1 = max(max1, arr[i] + i)
            min1 = min(min1, arr[i] + i)
            max2 = max(max2, arr[i] - i)
            min2 = min(min2, arr[i] - i)

        return max(abs(max1-min1),abs(max2-min2))
        
arr = [5,9,2,6]
n = len(arr)

res = find_maximum(arr, n)
print(res)