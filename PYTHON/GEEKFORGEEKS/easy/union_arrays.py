'''Given two arrays a[] and b[], the task is to find the number of elements in the union between these two arrays.

The Union of the two arrays can be defined as the set containing distinct elements from both arrays. If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements of a[] and b[] are not necessarily distinct.'''

def find_union(a: list, b: list):
    dict1 = {}
    count = 0
    for num in a:
        if num not in dict1:
            dict1[num] = 1
            count += 1

    for num in b:
        if num not in dict1:
            dict1[num] += 1
            count += 1

    return count


a = [1,1,2,2]
b = [1, 2, 1]

print(find_union(a, b))