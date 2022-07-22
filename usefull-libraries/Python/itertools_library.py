"""
sources:
    https://pythonworld.ru/moduli/modul-itertools.html
    https://docs.python.org/3/library/itertools.html

    комбинаторика (для permutations, combinations, combinations_with_replacement)
    https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%82%D0%BE%D1%80%D0%B8%D0%BA%D0%B0

модуль itertools содержит функции для работы с итераторами, и создания итераторов

 -- product
    декартово произведение итераторов (для избегания вложенных циклов for)

 -- permutations (перестановки)
    генераци перестановок

 -- combinations
    генераци сочетаний

 -- combinations_with_replacement
    генераци размещений

 -- chain
    соединение нескольких итераторов в один

 -- takewhile
    получение значений последовательности, пока
    значение функции-предиката для её элементов истинно

 -- dropwhile
    получение значений последовательности начиная с элемента,
    для которого значение функции-предиката перестаёт быть истинно

В паре takewhile и dropwhile позволяют последовательность разбить
на две части

"""
from pprint import pprint as pp
from itertools import (
    product, chain,
    permutations,
    combinations,
    combinations_with_replacement,
    takewhile, dropwhile,
)
import time


# -------------------------------------------------------------------------
# product - прекрасно заменяет вложенные циклы


# for i in range(1, 5):  # без функции product
#     for j in range(1, 5):
#         print(f'{i} * {j} = {i * j}')
# print()
# for i, j in product(range(1, 5), range(1, 5)):  # с функцией product
#     print(f'{i} * {j} = {i * j}')

# но эта функция синтаксический сахар и Python
# работает с ней медленне, сравни
def compare_time(data):
    start = time.time()
    data()
    return time.time() - start


def loops():
    for i in range(1, 100):
        for j in range(1, 100):
            for l in range(1, 100):
                a = i + j + l


def loops_product():
    for i, j, l in product(range(1, 100), range(1, 100), range(1, 100)):
        a = i + j + l


for i in range(10):
    # print()
    # print(compare_time(loops))
    # print(compare_time(loops_product))
    pass
# -------------------------------------------------------------------------

# chain - склеивает циклы вместе
for i in range(1, 5):  # без функции chain
    # print(i)
    pass
for j in range(1, 5):
    # print(j)
    pass
# print()
for i in chain(range(1, 5), range(1, 5)):  # с функцией chain
    # print(i)
    pass

# Проверять не буду но chain тоже скорее всего замедляет циклы
# -------------------------------------------------------------------------

# permutations (перестановки)
# combinations (комбинации)
# combinations_with_replacement (комбинации с заменой)
# Эти функции для комбинаторики


string = 'ABC'
elements = 2
# print(list(permutations(string, elements)))
## [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# print(list(combinations(string, elements)))
## [('A', 'B'), ('A', 'C'), ('B', 'C')]

# print(list(combinations_with_replacement(string, elements)))
## [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# -------------------------------------------------------------------------

# takewhile
# dropwhile

values = [1, 4, 3, 5, 3, 2, 8, ]
predicate = lambda x: x < 5
## все элементы что соответствуют True, до первого False, дальше не интересуют
print(list(takewhile(predicate, values))) # [1, 4, 3]

## с первого False и до самого конца, даже если остальные True
print(list(dropwhile(predicate, values))) # [5, 3, 2, 8]
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
