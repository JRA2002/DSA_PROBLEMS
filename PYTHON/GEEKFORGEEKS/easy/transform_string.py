'''You are given the string S . Compress the string when lower 
and upper cases are the same. In compressed string characters should be in lowercase.'''

def transform(S: str):
    S = S.lower()
    i = 0
    count = 1
    new = ''
    while i < len(S):
        print(i)
        if i+1 < len(S):
            if S[i] == S[i+1]:
                count += 1
            else:
                res = str(count) + S[i]
                new += res
                count = 1
        else:
            res = str(count) + S[i]
            new += res
        i += 1
    return new
        
        

S = 'a'
res = transform(S)
print(res)
