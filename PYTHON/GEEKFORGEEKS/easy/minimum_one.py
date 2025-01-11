'''Given a 2D binary matrix(1-based indexed) mat of dimensions nxm , determine the row that contains the minimum number of 1's.
Note: The matrix contains only 1's and 0's. Also, if two or more rows contain the minimum number of 1's, the answer is the lowest of those indices.'''

def minRow(a: list):
    mini = len(a[0]) + 1
    
    for i in range(len(a)):
        count = 0
        for j in range(len(a[0])):
            if a[i][j] == 1:
                count += 1
        if count < mini:
            mini = count
            idx = i + 1

    return idx

a = [[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]

print(minRow(a))