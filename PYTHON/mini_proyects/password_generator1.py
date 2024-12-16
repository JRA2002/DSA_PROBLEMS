import string
import random

letters = string.ascii_letters
digits = string.digits


def generate_password(min_lenght,digits_include=True):

    pwd = ''

    for _ in range(min_lenght-1):

        pwd = pwd + random.choice(letters)
        if digits_include:
            pwd += random.choice(digits)

    return pwd

min_lenght = int(input('enter a minimun lenght : '))
digits_include = input('include a digits y/n ?: ') == 'y'

pwd = generate_password(min_lenght,digits_include)

print(pwd)