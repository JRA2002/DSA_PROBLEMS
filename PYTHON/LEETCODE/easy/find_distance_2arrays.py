'''Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.'''

def find_distance(arr1: list, arr2: list, d: int):
    count = 0
    
    for num in arr1:
        flag = True
        for i in range(len(arr2)):
            if abs(num - arr2[i]) <= d:
                flag = False
                break
        
        if flag:
            count += 1
    return count

# optimal approach

def find_distance2(arr1: list, arr2: list, d: int):
    arr2.sort()
    count = 0
    for num in arr1:
        l = 0
        r = len(arr2) - 1
        while l <= r:
            m = (l+r)//2
            if arr2[m] == num:
                break
            elif arr2[m] < num:
                l = m + 1
            else:
                r = m - 1
        print(arr2)
        print(m)
        if min(abs(num - arr2[m]),abs(num - arr2[m+1])) > d:
            count += 1
            print(num, arr2[m])

    return count

arr1 = [2,1,100,3]
arr2 = [-5,-2,10,-3,7]
d = 6

res = find_distance2(arr1, arr2, d)
print(res)