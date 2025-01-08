'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'''

# using a 2d matrix extra memory
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

    ROWS, COLS = len(matrix), len(matrix[0])
    for r in range(ROWS):
        for c in range(COLS):
            matrix[r][c] = ans[r][c]
    

# optimal approach O(1)
def rotate1(matrix: list):
    pass



matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

print(rotate(matrix))