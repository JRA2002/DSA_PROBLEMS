'''Given an integer array a[] of size n, find the highest element of the array. The array will either be strictly increasing or strictly increasing and then strictly decreasing.

Note: a[i] != a[i+1] '''

def peak_element(a):
     i = 0
     j = len(a) - 1
     while i <= j:
            midd = (i+j)//2
            if midd+1 <= j:
                if a[midd] > a[midd+1] and a[midd] > a[midd-1]:
                    return a[midd]
                elif a[midd] < a[midd+1]:
                    i = midd + 1
                else:
                    j = midd - 1
            else:
                 return a[midd]
            

a = [1, 2, 3, 4, 5, 6,1,2,3]

res = peak_element(a)
print(res)