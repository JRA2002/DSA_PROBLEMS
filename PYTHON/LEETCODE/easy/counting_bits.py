'''Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.'''

def counting_bits(n: int):
    res = [0] * (n+1)
    for i in range(n+1):
        idx = i
        count = 0
        while i != 0:
            r = i % 2
            if r == 1:
                count += 1
            i = i // 2
        res[idx] = count
    
    return res

# optimal approach
# using bit manipulation 
def counting_bits2(n: int):
    pass

n = 5
print(counting_bits(n))