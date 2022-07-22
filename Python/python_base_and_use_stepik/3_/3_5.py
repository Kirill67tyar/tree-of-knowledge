from pprint import pprint as pp

"""
API какого-нибудь модуля или сервиса - 
это набор функций, констант и методов, которые мы можем использовать
и при этом про каждую из них известно:
1 - что она принимает
2 - что она возвращает
3 - что она должна делать
Но при этом может быть неизвестно как она это делает (сокрыта реализация)

Почти все web-сервисы, которые предоставляют API требуют API ключ
Это связано с аутентификацией.
Мы должны представиться сервису, он должен знать кто делает данный запрос
Благодаря этому web-сервис предоставляющий API может делать статистику
о пользователях, которые пользуются его API (время, регион и т.д.)


3.5.4
import requests

# source - https://developers.artsy.net/v2/start

data_about_artists = {}
url = 'https://api.artsy.net/api/tokens/xapp_token'
params = {
    'client_id': '148ea5d060d2f5d9f460',
    'client_secret': '134113c19febc45bdc89380d8d9e5d45',
}
kwargs = {
    'url': url,
    'params': params,
}
resp = requests.post(**kwargs)
TOKEN = None
if resp.status_code == 201:
    TOKEN = resp.json().get('token')

with open('dependecies/dataset_24476_4.txt', 'r', encoding='utf-8') as f:
    artists_ids = f.read().splitlines()
    if TOKEN:
        headers = {
            'X-Xapp-Token': TOKEN,
        }
        for art_id in artists_ids:
            url = f'https://api.artsy.net/api/artists/{art_id}'
            response = requests.get(url=url, headers=headers)
            # pp(response.json())
            data = response.json()
            data_about_artists[data['sortable_name']] = int(data['birthday'])

with open('dependecies/artists_names.txt', 'w', encoding='utf-8') as f:
    output = list(data_about_artists.keys())
    output.sort(key=lambda x: data_about_artists[x])
    f.write('\n'.join(output))
    

"""