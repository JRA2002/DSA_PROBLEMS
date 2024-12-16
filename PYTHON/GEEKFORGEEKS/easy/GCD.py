'''find the gcd in the array'''

def gcd(arr):
    maxi = max(arr)//2
    count = 0
    n = len(arr)
    
    for i in range(1,maxi+1):
        for num in arr:
            if num%i == 0:
                count += 1
        if count == n:
            res = i
        count = 0
    return res

arr = [20,20,80,40]
res = gcd(arr)
print(res)