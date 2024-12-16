'''Given a string, the task is to reverse the order of the words in the given string. '''
def reverse(s: str):
    lista = s.split(' ')
    news = ''
    for i in range(len(lista) - 1, -1, -1):
        news = news + lista[i] + ' '
    return news

s = 'geeks quiz practice code'
res = reverse(s)
print(res)
