'''Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.'''

def square_sum(c):
    i = 0
    j = c
    while i <= j:
        if (i*i) + (j*j) == c:
            return i, j
        elif (i*i) + (j*j) > c: 
            j -= 1
        else:
            i += 1
    return False
# optimal solution

def square_sum2(c):
    start =  1
    end = c
    while start <= end:
        midd =  (end-start)//2 + start
        if midd * midd == c:
            end = midd
            break
        elif midd * midd > c:
            end = midd - 1
        else:
            start = midd + 1
   
    for i in range(end,-1,-1):

        num = c - i*i
        a = int(num ** 0.5)
        if  a * a == num:
            return True
    return False

c = 1000
res = square_sum2(c)
print(res)