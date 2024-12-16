'''We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.'''
from random import randint

    
def guess_number(n: int):
        res = randint(1, n)
        def guess(ans: int) -> int:
            
            if ans == res:
                return 0
            elif ans < res :
                return 1
            else:
                return -1
        
        l = 1
        r = n
        while l <= r:
            m = (l + r)//2
            if guess(m) == 0:
                return m
            elif guess(m) == 1:
                l = m + 1
            else:
                r = m - 1

n = 10

res = guess_number(n)
print(res)