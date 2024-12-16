'''Given an array of positive numbers, find the smallest 
positive integer value that cannot be represented as the 
sum of elements of any subset of a given set. 
The expected time complexity is O(nlogn).'''

def positive_integer(arr):
    res = True
    num = 1
    while res:
        if num in arr:
            num += 1
        else:
            k = 2
            for i in range(len(arr) - k + 1):
                new = arr[i:k+i]
                if sum(new) == num:
                    num += 1
                    continue
            return num
        
arr = [1, 2, 5, 10, 20, 40]
res = positive_integer(arr)
print(res)
