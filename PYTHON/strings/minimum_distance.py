'''Given a list of words followed by two words, the task 
is to find the minimum distance between the given two words in the list of words.'''

def minimum_distance(arr, w1, w2):
    lista1 = []
    lista2 = []
    for i, v in enumerate(arr):
        if w1 == v and w1 in arr:
            lista1.append(i)
        if w2 == v and w2 in arr:
            lista2.append(i)
    result = min(lista2) - max(lista1)
    return result


arr = ['the', 'quick', 'the', 'fox', 'quick','fox']
res = minimum_distance(arr, 'the', 'fox')
print(res)
