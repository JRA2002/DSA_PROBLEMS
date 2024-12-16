'''Given an array consisting of the cost of toys. Given an integer K depicting the amount of money available to purchase toys. 
Write a program to find the maximum number of toys one can buy with the amount K. '''

def maximun_toys(arr: list, n, k):
    count = 0
    suma = 0
    arr.sort()

    for i in range(n):
        
        if suma + arr[i] < k:
            count += 1
            suma += arr[i]
    return count, suma


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
res = maximun_toys(arr,n ,13)

print(res)

