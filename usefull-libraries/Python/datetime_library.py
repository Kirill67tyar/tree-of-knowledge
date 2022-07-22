"""
sources:
    https://pythonworld.ru/moduli/modul-datetime.html
    https://docs.python.org/3/library/datetime.html

    форматы для вывода дат
    https://www.ibm.com/docs/en/cmofm/9.0.0?topic=SSEPCD_9.0.0/com.ibm.ondemand.mp.doc/arsa0257.htm

В datetime описаны 4 типа данных:

1. datetime - дата и время
2. date - только дату
3. time - только время
4. timedelta - разница между двумя точками во времени

"""
from pprint import pprint as pp

from datetime import date, time, datetime, timedelta

# pp(dir(date))
# print(date.today())

# можно установить год, число, дату, время
d = datetime(year=1984, month=8, day=5, hour=15, minute=50, second=30)
print(d)

# dd = datetime(year=1984, month=8, day=5, hour=15, minute=500, second=30) # ValueError: minute must be in 0..59
# print(dd)

dd = datetime(year=1984, month=8, day=5) # Эти три аргумента обязательны
print(dd)

# timedelta можно вычислять из time, date, datetime
# главное аргументы правильные передавать
some_day = date.today() - timedelta(days=5, hours=12, minutes=34) # 2022-04-29
print(some_day.strftime('%A, %d.%m.%y')) # Friday, 29.04.22
