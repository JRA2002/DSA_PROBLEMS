def sum_digits(num):
    if num < 10:
        return num
    return sum_digits(num // 10) + num % 10

res = sum_digits(123456789)
print(res)