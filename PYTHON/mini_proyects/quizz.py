import os
import time

ans=False

print('do you wanna play ?')
user_respond = input('yes or no ?')
if user_respond!='yes':
    quit()
else:
    while ans!=True:
    
        os.system('clear')

        print('welcome to my quizz')
        print('------------------')
        print('what is my favorite languaje?')
        print('select your choice : ')
        print('a. python')
        print('b. java')
        print('c. c++')

        answer = str(input('ANSWER : '))

        choices = ['a','b','c']

        answer1 = answer.lower()
        if answer1 in choices:
            if answer1=='a':
                print('PYTHON ITS MY FAVORITE LANGUAGE, GOOD')
                ans = True
            else:
                print('BAD CHOICE')
                time.sleep(2)
        else:
            print('no choice slelected')
            time.sleep(2)


    