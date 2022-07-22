"""
sources:
    https://docs.python.org/3/reference/datamodel.html#object.__lt__


Магические методы сравнения

__eq__ - ==
__ne__ - !=
__lt__ - <
__le__ - <=
__gt__ - >
__ge__ - >=

Для всех них (self, other)

Как правило достаточно релаизовать только __eq__  и  __lt__, __le__ или __gt__, __ge__



Чтобы не реализовывать все магические методы сравнения, можно использовать декоратор
functools.total_ordering, который позволяет  сократить код, реализовав только методы __eq__ и __lt__

from functools import total_ordering


@total_ordering
class Account:
    def __init__(self, balance):
        self.balance = balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance


---------------- __hash__()

    print(object().__hash__()) # 147575908553

    hasattr(list, '__hash__') # True

Таким образом возможность хеширования у list, dict, set отменяется (скорее всего так)
ведь она есть уде у object и может вызываться

    class C:
        pass

    hash(C()) # 147576238505

по умолчанию  у классов которые мы создаём хеширование уже есть
но когда мы определяем метод __eq__(), то хеширование слетает
и наш класс становится нехешированным объектом

    class C:
        def __eq__(self, other):
            return True

    hash(C()) # TypeError: unhashable type: 'C'

Если хочешь вернуть хеширование, то определи метод __hash__(self)
и верни результат чего либо хеширования - hash(<some_obj>)

class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __eq__(self, other):
        какое-то сравнение

    def __hash__(self):
        return hash(
        (self.a, self.b,)
        )
"""


class Rectangle(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ call')
        if isinstance(other, type(self)):
            return self.a == other.a and self.b == other.b

    def __gt__(self, other):
        print('__gt__ call')
        if isinstance(other, type(self)):
            return self.area > other.area
        elif isinstance(other, (int, float)):
            return self.area > other

    def __ge__(self, other):
        print('__ge__ call')
        return self > other or self == other


# задание 3.4.2
from operator import (
    lt, gt, eq,
)


class ChessPlayer:
    def __init__(self, name, surname, rating):
        self.name = name
        self.surname = surname
        self.rating = rating

    def operation(self, action, other):
        if isinstance(other, int):
            return action(self.rating, other)
        elif isinstance(other, type(self)):
            return action(self.rating, other.rating)
        else:
            return 'Невозможно выполнить сравнение'

    def __eq__(self, other):
        return self.operation(action=eq, other=other)

    def __lt__(self, other):
        return self.operation(action=lt, other=other)

    def __gt__(self, other):
        return self.operation(action=gt, other=other)
