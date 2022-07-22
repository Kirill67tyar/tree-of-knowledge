"""
sources:
    https://pythonworld.ru/moduli/modul-fractions.html
    https://docs.python.org/3/library/fractions.html
    https://skysmart.ru/articles/mathematic/chto-takoe-racionalnye-chisla

from pprint import pprint as pp
help(Fraction)
print(' -- ' * 20)
pp(dir(Fraction))
print(' -- ' * 20)
pp(Fraction.mro())
print(' -- ' * 20)
pp(Fraction.__dict__)

Модуль fractions предоставляет поддержку рациональных чисел.
для дробей можно сказать

Всё также, можно производить любые математические операции, кроме
извлечения корня (** 0.5)
"""
from pprint import pprint as pp
from decimal import Decimal
from fractions import Fraction

print(1 / 3)  # 0.3333333333333333

print(Decimal('1') / Decimal('3'))  # 0.3333333333333333333333333333

print(Fraction('1') / Fraction('3'))  # 1/3

print(Fraction(1, 3))  # 1/3

print(repr(Fraction(1, 3)))  # Fraction(1, 3)

print(Fraction(-3.14))  # -7070651414971679 / 2251799813685248
print(Fraction(-34.16))  # -1201898150554501 / 35184372088832
