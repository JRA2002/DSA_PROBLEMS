def is_deficient(n):
    divi = []
    for i in range(1, n):
        if n % i == 0:
            divi.append(i)
    if sum(divi) > n:
        return False
    return True

res = is_deficient(12)
print(res)