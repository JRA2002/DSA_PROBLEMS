'''Given two arrays a[] and b[] of equal size, the task is to find whether the elements in the arrays are equal.

Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.

Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.'''

def check_equal(a: list, b: list):
    mapa = {}
    mapb = {}
    for i in range(len(a)):
        if a[i] not in mapa and b[i] not in mapb:
            mapa[a[i]] = 1
            mapb[b[i]] = 1
        else:
            mapa[a[i]] += 1
            mapb[b[i]] += 1

    return mapa == mapb

a = [1, 2, 5, 4, 0]
b = [2, 4, 5, 0, 11]

print(check_equal(a, b))