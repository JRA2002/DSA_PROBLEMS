'''Your task, is to create a NxN spiral with a given size.
Return value should contain array of arrays, of 0 and 1, with 
the first row being composed of 1s. For example for given size 5 
the result should be:
[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.
General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.'''

def spiral_ones(k):
        arr = [[] * k] * k
        m = len(arr)
        n = len(arr[0])
        top = 0
        bottom = n - 1
        left = 0
        right = m - 1

        print(arr)
        for i in range(left,right + 1):
            arr[top][i] = 1
            print(arr[top][i])
        arr[2][2] = 8
        print(arr)
            

    
spiral_ones(5)
#print(res)