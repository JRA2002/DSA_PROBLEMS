'''Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

Note: No two strings are the second most repeated, there will be always a single string.'''

def second_repeated(arr: list, n: int):
    mapa = {}
    for word in arr:
        if word not in mapa:
            mapa[word] = 1
        else:
            mapa[word] += 1
    mapa = dict(sorted(mapa.items(), key=lambda item: (item[1], item[0]), reverse=True))
    i = 1
    for k,v in mapa.items():
        if i == 2:
            return k
        i += 1

    return ''

arr = ["aaa", "bbb", "ccc", "bbb", "aaa", "aaa"]
n = len(arr)

print(second_repeated(arr, n))