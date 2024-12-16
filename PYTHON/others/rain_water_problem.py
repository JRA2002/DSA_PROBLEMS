'''Trapping Rainwater Problem states that given an array of N 
non-negative integers arr[] representing an elevation 
map where the width of each bar is 1, compute how much w
ater it can trap after rain.'''

def rain_water(arr):
    water = 0
    ini = arr[0]
    rest = 0
    for i in range(1, len(arr)):
        if ini < arr[i]:
            water = water + (i-1)*ini - rest
            ini = arr[i]
            rest = 0
        else:
            rest = rest + arr[i]
            print(rest)
    

    return water

arr = [3, 0, 2, 0, 4]
res = rain_water(arr)
print(res)
