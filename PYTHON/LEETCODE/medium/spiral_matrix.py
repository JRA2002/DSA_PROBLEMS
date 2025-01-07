'''Given an m x n matrix, return all elements of the matrix in spiral order.'''

def spiral_matrix(matrix: list):
    top = 0
    right = len(matrix[0])
    left = 0
    bottom = len(matrix)
    ans = []
    
    while top < bottom and left < right: 
                                     
        for t in range(top, right):
            ans.append(matrix[top][t])
            
        top += 1
        right -= 1

        for t in range(top, bottom):
            ans.append(matrix[t][right])
            
        bottom -= 1
        
        if top <= bottom:
            for t in range(right-1, left - 1, -1):
                ans.append(matrix[bottom][t])
            left += 1
           
            if left <= right:
                for t in range(bottom-1, top-1, - 1):
                    ans.append(matrix[t][top-1])
                                                 
    return ans

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(matrix))