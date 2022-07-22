from pprint import pprint as pp


"""
Структура HTTP при запросе:

    GET /wiki/Python HTTP/1.1
    Host: ru.wikipedia.org
    Cookie: GeoIP=RU:MOW:Moscow:55.75:37.62:v4; 
            WMF-Last-Access-Global=24-May-2022; 
            WMF-Last-Access=24-May-2022
            

На сегодняшний день HTTP используется не только для обмена гипертекста
с помощью HTTP можно загружать картинки, музыка, видеозаписи (прикреплять, не текстовые, а бинарные (двоичные) файлы) 





3.3.6
from re import findall
import requests

def find_urls(response) -> list:
    all_urls = []
    pattern = r'hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))'
    # pattern = r'<a href=\".+\">[0-9]</a>'
    links = findall(pattern, response.text)
    if links:
        for item in links:
            urls = list(map(lambda s: s.replace('"', ''), filter(lambda x: 'https' in x, item)))
            all_urls.extend(urls)
    return all_urls


first_url = input()
second_url = input()
all_urls = []
response1 = requests.get(url=first_url)
response2 = requests.get(url=second_url)
no = set()
yes = None
if response1.status_code == 200 and response2.status_code == 200:
    # pattern = r'/(https?://)?([\da-z.-]+).([a-z.]{2,6})([/\w .-])/?$/'
    urls = find_urls(response1)
    if urls:
        for u in set(urls):
            r = requests.get(url=u)
            if r.status_code == 200:
                tmp_url = find_urls(r)
                if response2.url in tmp_url:
                    yes = 'Yes'
                    print(yes)
                    break
                else:
                    no.update(('No',))
            else:
                no.update(('No',))

    else:
        no.update(('No',))
else:
    no.update(('No',))
if not yes and no:
    print(list(no)[-1])
















"""

