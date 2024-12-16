'''Given a string in roman no format (s)  your task is to convert it to an integer . Various symbols and their values are given below.
I 1
V 5
X 10
L 50
C 100
D 500
M 1000'''

def roman_integr(S):
    def romans(char):
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'C':
            return 100
        elif char == 'L':
            return 50
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000
    res = 0    
    i = 0
    while i < len(S):
        r1 = romans(S[i])
        if i + 1 < len(S):
            r2 = romans(S[i+1])
        else:
            r2 = 0
        if r1 > r2:
            res = res + r1
            i += 1
        elif r1 == r2:
            res = res + r1 + r2
            i += 2
        else:
            res = res + r2 - r1
            i += 2
    return res

S = 'MMMDCLXXX'
res = roman_integr(S)
print(res)