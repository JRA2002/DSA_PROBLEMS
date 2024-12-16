'''Ritu has all numbers from 2 to n in an array, arr of 
length n-1 except one number. You have to return the 
missing number, Ritu doesn't have from 1 to n.

Note: Don't use Sorting'''

def missing_number(n, arr):
    suma = n * (n+1)//2
    res = 0
    for num in arr:
        res += num
    return suma - res


n = 4
arr = [1,  4,  3]

res = missing_number(n, arr)
print(res)