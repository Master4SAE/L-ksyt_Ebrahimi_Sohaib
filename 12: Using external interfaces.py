#12.1
import requests


def get_joke():
    request = "https://api.chucknorris.io/jokes/random"
    response = requests.get(request).json()
    return print(response["value"])


keyword = input("Hey press a for a random joke and press anything else to quit > ")

keyword = keyword.lower()
while keyword == 'a':
    get_joke()
    keyword = input("Hey press a for a random joke and press anything else to quit > ")
