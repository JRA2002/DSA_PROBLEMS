'''You are given an array arr[] containing positive integers. The elements in the array arr[] range from 1 to n (where n is the size of the array), and some numbers may be repeated or absent. Your task is to count the frequency of all numbers in the range 1 to n and return an array of size n such that result[i] represents the frequency of the number i (1-based indexing).'''

def freq_count(arr: list):
    mapa = {}
    res = []
    for num in arr:
        if num not in mapa:
            mapa[num] = 1
        else:
            mapa[num] += 1

    for i in range(1, len(arr) + 1):
        if i not in mapa:
            res.append(0)
        else:
            res.append(mapa[i])
        
    return res

arr = [2, 3, 2, 3, 5]

print(freq_count(arr))