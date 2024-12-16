'''Given an integer N the task is to find the largest number which is smaller or equal
 to it and has its digits in non-decreasing order.'''

def find_number(N):
    for num in range(N,0,-1):
        res = True
        num = str(num)
        for i in range(len(num) - 1):
            if num[i] > num[i+1]:
                res = False
                break
        if res:
            return num


N = 43  
res = find_number(N)
print(res)

