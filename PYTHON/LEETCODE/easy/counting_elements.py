'''Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.'''

from collections import Counter
def counting_elements(arr: list):
    count = 0
    for num in arr:
        if num+1 in arr:
            count += 1
    return count

# another approach using N space

def counting_elements2(arr: list):
    hash_table = Counter(arr)
    print(hash_table)
    count = 0
    for k in hash_table:
        if hash_table[k+1]:
            count += 1
    return count

arr = [1,3,2,3,5,0]

res = counting_elements2(arr)
print(res)