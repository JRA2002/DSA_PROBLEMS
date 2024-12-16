'''Given an unsorted array arr of positive integers. One number a from the set [1, 2,....,n] is missing and one number b occurs twice in the array. Find numbers a and b.

Note: The test cases are generated such that there always exists one missing and one repeating number within the range [1,n].'''

def find_two_elements(arr: list):
    arr.sort()
    n = len(arr)
    suma = n*(n+1)//2
    suma_arr = sum(arr)
    ans = []

    for i in range(n-1):
        if arr[i] == arr[i+1]:
            ans.append(arr[i])
            break
  
    ans.append(ans[0]+(suma-suma_arr))
    return ans

arr = [1,4,2,4]

res = find_two_elements(arr)
print(res)