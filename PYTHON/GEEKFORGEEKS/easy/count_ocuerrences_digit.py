'''Given an array arr[]. Your task is to return an integer denoting the total number of times digit k appears in the array.'''

def count_num(k: int, arr: list):
    count = 0
    for num in arr:
        while num > 0:
            r = num % 10
            if r == 1:
                count += 1
            num = num // 10

    return count

k=1
arr = [11, 12, 13, 14, 15]

print(count_num(k, arr))