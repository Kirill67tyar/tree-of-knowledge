"""
sources:
    https://docs.python.org/3/library/random.html
    https://pythonworld.ru/moduli/modul-random.html

Основаная функция - random.random()

в типе данных float, количество цифр после запятой
Все остальные функции зависят от неё и
работают на основе неё

Все функции этого модуля random

являются методами скрытого экземпляра класса random.Random

    print(random.Random) # <class 'random.Random'>
    print(random.Random.mro()) # [<class 'random.Random'>, <class '_random.Random'>, <class 'object'>]

При импортировании этого модуля создаётся скрытый экземпляр, класса Random
и все методы этого экземпляра импортируются в пространство имён модуля
примерно как

    random = _random_instance.random

Ну и так далее

В этом модуле есть также класс SystemRandom

    print(random.SystemRandom) # <class 'random.SystemRandom'>
    pp(random.SystemRandom.mro()) # [<class 'random.SystemRandom'>,
                                    #   <class 'random.Random'>,
                                    #  <class '_random.Random'>,
                                    #  <class 'object'>]

класс Random реализован на Python
класс SystemRandom использует системный вызов для получения случайного числа
Короче число получается более случайным

    systrand = random.SystemRandom()
    print(systrand.random())

число получится более случайным, сложнее будет найти закономерность
на более низком уровне SystemRandom подбирает случайность
Может быть полезно для криптографии
"""
from pprint import pprint as pp
import random


# # ----------------------------------------
# # Узнаём какое минимальное и максимальное кол-во цифр после запятой у random.random()
#
# # Предоставляет рандомное число от 0 до 1
# # Minimum count of digits after dot: 10
# # Maximum count of digits after dot: 20
# # Average value: 16.269686

#
# data = []
# for i in range(1000000):
#     data.append(len(str(random.random()).split('.')[-1]))
#
# min_value = min(data)
# max_value = max(data)
#
# average = sum(data) / len(data)
#
# print('Minimum count of digits after dot: {}'.format(min_value))
# print('Maximum count of digits after dot: {}'.format(max_value))
# print('Average value: {}'.format(average))
# # ----------------------------------------

# ----------------------------------------
# 1)
random.uniform(1, 100)
for i in range(10):
    # print(random.uniform(1, 100))
    pass

# 2)
random.shuffle(['a', 'b', 'c', ]) # перемешивает изменяемую последовательность
ls = list(range(100))
random.shuffle(ls)
# print(ls)
# здесь работать не будет т.к. tuple не изменяемый тип данных
t = random.shuffle(tuple(range(-100,1,-1)))
# print(t)

# 3)
random.Random
# print(random.Random)
# pp(random.Random.mro())

# 4)
random.SystemRandom
# print(random.SystemRandom)
# pp(random.SystemRandom.mro())
systrand = random.SystemRandom()
pp(systrand.random())
# ----------------------------------------
