'''Given an unsorted array arr[] of size n. Rotate the array to 
the left (counter-clockwise direction) by d steps, where d is a 
positive integer. '''

def rotate_array(A : list, D, N):
    D = D%N
    
    A[:D] = reversed(A[:D])
    A[D:] = reversed(A[D:])
    A[:N] = reversed(A[:N])
    
    return A

A = [1,2,3,4,5,6]
D = 3
N = len(A)
res = rotate_array(A, D , N)
print(res)