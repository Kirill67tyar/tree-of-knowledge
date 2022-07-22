"""
Два правила магических методов:
1. Все магические методы срабатывают при выполнении соответствующей операции, или вызове функции
2. Все магические методы работают с уже встроенными типами данных.
   Даже в твоём классе они будут работать только built-in типами данных

sources:
    документация
    https://docs.python.org/3/reference/datamodel.html#object.__add__
    https://docs.python.org/3/reference/datamodel.html#object.__radd__
    https://docs.python.org/3/reference/datamodel.html#object.__iadd__


Магические методы, которые отвечают за базовае математические операции:
__add__ - сложение (our_instance + 5)
__radd__ - сложение (5 + our_instance)
__mul__ - умножение (__rmul__)
__sub__ - вычитание (__rsub__)
__truediv__ - деление (только /) (__rtruediv__)


Операторы математических действий:
1. Всегда принимают аргумент other (self, other)
2. имеют аналоги начинающиеся на:
    r (__radd__  -  5 + myinstance)
    i ( __iadd__  -  myinstance += 5)
"""


class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f'Client {self.name}; Balance - {self.balance}'

    def __add__(self, other):
        print('__add__ call')
        if isinstance(other, (int, float,)):
            return self.balance + other

        elif isinstance(other, BankAccount):
            # return self.balance + other.balance

            # если сделать объект изменяемым:
            # self.balance += other.balance
            # или создать новый объект
            return BankAccount(self.name, self.balance + other.balance) # новый объект

        else:
            raise NotImplemented  # нет смыла вызывать NotImplemented ведь он не заимствован от BaseException
            # print('Шо ха хуйня')

    def __radd__(self, other):
        print('__radd__ call')
        return self + other

    def __mul__(self, other):
        print('__mul__ call')
        if isinstance(other, (int, float,)):
            return self.balance * other

        elif isinstance(other, BankAccount):
            return self.balance * other.balance
        else:
            raise NotImplemented

    def __rmul__(self, other):
        print('__radd__ call')
        return self * other


"""
c = BankAccount('Aftem', -1488)
cc = BankAccount('user', 488)
"""



"""
3_4_2

from operator import add, mul


class Vector:

    def __init__(self, *args):
        self.values = [i for i in args if isinstance(i, int)]
        self.values.sort()

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(self.values)}'
        else:
            return 'Пустой вектор'

    def operation(self, action, other, output_word1, output_word2):
        if isinstance(other, int):
            values = [action(i, other) for i in self.values]
            return Vector(*values)
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                values = list(map(lambda x: action(x[0], x[-1]), zip(self.values, other.values)))
                return Vector(*values)
            else:
                print(f'{output_word1} векторов разной длины недопустимо')
        else:
            print(f'Вектор нельзя {output_word2} с {other}')

    def __add__(self, other):
        return self.operation(
            action=add,
            other=other,
            output_word1='Сложение',
            output_word2='сложить'
        )

    def __mul__(self, other):
        return self.operation(
            action=mul,
            other=other,
            output_word1='Умножение',
            output_word2='умножить'
        )
"""