'''You are given the heights of consecutive buildings. You can move from the roof of a building to the roof of the next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.'''

def max_step(arr):
    count = 0
    maxi = 0
    for i in range(len(arr) - 1):
        if arr[i] < arr[i+1]:
            count += 1
            maxi = max(maxi, count)
        else:
            count = 0
        
    return maxi

arr = [20, 6, 5, 10, 7, 17, 19, 4, 17, 2, 18, 12, 16, 11]
res = max_step(arr)
print(res)