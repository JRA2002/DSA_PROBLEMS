'''Given a matrix(2D array) M of size N*N consisting of 0s and 1s only. The task is to find the column with maximum number of 0s. If more than one column exists, print the one which comes first. If the maximum number of 0s is 0 then return -1.'''

def column_zeros(arr: list, N: int):
    maxZ = 0
    idx = -1
    
    for j in range(len(arr[0])):
        count = 0
        for i in range(len(arr)):
            if arr[i][j] == 0:
                count += 1

        if count > maxZ:
            maxZ = count
            idx = j

    return idx


N = 3
M = [[0,1,0],[1,1,0],[0, 1, 0]]

print(column_zeros(M, N))
        
          