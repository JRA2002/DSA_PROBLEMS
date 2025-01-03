'''You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.'''

def search_matrix(matrix: list, target: int):
    for row in matrix:
        l = 0
        r = len(row) - 1
        while l <= r:
            m = (l+r) // 2
            if row[m] == target:
                return True
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1

    return False
            

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 2

print(search_matrix(matrix, target))