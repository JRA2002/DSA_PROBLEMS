'''Given two arrays a[] and b[] respectively of size n and m, 
the task is to print the count of elements in the intersection 
(or common elements) of the two arrays.

For this question, the intersection of two arrays can be defined
 as the set containing distinct common elements between the two arrays. '''

def intersection_arrays(a: list, b: list, n, m):

        set1 = set()
        count = 0
        
        for i in range(n):
            set1.add(a[i])
            
        for i in range(m):
            if b[i] in set1:
                count += 1
                set1.remove(b[i])
        return count
        

a = [1,2,3,4,5,6]
b = [3,4,5,6,7]
n = len(a)
m = len(b)

res = intersection_arrays(a, b, n, m)
print(res)