def to_from_list(n):
    if isinstance(n, int):
        lista = []
        string = str(n)
        for i in string:
            lista.append(i)
        return lista
    number = ''
    for i in n:
        number = number + str(i)
    return int(number)

res = to_from_list([1,2,3,4,5])
print(res)
