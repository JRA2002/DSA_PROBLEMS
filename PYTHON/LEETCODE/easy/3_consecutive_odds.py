'''Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.'''

def three_cons_odds(arr: list):
    n = len(arr)
    count = 0
    for i in range(n):
    
        if arr[i]%2 != 0:
            count += 1
            if count == 3:
                return True
        else:
            count = 0
    
    return False

arr = [1,1,1]

res = three_cons_odds(arr)
print(res)