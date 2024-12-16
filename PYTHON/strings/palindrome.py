def ispar(x):
        res = {'{':'}', '[':']', '(':')'}
        i = 0
        j = len(x) - 1
        if 'p' in res:
             print('noo')
        else:
             print('yes')
        while i < j:
            if res[x[i]] != x[j]:
                return False   
            i += 1
            j -= 1
        return True

str1 = '{([])}'
res = ispar(str1)
print(res)