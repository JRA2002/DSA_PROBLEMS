'''You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.'''

def check_staright(coordinates: list):
    n = len(coordinates)
    if n == 2:
        return True
    for i in range(n):
        for j in range(i+1,n):
            v1 = (coordinates[j][0] - coordinates[i][0],)
            v2 = coordinates[j][1] - coordinates[i][1]
              
    
    return True


coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]

res = check_staright(coordinates)
print(res)