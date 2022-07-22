"""
https://api.openweathermap.org/data/2.5/onecall?&&appid=2e04ebccf6e8cf4e9e1bc3288cf3b7a7
lat=33.44
lon=-94.04

https://api.openweathermap.org/data/2.5/weather?q=Moscow,ru&appid=2e04ebccf6e8cf4e9e1bc3288cf3b7a7&
"""
import requests
import json
KEY = None
cities = {
        'курган': 'Kurgan,ru',
        'москва': 'Moscow,ru',
    }
with open('dependecies/key_for_openweathermap.txt', 'r') as f:
    KEY = f.read().strip()

if KEY:
    q = None
    while True:
        city = input()
        try:
            q = cities[city.lower()]
            if q:
                break
        except KeyError:
            print('Об этом городе нет данных, или Вы ввели не правильно. Попробуйте ещё раз')


    kwargs = {
        # 'url': 'https://api.openweathermap.org/data/2.5/onecall',
        'url': 'https://api.openweathermap.org/data/2.5/weather',
        'params': {
            'appid': KEY,
            # 'lat': input(),  # 33.44
            # 'lon': input(),  # -94.04
            'q': q,
            'units': 'metric',
        }
    }

    response = requests.get(**kwargs)
    if response.status_code == 200:
        # pp(response.headers)
        # print(response.headers.get('Content-Type'))
        # # pp(response.json()) # return json.loads(response.text)
        # pp(response.json() == json.loads(response.text)) # True
        data = response.json()
        tmp = data.get('main').get('temp')
        print(f'Температура в городе {city.title()} - {tmp} C')
        pass
