# using tail recursion , most effective on C++ 
def sum_array(arr, acum=0):

    if len(arr) == 0:
        return acum
    return sum_array(arr[1:],acum + arr[0])

res = sum_array([1,2,3,4])
print(res)