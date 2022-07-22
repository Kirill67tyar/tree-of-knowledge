from pprint import pprint as pp

r"""
sources:
    https://habr.com/ru/post/349860/
    https://tproger.ru/translations/regular-expression-python/
    https://docs.python.org/3/library/re.html
    
    метасимволы
    https://desktop.arcgis.com/ru/arcmap/latest/extensions/data-reviewer/metacharacters-used-to-build-regular-expressions.htm
    
    на английском хорошие материалы
    https://www.regular-expressions.info/
    
    сервис для отладки и тестирования регулярных выражений (выбери Python)
    https://regex101.com/
    
    Онлайн визуализация регулярок (не забудьте выбрать Python)
    https://www.debuggex.com/
    

Регулярные выражения - мощный инструмент, для поиска в тексте

в Python предоставляются стандартной библиотекой re

"Сырые" строки - подавляют экранирование
Если перед открывающей кавычкой стоит символ 'r' (в любом регистре), то механизм экранирования отключается.

Сырые строки используют тогда, когда нужно в записи строки использовать обратный слеш. 
В частности, в регулярных выражениях.

в обчгых строках мы используем обратный слеш, чтобы заэкранировать
какой-нибедь символ

    >>> "qwe \" fds"
    'qwe " fds'
    >>> "qwe " fds" # SyntaxError: invalid syntax
    
Чтобы указать интерпретатору, что строки нужно использовать 
ровно с теми символами, которые в них указаны, 
нужно поставить перед строкой r (так называемая сырая строка)

    r
    print(r"asd \n dsa") # asd \n dsa
    print(repr(r"asd \n dsa")) # 'asd \\n dsa'
    
    без r
    print("asd \n dsa")asd 
                         dsa
    print(repr("asd \n dsa")) # 'asd \n dsa'
                        


----- метасимволы

[] - множество, которое под шаблон подходит
     можно указать множество подходящих символов

pattern = r'abc'

pattern = r'a[abc]c' - означает, что вторым символом строки может являться не только b но также a и c

======================================================================Метасимволы:
. ^ $ * + ? { } [ ] \ | ( ) — метасимволы

[ ] — можно указать множество подходящих символов
^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не-цифра в начале строки).
\d ~ [0-9] — цифры
\D ~ [^0-9]
\s ~ [ \t\n\r\f\v] — пробельные символы
\S ~ [^ \t\n\r\f\v]
\w ~ [a-zA-Z0-9_] — буквы + цифры + _
\W ~ [^a-zA-Z0-9_]

[] множество символов
[abc]
[a-c]
======================================================================

----- re


# 3.2.7
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if len(findall(r'cat', line)) >= 2:
#         answer.append(line)
# print(*answer, sep='\n')
#
#
# 3.2.8
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if search(r'\bcat\b', line):
#         answer.append(line)
# print(*answer, sep='\n')
#
# 3.2.9
# answer = []
# for line in sys.stdin:
#     line = line.rstrip()
#     # if line.find('cat') != -1:
#     #     if line.count('cat') >= 2:
#     #         answer.append(line)
#     # or
#     if search(r'z.{3}z', line):
#         answer.append(line)
# print(*answer, sep='\n')



# 3.2.10
# import sys
# from re import findall, search
# answer = [line.rstrip() for line in sys.stdin if findall(r'\\', line)]
# print(*answer, sep='\n')


# # 3.2.11
# import sys
# from re import findall, search
# answer = [line.rstrip() for line in sys.stdin if findall(r'\b(\w+)\1\b', line)]
# print(*answer, sep='\n')


# # 3.2.13
# import sys
# from re import IGNORECASE, sub
# answer = [sub(r'\b([aA])+\b', 'argh', line, count=1, flags=IGNORECASE).strip() for line in sys.stdin]
# print(*answer, sep='\n')


# # 3.2.14
# import sys
# from re import IGNORECASE, sub
# # answer = [sub(r'\b(\w)(\w)(\w+)', r'\2\1\3', line, flags=IGNORECASE).strip() for line in sys.stdin]
# answer = [sub(r'\b(\w)(\w)+?', r'\2\1', line, flags=IGNORECASE).strip() for line in sys.stdin]
# print(*answer, sep='\n')


# # 3.2.15
# import sys
# from re import IGNORECASE, sub, findall
# answer = []
# for line in sys.stdin:
#     if findall(r'(\w)\1+', line):
#         answer.append(sub(r'(\w)\1+', r'\1', line.strip()))
#     else:
#         answer.append(line.strip())
# print(*answer, sep='\n')

"""














