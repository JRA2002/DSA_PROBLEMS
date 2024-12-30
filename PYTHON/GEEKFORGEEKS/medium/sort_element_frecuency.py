'''Given an array of integers arr[], sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.'''

def sort_by_freq(arr: list):
    mapa = {}
    for num in arr:
        if num not in mapa:
            mapa[num] = 1
        else:
            mapa[num] += 1
            
    for i in range(len(arr)):
        arr[i] = (arr[i], mapa[arr[i]])
    
    arr = sorted(arr, key=lambda x: (-x[1], x[0]))
    
    i = 0
    for tup in arr:
        arr[i] = tup[0]
        i += 1
    return arr

arr = [5,5,4,6,4]

print(sort_by_freq(arr))