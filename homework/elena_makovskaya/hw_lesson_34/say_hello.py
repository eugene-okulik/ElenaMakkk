import requests

a = 1

while a <= 30:
    name = 'Дорогой друг'
    print(f"Hello, {name} - {a}")
    response = requests.get('https://google.com').status_code
    print(response)
    a = a + 1
