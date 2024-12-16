def odd_factors(num):
    list = [1]
    for i in range(2,num+1):
        if num%i==0 and i%2!=0:
            list.append(i)
    print(list)
    print(sum(list))

odd_factors(18)