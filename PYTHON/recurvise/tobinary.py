def tobinary(n):
    if n == 0:
        return 0
    func = tobinary(n // 2)
  
    return (n % 2) + 10 * func

res = tobinary(21)

def count_one(res):
    res = str(res)
    count = res.count('1')

    return count

