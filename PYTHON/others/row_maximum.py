'''Given a binary 2D array, where each row is sorted. Find the row with the maximum number of 1s. '''

def row_maximum(arr: list):

    maxi = arr[0].count(1)
    i = 0
    j = 0
    for row in arr:
        num = row.count(1)
        if num > maxi:
            maxi = num
            j = i
        i += 1
    return maxi,j
    

arr = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
res = row_maximum(arr)
print(res)

# Time Complexity: O(M * N)
# Auxiliary Space: O(1)