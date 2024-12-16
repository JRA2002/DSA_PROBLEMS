'''Given an array, arr[] of positive integers. Your task is to return the product of array elements under the given modulo, mod with the value of 1000000007.

Note: The modulo operation finds the remainder after the division of one number by another. For example, k(mod(m))=k%m= remainder obtained when k is divided by m'''

def find_product(arr):
    p = 1
    for num in arr:
        p *= num
    p = p % 1000000007
    return p

arr = [1, 2, 3, 4]

res = find_product(arr)
print(res)