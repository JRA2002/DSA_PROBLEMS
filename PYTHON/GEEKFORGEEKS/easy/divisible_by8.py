'''Given a string representation of a decimal number s, check whether it is divisible by 8.'''

def is_divisible_by_8(s: str):
        s = s[-3:]
        res = int(s)%8 == 0
        if res:
            return 1
        return -1

s = "54141111648421214584416464555"

res = is_divisible_by_8(s)
print(res)