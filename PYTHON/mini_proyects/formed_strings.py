import  random

strings = ['c' ,'a' , 't' , 'd' , 'o' , 'g']
name = ''

random.shuffle(strings)
print(strings)
for chr in strings:
    name = name + chr

print(name)