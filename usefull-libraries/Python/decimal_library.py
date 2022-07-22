"""
sources:
    https://docs.python.org/3/library/decimal.html
    https://pyprog.pro/python/st_lib/decimal.html

from pprint import pprint as pp
help(Decimal)
print(' -- ' * 20)
pp(dir(Decimal))
print(' -- ' * 20)
pp(Decimal.mro())
print(' -- ' * 20)
pp(Decimal.__dict__)

Модуль decimal предоставляет более точные числа с плавающей точкой

float -- 0.1 + .2 # 0.30000000000000004

decimal -- Decimal('0.1') + Decimal('0.2') # 0.3
           Decimal(0.1) + Decimal(0.2) # 0.3000000000000000166533453694

'value' can be an integer, string, tuple, or another Decimal object

В django есть поле для моделей DecimalField
который сохраняет данные в бд в типе данных DECIMAL

Т.е. такой тип данных есть и в SQL

Тип данных класса Decimal, модуля decimal - <class 'decimal.Decimal'>

    d = Decimal('0.5') + Decimal('23.342')
    print(type(d)) # <class 'decimal.Decimal'>

С этим типом данных можно выполнять любые арифметические операции

Очень много методов:
pp(dir(Decimal))

Очень полезен для работы с валютой

Важно!!
для Decimal доступны типы данных str, int, float и даже tuple
но лучше использовать str

"""
from pprint import pprint as pp
from decimal import Decimal

print(Decimal('0.1') + Decimal('0.2')) # 0.3
print(Decimal(0.1) + Decimal(0.2)) # 0.3

d = Decimal('0.1') + Decimal('0.2')
# print(type(d)) # <class 'decimal.Decimal'>
# help(Decimal)
# print(' -- ' * 20)
pp(dir(Decimal))
# print(' -- ' * 20)
# pp(Decimal.mro())
# print(' -- ' * 20)
# pp(Decimal.__dict__)