'''You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.'''

def largest_local(grid):
    right = len(grid[0]) - 1
    left = 1
    maxi = 0
    while left <=right:
        for i in range(0, right):
            print(grid[left][i])
            if grid[left][i] > maxi:
                maxi = grid[left][i]
        left += 1
    return maxi
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
res = largest_local(grid)
print(res)
# pendiente