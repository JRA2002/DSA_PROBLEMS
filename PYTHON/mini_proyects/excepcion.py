
lista = []
try:
    while True:
        line = input("Enter a line :")
        lista.append(line)
except EOFError:
    print("\nyou press a ctrl+D")
    lista.reverse()
    print(lista)
    
    
