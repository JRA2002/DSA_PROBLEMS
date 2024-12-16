print('WELCOME TO THE GAME')
print('--------------------')

answer = input('choose right or left :')

if answer=='right':
    answer = input('You choose the right direction ,and do you like river or wood :')
    if answer=='river':
        print('you are in the river good swim')
    elif answer=='wood':
        print('be careful ,many bears inside')
    else:
        print('you write the wrong choice....')   
elif answer=='left':
    print('you win')
else:
    print('you write the wrong choice....')
