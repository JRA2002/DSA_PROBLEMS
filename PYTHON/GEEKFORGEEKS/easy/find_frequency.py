'''Given an Array Arr of N positive integers and an integer X. Return the frequency of X in the array.'''
from collections import Counter
def find_frequency(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    return count

arr = [1, 1, 1, 1, 1]
n = len(arr)
x = 1

res = find_frequency(arr, n, x)
print(res)

a = 'hello hello ola'
s = a.split(' ')
set1 = set(s)
n = a.count('hello')
print(n)
print(set1)