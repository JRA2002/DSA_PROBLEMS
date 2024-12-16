from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://cat-fact.herokuapp.com'
ALL_JSON = '/facts'

printer = PrettyPrinter()

data = get(BASE_URL + ALL_JSON).json()

printer.pprint(data)