"""

pp(dir(functools))
help(functools)
print(functools.__doc__)

sources:
    https://pythonworld.ru/moduli/modul-functools.html
    https://pythonim.ru/moduli/functools-python

Модуль functools - сборник функций высокого уровня:
взаимодействующих с другими функциями или возвращающие другие функции.

 -- reduce

аналог функции, который выдаёт последовательность фибоначчи

    from functools import reduce
    print(reduce(lambda x,y: x + y, range(1,11))) # 55

т.е. нужно передать в reduce функцию,
которая принимает два аргумента, что-то с ними делает,
(вычитает, умножает, складывает)
и выдаёт один аргумент

т.е. эта функция делает что-то с двумя первыми элементами,
а затем с результатом вычислений этих элементов со следующим и т.д.

просто запомни аналогию, - фибоначчи, тоже самое, но доступно не только сложение

 -- iru_cache
 декоратора, который кеширует значение функций, которые не меняют свой результат
 при неизменных аргументах;

 полезен для:
  - кеширования данных (различного рода запросов),
  - мемоизации (сохранения результатов для возврата без вычисления функций)
  - значений рекурсивных функций (например, такого типа, как функция
    вычисления n-го числа Фибоначчи) и т.д.

 iru_cache полезна, когда функция является чистой, и при тех же аргументах
 выдаёт тот-же самый результат

 -- partial
 частичное применение функции (вызов функции с меньшим кол-вом аргументов,
 чем она ожидает, и получение функции, которая принимает оставшиеся параметры)
"""
from pprint import pprint as pp
from functools import reduce, lru_cache, partial

# -------------------------------------------------------------------------
#  reduce
# работает как fibonacci, но доступно не только сложение
fibonacci_reduce = lambda count: reduce(lambda x,y: x + y, range(count+1))

def fibonacci(count):
    first, second = 0, 1
    result = 0
    for i in range(count):
        result = second
        first, second = second, second + first
    return result

# print(fibonacci_reduce(10)) # 55
# print(fibonacci(10)) # 55
# print(fibonacci(100)) # 354224848179261915075
# -------------------------------------------------------------------------
# @wraps

def decor(func, *args, **kwargs):

    @wraps(func)
    def inner(*args, **kwargs):
        print('something happening')
        return func(*args, **kwargs)

    return inner

# @wrap заменяет
#               inner.__name__ = func.__name__
#               inner.__doc__ = func.__doc__

# -------------------------------------------------------------------------
 # @lru_cache
#  очень полезная функция для кеширования
# пример рекурсивной функции
@lru_cache(maxsize=None) # maxsize=None - максимальное значение не ограничени
def fibonacci_recurs(value):
    if value == 1 or value == 2:
        return 1
    return fibonacci_recurs(value - 1) + fibonacci_recurs(value - 2)

# считает довольно долго
# без декоратора
# print(fibonacci_recurs(10)) # 55
# print(fibonacci_recurs(20)) # 6765
# print(fibonacci_recurs(30)) # 832040
# print(fibonacci_recurs(40)) # 102334155 но это будет вычислять уже очень долго

# попробуй включи декоратор и отключи
for i in range(1, 101):
    # print(fibonacci_recurs(i))
    pass

# -------------------------------------------------------------------------
# partial
# позволяет частично применять функции
# частичное применение фунции - применение её не ко всем аргументам,
# которые её ожидают, а только к части из них, и получение
# новой функции, которая будет брать все оставшиеся аргументы

def add(x):
    def func(y):
        return x + y
    return func

add_to_five = add(5)
# print(add_to_five(10)) # 15

# или
def add2(x, y):
    return x + y

add_to_five2 = partial(add2, 5)
# print(add_to_five2(100)) # 105

# причём к функции partial можно применять не только
# позиционные аргументы но и именованные

# хороший пример:

p = partial(print, sep='\n', end='\n' + '-' * 50)

# p(*dir(list))

# ещё один хороший пример

# принимаем число в двоичной системе и показывем его значение
print(int('1101', base=2)) # 13

# специальная функция, которая приводит двоичное число в десятиричное
int_2 = partial(int, base=2)
print(int_2('1101'))# 13




