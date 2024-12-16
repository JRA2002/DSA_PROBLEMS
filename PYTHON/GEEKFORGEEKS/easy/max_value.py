'''In a given array arr[], find the maximum value of (arr[i] – i) - (arr[j] – j) where i is not equal to j and n is the size of the array. i and j vary from 0 to n-1  arr[].'''

def max_value(arr: list):
    maxi = 0
    mini = arr[0]
   
    n = len(arr)
   
    for i in range(n):
        if (arr[i]-i) > maxi:
            maxi = arr[i] - i
            
    for i in range(n):
        if (arr[i]-i) < mini:
            mini = arr[i] - i 
            
    return maxi - mini
    
arr = [937, 72, 246, 187, 392, 941, 727, 800, 399, 525, 578, 246, 785, 911, 800, 812, 215, 694, 887, 336, 376, 968, 824, 259, 600, 149, 647, 443, 577, 252, 977, 751, 199, 691, 192, 861, 147, 381, 296, 584, 992, 156, 958, 335, 785, 719, 325, 261, 590, 912, 581, 586, 563, 699, 781, 706, 496, 924, 140, 901, 668, 12, 670, 637, 353, 103, 201, 768, 123, 309, 252, 418, 966, 590, 867, 174, 327, 787, 580, 422, 6, 197, 907, 656, 878, 63, 410, 999, 468, 248, 481, 286, 866, 949, 674, 728, 539, 245, 955, 103]

res = max_value(arr)
print(res)