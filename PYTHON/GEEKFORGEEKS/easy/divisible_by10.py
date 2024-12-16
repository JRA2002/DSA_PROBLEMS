'''Given a binary number in the form of string, the task is to check whether the decimal representation of the given binary number is divisible by 10 or not. The number could be very large and may not fit even in long long int.'''

def divisible_by_10(bin: str):
    num = int(bin, 10)
    

bin = "1010"

res = divisible_by_10(bin)
print(res)