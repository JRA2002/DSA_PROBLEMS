def perrin_sequence(n):
    lista = []
    if n == 0:
        return 3
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    print(n)
    return perrin_sequence(n-2) + perrin_sequence(n-3)

res = perrin_sequence(5)
print(res)

hash()