'''Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.'''

def lucky_number(matrix: list):
        
    n = len(matrix)
    for i in range(len(matrix[0])):
        maxi = matrix[0][i]
        mini = matrix[i][0]
        
        for j in range(n):
            if matrix[j][i] > maxi:
                maxi = matrix[j][i]
            if matrix[i][j] < mini:
                mini = matrix[i][j]
                
        if maxi == mini:
            return maxi
    

matrix = [[7,8],[1,2]]

res = lucky_number(matrix)
print(res)