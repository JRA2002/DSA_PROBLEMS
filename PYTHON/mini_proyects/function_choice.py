from random import randrange

def mychoice(lista):
    num = randrange(1,9)
    if num in lista:
        print(f"your choice is {num}")
    else:
        mychoice(lista)

lista = [3,6,1,9,4]
mychoice(lista)



