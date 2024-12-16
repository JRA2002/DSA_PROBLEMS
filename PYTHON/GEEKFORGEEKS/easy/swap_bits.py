'''Two players, Player 1 and Player 2, are given an integer
 N to play a game. The rules of the game are as follows :
1. In one turn, a player can remove any set bit of N in 
its binary representation to make a new N.
2. Player 1 always takes first turn.
3. If a player cannot make a move, he loses.'''

def swap_bits(N):
    count = 0
    while N > 0:
        res = N % 2
        if res == 1:
            count += 1
        N = N // 2
    if count %2 == 0:
        return 2
    return 1

N = 7
res = swap_bits(N)
print(res)