'''A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.'''

def find_distance_stop(distance: list, start, destination):
        suma1 = 0
        n = len(distance)
        if start < destination:
            for i in range(start,destination):
                suma1 += distance[i]
        else:
            for i in range(destination,start):
                suma1 += distance[i]

        suma2 = 0
        for i in range(n):
            suma2 += distance[i]
        suma2 = suma2 - suma1
        
        return min(suma2, suma1) 


distance = [1,2,3,4]
start = 0
destination = 3

res = find_distance_stop(distance, start, destination)
print(res)