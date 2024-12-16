'''Given a non-negative integer(without leading zeroes) represented as an array arr. Your task is to add 1 to the number (increment the number by 1). The digits are stored such that the most significant digit is at the starting index of the array.'''

def increment(arr: list):
    res = 0
    one = 1
    n = len(arr)
    for i in range(n-1, -1, -1):
        num = (arr[i] + one + res)
        res = num//10
        coq = num%10
        arr[i] = coq
        one  = 0

    if res != 0:
        arr.insert(0,res)

    return arr

arr = [9,9,9,9,9]

res = increment(arr)
print(res)