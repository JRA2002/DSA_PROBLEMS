def factorial(num):
    if num == 1:
        return 1
    return factorial(num - 1) * num

# using tail recursion
def new_factorial(num, acum=1):
    if num == 0:
        return acum
    return new_factorial(num - 1, num * acum)

res = factorial(15)
print(res)