n = int(input("enter n: "))
lines = 1
count = 1
m = n * 3
while lines <= n:
    star = '.|.' * count
    line = '-' * ((m - 3) // 2)
    if lines < (n // 2) + 1:
        print(line + star + line)
        count += 2
    elif lines == (n // 2) + 1:
        print(line + "WELCOME" + line)
    elif lines > (n // 2) + 1:
        star = '.|.' * (count)
        print(line + star + line)
        count -= 2
        
    lines += 1