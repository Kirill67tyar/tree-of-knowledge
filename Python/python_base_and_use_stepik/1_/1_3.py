# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())

from pprint import pprint as pp
import sys



# pp(globals())
# pp(sys.implementation)
# pp(sys.api_version)

# 1.3.2 -------------------------------------------------

# def f():
#     """
#     та-ша
#     """
#     return 'a'
#
# lf = lambda x: x ** 2
#
# print(f)  # <function f at 0x0000027D93A2CEE0>
# print(lf)  # <function <lambda> at 0x0000027D93D50E50>
# ff = f
# print(type(f))  # <class 'function'>
# print(type(lf))  # <class 'function'>
# pp(dir(lf))
# pp(lf.__name__)  # '<lambda>'
# pp(f.__name__)  # 'f'
# pp(ff.__name__)  # ТОЖЕ 'f'
#
# pp(type(lf).mro())
# print()
# pp(globals())
#
# help(f)

# 1.3.6 -------------------------------------------------

# sources:
# https://pythontutor.com/

# Наглядная иллюстрация стека вызова

# def g():
#     print(f'Hello from function {g.__name__} ({g})')
#
# def f():
#     print(f'I am in function {f.__name__} ({f})')
#     g()
#     print(f'I am in function {f.__name__} ({f})')
#
#
# print('I am outside of any function')
# f()
# print('I am outside of any function')

# # самая базовая концепция стека вызовов
# # то что когда функция вызывается - функция кладётся на стек
# # когда она завершает исполнение - функция снимается со стека

# # В самом низу стека находится функция module
# # эта функция занимается тем, что исполняет наши запросы


#
# # если мы вызываем функцию в теле функции, то внешняя
# # то внешняя функция не может завершиться раньше
# # чем та функция которую мы вызвали в теле внешней функции
# # если же мы вызываем функцию, передавая её в аргумент
# # то конечно, эта функция сначала выполнится
# # и только потом начнёт выполняться функция, куда мы передали аргумент
# # вернее начнёт происходить инициализация, а потом выполнение
# # т.е. в таком коде
# print(g())
# # функция g() не ложится на функцию print()
# # в стеке вызовов, она сначала полностью выполнится
# # а потом уже начнёт выполняться функция print()
# # с инициализацией и т.д.

# # упражнение для подсчёта функций в стеке вызовов
# # как максимальное количество функций будет в стеке:
# def h():
#   print(12)
#
# def f():
#   g(h)
#
# def g(a):
#   a()
#
# g(f)

# # пример того, что функции которые мы определяем и вызываем
# # не являются ленивыми функциями
# ls = []
# def f(value):
#     ls.append(value)
#
# x = f(15)
# print(ls)

# 1.3.10 -------------------------------------------------

# ----- варианты передачи аргументов
# def f(a, b):
#     pass
#
# ob1 = f(5, 6)
# ob2 = f(5, b=6)
# ob3 = f(b=5, a=6)
#
# args = [1, 2, ]
# ob4 = f(*args)
#
# kwargs = {'a': 5, 'b': 6, }
# ob5 = f(**kwargs)
# ----- варианты передачи аргументов

# 1.3.12 -------------------------------------------------
# шаблон передачи аргументов в функцию
# (в [] значит не обязательно)

# def function( [positional_args,
#               [positional_args_with_default,
#               [*args,
#               [keyword_only_args, # блок аргументов, которые можно передать только по имени
#               [**kwargs]]]]]):
# def printab(a, b=5, *args, c=7, d, **kwargs):
#     return (a, b, args, c, d, kwargs,)
#
# printab(10, d=20)

# !!! ATTENTION !!!
# при функции def func(a, b=2, *args, **kwargs): pass
# если мы её вызываем, то аргумент b, если передавать его по имени
# может идти только после args
# func(1,2,3,b=4) # 2,3 будут таплом args
# func(1,2,3,4) # 2 будет аргументом b, 3,4 будут таплом args
# !!! ATTENTION !!!