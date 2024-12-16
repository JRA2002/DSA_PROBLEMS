'''Given two strings a and b. The task is to find if the string 'b' 
can be obtained by rotating (in any direction) string 'a' by exactly 
2 places.'''


def is_rotate(str1, str2):
    A = [i for i in str1]
    B = [i for i in str2]
    N = len(str1) - 1

    for _ in range(2):
        A.append(A[0])
        A.pop(0)
    if A == B:
        return 1
    
    A = [i for i in str1]

    for _ in range(2):
        A.insert(0, A[N])
        A.pop()
    
    if A == B:
        return 1
    return 0
    
    
    
str1 = 'amazon'
str2 = 'azonam'

res = is_rotate(str1, str2)
print(res)