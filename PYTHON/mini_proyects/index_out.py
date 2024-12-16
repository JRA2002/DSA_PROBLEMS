lista = [2,3,4,5]

def out_index(lista):
    a = []
    try:
        for i in range(len(lista)):
            a[i] = i * 4
        return a
    except IndexError:
        return print("“Don’t try buffer overflow attacks in Python!”")

a = out_index(lista)
print(a)