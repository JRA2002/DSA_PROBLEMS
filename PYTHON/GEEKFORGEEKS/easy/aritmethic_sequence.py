'''Given three integers  'A' denoting the first term of an arithmetic 
sequence , 'C' denoting the common difference of an arithmetic sequence 
and an integer 'B'. you need to tell whether 'B' exists in the arithmetic 
sequence or not. Return 1 if B is present in the sequence. Otherwise, returns 0.'''

def aritmehtic_sequence(A, B, C):
    print(A,B,C)
    if A > B:
        while B > A:
            print(A)
            A = A + C
            
    else:
        while A < B:
            print(A)
            A = A + C
    if B == A:
        return 1
            
    return 0

A = -2
B = -9
C = -7

res = aritmehtic_sequence(A, B, C)
print(res)