"""
sources:
    https://docs.python.org/3/library/re.html
    https://docs.python.org/3/howto/regex.html
    https://pyneng.readthedocs.io/ru/latest/book/15_module_re/
    https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D0%B3%D1%83%D0%BB%D1%8F%D1%80%D0%BD%D1%8B%D0%B5_%D0%B2%D1%8B%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F

    регулярные выражения
    https://habr.com/ru/post/349860/
    https://tproger.ru/translations/regular-expression-python/
    https://docs.python.org/3/library/re.html

    метасимволы
    https://desktop.arcgis.com/ru/arcmap/latest/extensions/data-reviewer/metacharacters-used-to-build-regular-expressions.htm

    группировка в метасимволах
    https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/grouping-constructs-in-regular-expressions
    https://ru.hexlet.io/courses/regexp/lessons/backreferences/theory_unit


pp(dir(re))
help(re)
print(re.__doc__)

4 основные функции
print(re.match.__doc__)
print(re.search.__doc__)
print(re.findall.__doc__)
print(re.sub.__doc__)


шаблон регулярных выражений, для поиска абсолютного url:

    r'hrefs*=s*("([^"]*")|\'[^\']*\'|([^\'">s]+))'



Регулярные выражения — специальная последовательность символов,
которая помогает сопоставлять или находить строки python с
использованием специализированного синтаксиса, содержащегося в шаблоне.
Регулярные выражения распространены в мире UNIX.

Модуль re предоставляет полную поддержку выражениям, подобным Perl в Python.
Модуль re поднимает исключение re.error, если возникает ошибка
при компиляции или использовании регулярного выражения.

Здесь регулярное выражение == шаблон

4 основные функции (но их больше):

 - match
 - search
 - findall
 - sub

--- match
Берёт шаблон, берёт строку, и проверяет подходит ли строка
под данный шаблон

--- search
находит первую подстроку, которая подходит под шаблон

--- findall
находит все подстроки строки, которые подходят под шаблон

--- sub
позволяет заменить все входждения подстрок, которые подходят под шаблон
чем-гибудь другим

Важно помнить, что метасимвол + жадный метасимвол (вбирает в себя как можно больше возможных комбинаций).
приницип прост:
сначала пытается выбрать строку максимальной длины, которая нам удовлетворяет,
а затем проверить - то что осталось от строки, оно подходит под остаток шаблона,
который у нас остался
Если нет, то мы один символ с конца выкинем, и снова проверим



----- флажки
    ASCII = A = sre_compile.SRE_FLAG_ASCII # assume ascii "locale"
    IGNORECASE = I = sre_compile.SRE_FLAG_IGNORECASE # ignore case
    LOCALE = L = sre_compile.SRE_FLAG_LOCALE # assume current 8-bit locale
    UNICODE = U = sre_compile.SRE_FLAG_UNICODE # assume unicode "locale"
    MULTILINE = M = sre_compile.SRE_FLAG_MULTILINE # make anchors look for newline
    DOTALL = S = sre_compile.SRE_FLAG_DOTALL # make dot match newline
    VERBOSE = X = sre_compile.SRE_FLAG_VERBOSE # ignore whitespace and comments
    # sre extensions (experimental, don't rely on these)
    TEMPLATE = T = sre_compile.SRE_FLAG_TEMPLATE # disable backtracking
    DEBUG = sre_compile.SRE_FLAG_DEBUG # dump pattern after compilation

Флаги можно использовать и с | (or) т.е. сраз несколько флагов

IGNORECASE = I = (pattern=pattern, string=string, flags=re.IGNORECASE) игнорирование строчный или заглавный текст
ASCII = A = (pattern=pattern, string=string, flags=re.ASCII)
LOCALE = L = (pattern=pattern, string=string, flags=re.LOCALE)
UNICODE = U = (pattern=pattern, string=string, flags=re.U)
MULTILINE = M = (pattern=pattern, string=string, flags=re.M)
DOTALL = S = (pattern=pattern, string=string, flags=re.S)
VERBOSE = X = (pattern=pattern, string=string, flags=re.VERBOSE)
TEMPLATE = T = (pattern=pattern, string=string, flags=re.T)
DEBUG = (pattern=pattern, string=string, flags=re.DEBUG) распаковывает, как это всё выглядит


----- метасимволы


[] - множество, которое под шаблон подходит
     можно указать множество подходящих символов

pattern = r'abc'

pattern = r'a[abc]c' - означает, что вторым символом строки может являться не только b но также a и c

т.е. aac, abc acc == r'a[abc]c'

Позволяет расширить список строк, которые подходят под наш шаблон


====================================================================== Метасимволы:
target="_top"
. ^ $ * + ? { } [ ] \ | ( ) — метасимволы

[ ] — можно указать множество подходящих символов
^ - карет, обозначает либо начало строки, либо инвертирование группы символов.
(например: "^[^0-9]" — не-цифра в начале строки).
\d ~ [0-9] — цифры
\D ~ [^0-9]
\s ~ [ \t\n\r\f\v] — пробельные символы
\S ~ [^ \t\n\r\f\v]
\w ~ [a-zA-Z0-9_] — буквы + цифры + _
\W ~ [^a-zA-Z0-9_]

* ~ любое кол-во символа
+ ~ положительное вхождение символа (больше 0)
? ~ 0 или 1 вхождение символа
[] множество символов
[abc]
[a-c]
{} кол-во сколько раз входит (ставится цифра в {})
{5} - 5 раз
{1,3} - от одного до 3
() - групировка нескольких символов

Важно помнить, что метасимвол + жадный метасимвол (вбирает в себя как можно больше возможных комбинаций).
приницип прост:
сначала пытается выбрать строку максимальной длины, которая нам удовлетворяет,
а затем проверить - то что осталось от строки, оно подходит под остаток шаблона,
который у нас остался
Если нет, то мы один символ с конца выкинем, и снова проверим
======================================================================
"""
from pprint import pprint as pp
from analizetools.analize import (
    p_dir, p_type
)
from re import (
    match,
    search,
    findall,
    sub,
)


# match - подходит ли строка под шаблон                                             print(re.match.__doc__)
# search - находит первую подстроку, которая подходит под шаблон                    print(re.search.__doc__)
# findall - находит все подстроки строки, которые подходят под шаблон               print(re.findall.__doc__)
# sub - позволяет заменить все входждения подстрок, которые подходят под шаблон     print(re.sub.__doc__)
#          чем-гибудь другим


# # match ------------------------------------------------------------------------------
# # print(re.match.__doc__)
# # help(re.math)
# # pp(dir(re.match))
# # match(pattern, string, flags=0)
# pattern = r'abc'
#
# # 1
# string = 'abclnlsd'
# match_object = match(pattern=pattern, string=string)
# print(match_object) # <re.Match object; span=(0, 3), match='abc'>
# # span=(0, 3) - позволяет понять, с какой и по какой индекс строки
# # находится вхождение шаблона в строку
# # 2
# string2 = 'qbclnlsd'
# match_object2 = match(pattern=pattern, string=string2)
# print(match_object2) # None
# # 3
# string3 = 'babclnlsd'
# match_object3 = match(pattern=pattern, string=string3)
# print(match_object3) # None
# # потому что хоть в babclnlsd и есть abc, начинается она не с abc
# # для этого есть функция search

# # 4
patter_with_all_letters = r'(test)'
patter_with_all_letters2 = r'(test|text)' #
patter_with_all_letters3 = r'abc|(test|text)' #
# patter_with_all_letters4 = r'ab{3}c' # {} кол-во сколько раз входит (здесь 3)
# patter_with_all_letters5 = r'ab{2,4}c' # от 2 до 4 вхождений
string = 'test'
string2 = 'testtest'
string3 = 'testtext'
string4 = 'abc'
print(match(pattern=patter_with_all_letters, string=string)) # <re.Match object; span=(0, 4), match='test'>
print(match(pattern=patter_with_all_letters2, string=string)) # <re.Match object; span=(0, 4), match='test'>
print(match(pattern=patter_with_all_letters2, string=string2)) # <re.Match object; span=(0, 4), match='test'>
print(match(pattern=patter_with_all_letters2, string=string3)) # <re.Match object; span=(0, 4), match='test'>
print(match(pattern=patter_with_all_letters3, string=string4)) # <re.Match object; span=(0, 3), match='abc'>






# # search ------------------------------------------------------------------------------
# # print(re.search.__doc__)
# # help(re.search)
# # pp(dir(re.search))
# # match(pattern, string, flags=0)
# pattern = r'abc'
# string3 = 'babclnlsd'
# search_object = search(pattern=pattern, string=string3)
# print(search_object)  # <re.Match object; span=(1, 4), match='abc'>
# # span=(1, 4) - показывает с какой и по какой индекс вхождение в строку
# # те же самые числа, что вернулись бы при слайсинге
#
# # # 2
# pattern2 = r'a[abc]c' # [] - здесь множество подходящих символов
# string2 = 'wabclnlsd'
# string3 = 'wacclnlsd'
# string4 = 'waaclnlsd'
# search_object2 = search(pattern=pattern2, string=string2)
# search_object3 = search(pattern=pattern2, string=string3)
# search_object4 = search(pattern=pattern2, string=string4)
# print(search_object2) # <re.Match object; span=(1, 4), match='aac'>
# print(search_object3) # <re.Match object; span=(1, 4), match='aac'>
# print(search_object4) # <re.Match object; span=(1, 4), match='aac'>
#
# # p_dir(search_object)

# # 3
string = 'Do you speak english?'
pattern = r'english?'
pattern2 = r'english\?'
search_object = search(pattern=pattern, string=string)
search_object2 = search(pattern=pattern2, string=string)
print(search_object) # <re.Match object; span=(13, 20), match='english'>
print(search_object2) # <re.Match object; span=(13, 21), match='english?'>
p_dir(search_object2)
print(search_object2.span())
# как видишь в первом search_object поиск english? не нашёл ?, а во втором нашёл
# ? - специальное выражение, и во второй раз мы поставили обратный слеш.


# # findall ------------------------------------------------------------------------------
# здесь ещё рассмотрены метасимволы
# pattern = r'a[abc]c' # [] - здесь множество подходящих символов
# pattern = r'a[a-d]c' # [] - здесь множество подходящих символов
# string = 'abc acc aac zxc'
# all_inclusions = findall(pattern=pattern, string=string)
# print(all_inclusions) # ['abc', 'acc', 'aac']

# # # 2
# pattern = r'a[a-d]c' # [] - здесь множество подходящих символов
# string = 'abc acc aac zxc adc'
# all_inclusions = findall(pattern=pattern, string=string)
# print(all_inclusions) # ['abc', 'acc', 'aac', 'adc'] сравни 'abc acc aac zxc adc'

# # # 3
# patter_with_all_letters = r'a[a-zA-Z]c' # [a-zA-Z] - все буквы
# patter_with_all_letters = r'a\wc' # \w == [a-zA-Z]
# string = 'abc acc aac zxc adc aWc ACV aXc aoc'
# all_inclusions = findall(pattern=patter_with_all_letters, string=string)
# print(all_inclusions) # ['abc', 'acc', 'aac', 'adc', 'aWc', 'aXc', 'aoc']

# # # 4
# # patter_with_all_letters = r'a[^a-zA-Z]c' # [^a-zA-Z] - наоборот не подходят эти буквы после ^
# patter_with_all_letters2 = r'a\Wc' # \W == [^a-zA-Z]
# # string = 'abc acc aac zxc adc aWc ACV aXc aoc a-c a$c a...c'
# string2 = 'abc acc aac zxc adc aWc ACV aXc aoc a-c a$c a...c a.c'
# all_inclusions = findall(pattern=patter_with_all_letters2, string=string2)
# print(all_inclusions) # ['a-c', 'a$c', 'a.c']

# # # 5
# patter_with_all_letters = r'a.c' # . - означает любой один символ
# string = 'abc acc aac zxc adc aWc ACV aXc aoc a-c a$c a...c'
# all_inclusions = findall(pattern=patter_with_all_letters, string=string)
# print(all_inclusions) # ['abc', 'acc', 'aac', 'adc', 'aWc', 'aXc', 'aoc', 'a-c', 'a$c']

# # # 6
# patter_with_all_letters = r'ab*c' # * любое кол-во символов b
# patter_with_all_letters2 = r'ab+c' # + положительное ключение символа b (без ноля)
# patter_with_all_letters3 = r'ab?c' # ? 0 или 1 вхождение символа b
# patter_with_all_letters4 = r'ab{3}c' # {} кол-во сколько раз входит (здесь 3)
# patter_with_all_letters5 = r'ab{2,4}c' # от 2 до 4 вхождений
# string = 'abc abbc abbbc ac atc'
# all_inclusions = findall(pattern=patter_with_all_letters, string=string)
# all_inclusions2 = findall(pattern=patter_with_all_letters2, string=string)
# print(all_inclusions) # ['abc', 'abbc', 'abbbc', 'ac'] ac Тоже всключено, т.к. b-0
# print(all_inclusions2) # ['abc', 'abbc', 'abbbc'] ac нет т.к. здесь было b+




# # # sub ------------------------------------------------------------------------------
# # sub(pattern, repl, string, count=0, flags=0)
# pattern = r'a[abc]c' # [] - здесь множество подходящих символов
# string = 'abc acc aac zxc'
# fixed_typos = sub(pattern=pattern, repl='abc', string=string)
# print(fixed_typos) # abc abc abc zxc
# p_type(fixed_typos) # <class 'str'>
# # обрати внимание, что заменил все вхождения на repl ('abc')

