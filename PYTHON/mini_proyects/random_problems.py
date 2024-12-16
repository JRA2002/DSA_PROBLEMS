import random
import os
import time

OPERATORS = ['-','+','*']

num1 = input('number 1 :')
num2 = input('number 2 :')
num_problems = int(input('How many problems to do you resolve? : '))

start_time = time.time()
print('----------------------')
for _ in range(num_problems):
    operator = random.choice(OPERATORS)
    operator1 = random.choice(OPERATORS)

    while True:
    
        exp = f'{num1}{operator}{num2}{operator1}{num1}'
        print(f'solve this {exp}')
        user_answer = input('= ')
        answer = eval(exp)

        if str(answer)==user_answer:
            print('GOOD JOB')
            break
        else:
            print('BAAAD')
end_time = time.time()
final_time = round(end_time-start_time,2)

print('yo finish in ',final_time,' seconds')

time.sleep(2)
os.system('clear')
