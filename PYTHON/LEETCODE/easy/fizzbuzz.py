'''Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.'''

def fizzbuzz(n: int):
    ans = [str(i) for i in range(1, n+1)]
    for i in range(n):
        
        if (i+1)%3 == 0 and (i+1)%5 == 0:
            ans[i] = "FizzBuzz"
        elif (i+1) % 3 == 0:
            ans[i] = "Fizz"
        elif (i+1) % 5 == 0:
            ans[i] = "Buzz"
    return ans
    

n = 15

print(fizzbuzz(n))