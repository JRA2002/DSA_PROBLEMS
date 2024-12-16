'''Given a string str and another string patt. Find the minimum index of the character in str that is also present in patt.'''

def min_index_char(Str, pat):
    dict1 = {}
    for i in range(len(Str)):
        if Str[i] not in dict1:
            dict1[Str[i]] = i

    for k,v in dict1.items():
        if k in pat:
            return v
    return -1

Str = 'geeksforgeeks'
pat = 'set'

res = min_index_char(Str, pat)
print(res)