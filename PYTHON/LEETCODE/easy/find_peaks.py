'''You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.

Return an array that consists of indices of peaks in the given array in any order.

Notes:

A peak is defined as an element that is strictly greater than its neighboring elements.
The first and last elements of the array are not a peak.'''

def find_peaks(mountain: list):
    n = len(mountain)
    i = 1
    res = []
    while i < n - 1:
        if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
            res.append(i)
        i += 1
    return res  


mountain = [1,3,6,5]

res = find_peaks(mountain)
print(res)