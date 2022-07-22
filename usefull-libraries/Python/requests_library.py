"""
sources:


 -- content
не для текста, а для бинарных файлов (картинки, видео, музыка)

атрибут content у объекта response предоставляет бинарные данные
это связано с тем, что мы можем использовать HTTP протокол
не только для передачи текста, но и бинарных данных
состоящих из байтовых строк

    >>> url = 'https://docs.python.org/3/_static/py.svg'
    >>> response = requests.get(url=url)
    >>> response.status_code
    200
    >>> response.content
    b'<svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">\n<path d="M7.90472

 -- text
атрибут text для HTML страницы






"""
from pprint import pprint as pp
import requests

# url = 'https://docs.python.org/3/_static/py.svg'
# response = requests.get(url=url)
# print(response.status_code)
# print(response.content)
# with open('pyt.png', 'wb') as f:
#     f.write(response.content)



"""
https://ru.wikipedia.org/wiki/%D0%90%D1%80%D1%85%D0%B0%D1%80


Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:

Yes
"""




