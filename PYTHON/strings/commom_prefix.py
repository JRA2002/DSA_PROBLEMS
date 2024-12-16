'''Given a set of strings, find the longest common prefix.'''
def common_prefix1(lista):
    if len(lista) == 1:
        return lista[0]
    
    mini = min(lista)

    value = True
    count = 0
    while value:
        for i in lista:
            if mini in i:
                count += 1
        if count == len(lista):
            value = False
        else:
            mini = mini[:-1]
            count = 0
        
    return mini

# using divide and conquer algorithm
def common_util(str1, str2):
    result = ''
    n1 = len(str1)
    n2 = len(str2)
    i = 0
    j = 0
    
    while i < n1 -1 and j <= n2 - 1:
        if str1[i] != str2[j]:
            break
        result += str1[i]
        i += 1
        j += 1

    return result
    
def common_prefix(lista, low, high):
    if low == high:
        return lista[low]
    if high > low:

        # Same as (low + high)/2, but avoids 
        # overflow for large low and high 
        mid = low + (high - low) // 2
        str1 = common_prefix(lista, low, mid - 1) 
        str2 = common_prefix(lista, mid + 1, high)

        return common_util(str1, str2)

lista = ['apple', 'ape', 'april']
res = common_prefix1(lista)
res2 = common_prefix(lista, 0, len(lista) - 1)
print(res)
print(res2)