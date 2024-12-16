'''You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 
means empty and 1 means not empty, and an integer n, return true 
if n new flowers can be planted in the flowerbed without violating 
the no-adjacent-flowers rule and false otherwise.'''

def can_place_flowers(flowerbed, n):
    i = 0
    j = len(flowerbed) - 1
    size = 0
    
    while i <= j:
        if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
            size += 1
            i += 2
        elif i+1 == j and flowerbed[j] == 0 and flowerbed[i] == 0:
            size += 1
            break
        elif i == j and flowerbed[i] == 0 and flowerbed[i-1] == 0:
            size += 1
            i += 1
            break

        else:
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i+1] == 0:
                size += 1
                i += 2
            else:
                i += 1
        
        
    print(size)
    if n <= size:
        return True
    return False

flowerbed = [1,0,0,0,0,0,0]
n = 1
res = can_place_flowers(flowerbed, n)
print(res)