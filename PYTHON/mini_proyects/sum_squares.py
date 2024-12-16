def sum_smaller(num):   
    lista = sum([i**2 for i in range(num,0,-1) if i % 2 != 0])
    return lista

print(sum_smaller(6))
