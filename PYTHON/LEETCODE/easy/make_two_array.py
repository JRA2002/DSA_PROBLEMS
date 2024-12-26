'''You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.'''

def make_two_array(target: list, arr: list):
    
    mapa = {}
    mapa1 = {}
    for num in target:
        if num not in mapa:
            mapa[num] = 1
        else:
            mapa[num] += 1
    for num in arr:
        if num not in mapa1:
            mapa1[num] = 1
        else:
            mapa1[num] += 1

    return mapa == mapa1


target = [1,2,2,3]
arr = [1,1,2,3]

print(make_two_array(target, arr))