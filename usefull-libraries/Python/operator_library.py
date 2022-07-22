"""
sources:
    https://codecamp.ru/blog/python-operator-module/
    https://docs.python.org/3/library/operator.html

Модуль operator содержит функции, которые соответствуют стандартным операторам

название этих функций такие же как и сооветствующие данным операциям специальные методы
только без символов подчёркивания
Можно напимать аналог этих функций с помощью lambda выражения,
но эти функции работают быстрее, чем аналог написанный
с помощью lambda

operator:           аналогичная lambda-функция:
 - add                  - lambda x, y: x + y
 - gt                   - lambda x, y: x > y
 - neg                  - lambda x: -x

В чисто функциональных языках все операциии являются функциями

__all__ = ['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains', 'countOf',
           'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt', 'iadd', 'iand',
           'iconcat', 'ifloordiv', 'ilshift', 'imatmul', 'imod', 'imul',
           'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift',
           'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le',
           'length_hint', 'lshift', 'lt', 'matmul', 'methodcaller', 'mod',
           'mul', 'ne', 'neg', 'not_', 'or_', 'pos', 'pow', 'rshift',
           'setitem', 'sub', 'truediv', 'truth', 'xor']

Кстати, как видно ниже в коде, эти функции работают быстрее
чем лямбда выражения

print('\n', 'Results comparing:')
print(sum(result_for_lambda) / len(result_for_lambda)) # 0.01078040361404419
print(sum(result_for_neg) / len(result_for_neg)) # 0.005010695457458496

Причём если судить по это выборке то в два раза быстрее
0.01078040361404419 для lambda выражения против
0.005010695457458496 для фунции neg
"""
from pprint import pprint as pp
from operator import neg, add, sub, mul, truediv, itemgetter, attrgetter
import time
from string import printable
from random import shuffle
# ls = [4, 1, 5, 3, 3, 2, 1, -5, ]
#
# # neg
# print(list(map(neg, ls)))  # [-4, -1, -5, -3, -3, -2, -1, 5]
#
#
# # -------------------------------------------------------------------------
# def compare_time(data):
#     start = time.time()
#     data()
#     return time.time() - start
#
#
# # -------------------------------------------------------------------------
# # сравнение функции neg с lambda x: -x
# # по скорости (neg быстрее в два раза)
#
# lst = list(range(1, 100000))
#
#
# def f():
#     result = list(map(lambda x: -x, lst))
#     return result
#
#
# def ff():
#     result = list(map(neg, lst))
#     return result
#
#
# result_for_lambda = []
# result_for_neg = []
#
# for i in range(1000):
#     print()
#     elem_for_lambda = compare_time(f)
#     elem_for_neg = compare_time(ff)
#     # print(elem_for_lambda)
#     # print(elem_for_neg)
#     result_for_lambda.append(elem_for_lambda)
#     result_for_neg.append(elem_for_neg)
#
# print('\n', 'Results comparing:')
# print(sum(result_for_lambda) / len(result_for_lambda))  # 0.01078040361404419
# print(sum(result_for_neg) / len(result_for_neg))  # 0.005010695457458496
#
# # на сколько бысрее работа neg
# print(sum(result_for_lambda) - sum(result_for_neg))  # 5.743523359298706

# -------------------------------------------------------------------------
# # itemgetter и attrgetter странные функции.
#
# # itemgetter
# ls = [1,2,3,4,5,]
# d = {'key': ['some value']}
# key = itemgetter('key')
# index = itemgetter(-1)
# print(key(d)) # ['some value']
# print(index(ls)) # 5
#
#
# ls = [5,3,2,3,5,3,2,1,121,32,1]
# attr = attrgetter('sort')
# attr(ls)()
# print(ls)
# print(attr(ls)) # <built-in method sort of list object at 0x000001A5AA268B00>


# print(len(printable))
for_values = printable * 10000 # создаём ключи
# print(len(for_values)
vals = []
for i in range(len(for_values)):
    vals.append(for_values[i] + str(ord(for_values[i])) + str(i))
ls = list(zip(range(10000), vals)) # создаём список с 10000 уникальными ключами:значениями

shuffle(ls) # перемешиваем его
pp(ls)

def f():
    data = ls.copy()
    # data.sort(key=lambda x : x[-1])
    index = itemgetter(-1)
    data.sort(key=index)

def compare(func):
    start = time.time()
    func()
    return time.time() - start

results = []
for i in range(1000):
    results.append(compare(f))

print(sum(results))
print(sum(results) / 10)


"""
X 10
для key=lambda x : x[-1]
0.03931236267089844
0.003931236267089844

для index = itemgetter(-1)
    data.sort(key=index)
0.02620553970336914
0.002620553970336914


X100 
для key=lambda x : x[-1]
0.3746013641357422
0.03746013641357422

для index = itemgetter(-1)
    data.sort(key=index)
0.3558955192565918
0.03558955192565918


X1000
для key=lambda x : x[-1]
3.0002787113189697
0.300027871131897

для index = itemgetter(-1)
    data.sort(key=index)
2.6591684818267822
0.26591684818267824




Таким образом делаем вывод, что itemgetter и lambda работают +- одинаково
возможно itemgetter чуть быстрее
"""
# def f():
#     ls =
# -------------------------------------------------------------------------
