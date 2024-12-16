def factorial_of_factorials(n):
    def factorial(x):
        if x == 1:
            return 1
        return factorial(x - 1) * x
    result = 1
    for i in range(n,1,-1):
        fact = factorial(i)
        result = result * fact
    return result

factorial_of_factorials(5)