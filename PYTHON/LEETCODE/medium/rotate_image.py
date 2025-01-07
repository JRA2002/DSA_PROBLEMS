'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''

def rotate(matrix: list):
    n = len(matrix)
    ans = [[0]*len(matrix[0]) for _ in range(n)]
    r = 0
  
    while r < n:
        c = 0
       
        for i in range(n-1,-1,-1):
            ans[r][c] = matrix[i][r]
            c += 1
        r += 1
        
    return ans


matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotate(matrix))