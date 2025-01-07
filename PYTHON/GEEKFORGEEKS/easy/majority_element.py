'''Given an array arr. Find the majority element in the array. If no majority exists, return -1.

A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.'''

def majority_element(arr: list):
    mapa = {}
    for num in arr:
        if num not in mapa:
            mapa[num] = 1
        else:
            mapa[num] += 1
        if mapa[num] > len(arr)//2:
            return num
    return -1

arr = [3, 1, 1, 3, 3]

print(majority_element(arr))