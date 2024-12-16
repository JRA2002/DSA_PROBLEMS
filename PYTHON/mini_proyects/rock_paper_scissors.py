import random
import time
import os

list = ['rock','paper','scissors']

while True:

    user = input('Type rock/paper/scissors  or Q to quit:').lower()

    if user=='q':
        break
    if user not in list:
        print('TYPE just rock , paper, scissors... please ')
    else:
        compu = random.choice(list)

        if user=='rock' and compu=='paper':
            print('YOU WIN')
            
        elif user=='scissors' and compu=='paper':
            print('USER WINS')
            
        elif user=='paper' and compu=='rock':
            print('YOU WIN')
        elif user==compu:
            print('EQUAL')
        else:
            print('YOU LOSE....looooser')
    break

print('GOODBYE USER')
time.sleep(4)
os.system('clear')

    

