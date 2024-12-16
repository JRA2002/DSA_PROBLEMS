'''Given two integers A and B. Find the smallest number X (greater than A)
 which is divisible by B.'''

def divisible_numbers(A, B):
        i = 1
        while i < A:
            res = B * i
            if res > A:
                return res
            i += 1

A = 5
B = 3

res = divisible_numbers(A, B)
print(res)