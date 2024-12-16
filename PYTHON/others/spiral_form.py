'''Given an m x n matrix, the task is to print all elements of the matrix in spiral form.'''

def spiral(arr , n, m):
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        while top <= bottom and left <= right:
            for i in range(left,right + 1):
                print(arr[top][i], end=' ')
            top += 1

            for i in range(top,bottom + 1):
                print(arr[i][right], end=' ')
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    print(arr[bottom][i],end=' ')
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    print(arr[i][left], end=' ')
                left += 1
        
arr = [[1,2,3], [8,9,4], [7,6,5]]

#spiral(arr, len(arr), len(arr[0]))

def spiral_lista(snail_map):
        m = len(snail_map)
        n = len(snail_map[0])
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1
        lista = []

        while top <= bottom and left <= right:
            for i in range(left,right + 1):
                lista.append(snail_map[top][i])
            top += 1

            for i in range(top,bottom + 1):
                lista.append(snail_map[i][right])
            right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    lista.append(snail_map[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    lista.append(snail_map[i][left])
                left += 1
        return lista

res = spiral_lista(arr)
print(res)
