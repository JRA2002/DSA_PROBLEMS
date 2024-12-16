'''Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.'''

def max_lenght(n, arr: list):
    k = 1
    maxi = 0
    while k <= n:
        for i in range(n - k + 1):
            new = arr[i:k+i]
            if sum(new) == 0:
                maxi = max(k,maxi)
        k += 1
    return maxi

# optimal solution

def max_lenght2(n, arr: list):
        dict1 = {}
        first = {}
        suma = 0
        for i in range(n):
            suma += arr[i]
            dict1[suma] = i
        suma = 0
        for i in range(n):
            suma += arr[i]
            if suma not in first:
                first[suma] = i
        maxi = 0
        suma = 0
        for num in arr:
            suma += num
            maxi = max(maxi,(dict1[suma] - first[suma]))
        print(dict1)
        print(first)
        return maxi

arr = [15,-2,2,-8,1,7,10,23]
n = len(arr)

res = max_lenght2(n, arr)
print(res)