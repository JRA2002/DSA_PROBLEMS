'''Given an array height representing the heights of buildings. You have to count the buildings that will see the sunrise (Assume the sun rises on the side of the array starting point).
Note: The height of the building should be strictly greater than the height of the buildings left in order to see the sun.'''

def count_buildings(height: list):
    maxi = 0
    count = 0

    for num in height:
        if num > maxi:
            count += 1
            maxi = num

    return count

height = [7, 4, 8, 2, 9]

print(count_buildings(height))