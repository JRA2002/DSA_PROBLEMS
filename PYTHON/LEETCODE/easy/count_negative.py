'''Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.'''

def count_negatives(grid: list):
    
    countN  = 0
    for k in range(len(grid)) :
        i = 0
        n = len(grid[k])
        j = n - 1
        
        while i <= j:
            m = (i+j)//2
            
            if grid[k][m] < 0 and (m == 0 or grid[k][m-1] >= 0):
                countN += n-m
                break
            elif grid[k][m] < 0 and grid[k][m-1] < 0 :
                j = m - 1
            else:
                i = m + 1
    
    return countN

grid = [[3,-1,-3,-3,-3],[2,-2,-3,-3,-3],[1,-2,-3,-3,-3],[0,-3,-3,-3,-3]]

res = count_negatives(grid)
print(res)