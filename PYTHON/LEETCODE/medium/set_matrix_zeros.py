'''Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.'''

def set_matrix(matrix: list):
    ROWS, COLS = len(matrix), len(matrix[0])
    rowZero = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                if r > 0:
                    matrix[r][0] = 0
                else:
                    rowZero = True
                matrix[0][c] = 0       
    
    for r in range(1, ROWS):
        for c in range(1, COLS):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for r in range(1, ROWS):
            matrix[r][0] = 0
    
    if rowZero:
        for c in range(COLS):
            matrix[0][c] = 0
    
    

matrix = [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]]

print(set_matrix(matrix))