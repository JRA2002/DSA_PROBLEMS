from random import shuffle,randint

lista = [2,2,5,5,6,3,4]

#building my own module shuffle
def own_shuffle(lista):
    lista.reverse()
    for i in range(len(lista)-1):
        j = randint(0,len(lista) - 1)
        lista[i], lista[j] = lista[j], lista[i]
    return lista

reorder_list = own_shuffle(lista)
print(reorder_list)