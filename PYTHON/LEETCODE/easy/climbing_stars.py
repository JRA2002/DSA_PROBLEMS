'''You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?'''

def climb_stairs(n: int):
    one = 1
    two = 1

    for _ in range(n-1):
        
        temp = one
        one = one + two
        two = temp

    return one

n = 30

print(climb_stairs(n))


