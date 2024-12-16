from requests import get
from pprint import PrettyPrinter
import os
import time

API_KEY = 'd0b440c5f0e5b3bcd1f11a30'
BASE_URL = 'https://v6.exchangerate-api.com'

printer = PrettyPrinter()

def get_currencies():

    endpoint = f'/v6/{API_KEY}/latest/USD'
    url = BASE_URL + endpoint

    response = get(url).json()['conversion_rates']

    data = list(response.items())

    return data

def print_currencies(currencies):
    for currency in currencies:
        name = currency[0]
        value = currency[1]
        if name=='USD':
            print(f'{name}-- fuck you gringos')
        print(f'{name} - - {value}')

def  convert_currency(cur1,cur2,amount):
    endpoint = f'/v6/{API_KEY}/pair/{cur1}/{cur2}'
    url = BASE_URL + endpoint

    data = get(url).json()
    rate = data['conversion_rate']
    state = data['result']

    total = amount*rate


    printer.pprint(f'{cur1} convert to {cur2} -- {rate} -- {state}')
    printer.pprint(f'You total amount is {total} {cur2}')


def main():

    print('Welcome to converter app')
    print('--------------------------')
    print("press 'q' to quite")
    print("type 'list' show actual currencies")
    print("type 'convert' for convert your money")

    while True:
        choice = input('choice = ').lower()

        if choice=='q':
            break
        elif choice=='list':

            data = get_currencies()
            print_currencies(data)
            continue
        elif choice=='convert':

            cur1 = input('Enter currency to convert : ')
            cur2 = input('Enter currency to you want : ')
            amount = int(input('Enter the amount to convert = '))

            convert_currency(cur1,cur2,amount)
            
            continue
        else:
            print('you enter a wrong word..try again')

main()
#time.sleep(6)
#os.system('clear')