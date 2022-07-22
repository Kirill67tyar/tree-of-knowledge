from pprint import pprint as pp

"""
sources:
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html
    
pp(dir(str))
help(str)
print(str.__doc__)



У многих методов str есть аргументы по умолчанию start и end
но не у всех
print(str.startswith.__doc__)
print(str.find.__doc__)

 - startswith
интересный пример startswith

    t = ('кит','кот',"хохло-кiт",)
    s = 'хохло-кiт ибавав вас в рiт'
    s.startswith(t) # True

 - endwith
очень удобен для форматов
 
    f = 'some_file.py'
    f.endswith('.py') # True

 - если у метода стоит вначале буква r, то скорее всего он читает строку с права на лево:
 
rfind
rindex
rstrip - удаление пробельных символов в конце строки
rpartition
rsplit

 - если метод начинается га is, то он проверяет строку на соответствие и возвращает булевое значение:
 
S.isdigit()	
S.isalpha()	
S.isalnum()	
S.islower()	
S.isupper()	
S.isspace()	
S.istitle()

 - split
str.split(sep=None, maxsplit=- 1)

    s = 'хохло-кiт ибав вас в рiт'
    s.upper().split() # ['ХОХЛО-КIТ', 'ИБАВ', 'ВАС', 'В', 'РIТ']
    
по умолчанию split разделяет по пробелу

    s = 'хохло-кiт       ибав\t\t\t вас     в \nрiт'
    s.split() # ['хохло-кiт', 'ибав', 'вас', 'в', 'рiт']
    
    
 - rstrip, lstrip, strip
 
rstrip - убирает справа
lstrip - убирает слева
strip - убирает с обоих концов

НО

    s = '_*__1,2,3,__@*_'
    repr(s.rstrip('*@_')) # "'_*__1,2,3,'"
    repr(s.lstrip('*@_')) # "'1,2,3,__*_'"
    repr(s.strip('*@_')) # "'1,2,3,'"

format и f-строка

    import requests
    resp = requests.get('https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str')
    st = 'Url is {0.url}, status code {0.status_code}'
    st.format(resp) # 'Url is https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str, status code 200'
    




    
"""