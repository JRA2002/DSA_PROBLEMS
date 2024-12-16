import random

try:
    answer = int(input('what number i am thinking : '))

    number = random.randint(1,3)
except:
    print('you need to choice a number....')

finally:
    if answer<0:
          print('need to enter a positive number')
          quit()
    else:
        if number==answer:
            print(f'you find my number...good')
            print(number)
        else:
            print('BAD CHOICE')



