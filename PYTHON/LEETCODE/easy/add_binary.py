'''Given two binary strings a and b, return their sum as a binary string.'''

def add_binary(a, b):
    res = bin(int(a, 2) + int(b, 2))
    return res[2:]

a = "11"
b = "1"

res = add_binary(a, b)
print(res)