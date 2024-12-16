'''You are given an integer n and an integer array arr of size n+2. 
All elements of the array are in the range from 1 to n. Also, all 
elements occur once except two numbers which occur twice. Find the two repeating numbers.
Note: Return the numbers in their order of appearing twice. So, if 
x and y are repeating numbers, and x's second appearance comes before 
the second appearance of y, then the order should be (x, y).'''

def two_repeated(n, arr):
    dict1 = {}
    i = 8
    ans = []
    for num in arr:
        if num in dict1:
            dict1[num] += 1
            if dict1[num] == 2:
                dict1[num] += i
                i -= 1
        else:
            dict1[num] = 1
    
    dict1 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
    
    for k,v in dict1.items():
        if v >= 9:
            ans.append(k)
    return ans
    
# optimal approach

n = 2
arr = [1, 2, 2,1]

res = two_repeated(n, arr)
print(res)