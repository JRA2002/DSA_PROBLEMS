'''Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal 
and all the elements on the secondary diagonal that are not part 
of the primary diagonal.'''

def matrix_diagonal_sum(matrix):
    if len(matrix) % 2 != 0:
        suma = -1 * matrix[len(matrix)//2][len(matrix)//2]
    else:
        suma = 0
    j = len(matrix) - 1
    for i in range(len(matrix)):
        
        suma =  suma + matrix[i][i] + matrix[i][j]
        j -= 1
    return suma

mat = [[1,2,3],
        [4,5,6],
        [7,8,9]]
res = matrix_diagonal_sum(mat)
print(res)




