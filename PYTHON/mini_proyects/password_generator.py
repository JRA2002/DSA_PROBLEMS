from cryptography.fernet import Fernet 
import random

list = ['a','b','c','1','2','3','@','#']

password = ''
for i in range(len(list)):
    
        a = random.choice(list)
        
        password = password + a

'''def write_key():
       key = Fernet.generate_key()
       with open('key.key','wb') as key_file:
              key_file.write(key)'''

def load_key():
       file = open('key.key','rb')
       key = file.read
       file.close()
       return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt' ,'r') as file:
            for line in file.readlines():
                   print(line)

def add():
       user = input('enter your username : ')
       with open ('password.txt','a') as file:
              file.write(f'{user}----{fer.encrypt(password.encode())}'+'\n')

print('welcome to password manager')
print('---------------------')

choice = input('your choice es add or view : ')
if choice == 'add':
       add()
elif choice == 'view':
       view()
else:
       print('you choice is wrong')
