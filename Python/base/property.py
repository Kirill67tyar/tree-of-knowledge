"""
[EXAMPLE, TASK]

Функция property - механизм инкапсуляции, конкретно методов доступа
Позволяет предоставить различные методы доступа к данным.

Управление атрибутами в ваших классах
Когда вы определяете класс на объектно-ориентированном языке программирования,
вы, вероятно, в конечном итоге получите некоторые атрибуты экземпляра и класса.
Другими словами, вы получите переменные, доступные через экземпляр, класс или даже и то, и другое,
в зависимости от языка. Атрибуты представляют или содержат внутреннее состояние данного объекта,
к которому вам часто потребуется обращаться и изменять его.

Как правило, у вас есть как минимум два способа управления атрибутом.
Либо вы можете получить доступ и изменить атрибут напрямую, либо вы можете использовать методы.
Методы — это функции, прикрепленные к данному классу. Они обеспечивают поведение и действия,
которые объект может выполнять со своими внутренними данными и атрибутами.

Если вы предоставляете свои атрибуты пользователям вашей программы, они становятся частью общедоступного API
( Application Programming Interface — «программный интерфейс приложения») ваших классов.
Пользователь вашего класса будет получать к ним доступ и изменять их непосредственно в своем коде.
И тут могут возникнуть ситуации, что пользователь попытается сохранить недопустимое
значение в атрибуты экземпляров вашего класса. Через сеттер(setter) вы можете повлиять на значение,
которое сохраняется в ваш атрибут. А геттер(getter) поможет управлять доступом к вашему атрибуту.
А для создания геттеров и сеттеров в Python вам может пригодиться property

property - эта функция позволяет вам превращать атрибуты класса в свойства или управляемые атрибуты.
Поскольку property() — это встроенная функция, вы можете использовать ее, ничего не импортируя.

Примечание. Обычно property называют встроенной функцией. Однако property — это класс,
предназначенный для работы как функция, а не как обычный класс.
Вот почему большинство разработчиков Python называют это функцией.
Это также причина, по которой property() не следует соглашению Python по именованию классов.

Зачем вообще нужен property? Чтобы как-то валидировать и приобразовывать те данные,
которые мы передаём в атрибуты экземпляра класса. Преобразовывать пароль в хешированные данные,
при смене пароля, и не давать его показывать.
Инфа поступает. Мы что-то с ней делаем. Возможно валидируем.
И сохраняем, или не сохраняем если валидация не прошла

С помощью property вы можете прикрепить методы получения(getter) и установки(setter) к заданным атрибутам класса.
Таким образом, вы можете обрабатывать внутреннюю реализацию этого атрибута,
не раскрывая методы получения и установки в вашем API.
Вы также можете указать способ обработки удаления атрибута и предоставить соответствующую строку документации для ваших свойств.

property(fget=None, fset=None, fdel=None, doc=None)
Параметры:

fget=None - функция для получения значения атрибута
fset=None - функция для установки значения атрибута
fdel=None - функция для удаления значения атрибута
doc=None - строка, для строки документации атрибута
Возвращаемое значение property — это сам управляемый атрибут. Если вы обращаетесь к управляемому атрибуту, как в obj.attr,
 тогда Python автоматически вызывает fget().
 Если вы присваиваете атрибуту новое значение, как в obj.attr = value, тогда Python вызывает fset(),
 используя входное значение в качестве аргумента. Наконец, если вы запустите оператор del obj.attr,
 то Python автоматически вызовет fdel().

Примечание. Первые три аргумента функции property должны принимают функциональные объекты.
Вы можете думать об объекте функции как об имени функции без вызывающей пары круглых скобок
Четвертым аргументом вы можете передать строку документации doc для вашего свойства.

class Person:
    def __init__(self, name):
        self._name = name

    def _get_name(self):
        print("Get name")
        return self._name

    def _set_name(self, value):
        print("Set name")
        self._name = value

    def _del_name(self):
        print("Delete name")
        del self._name

    name = property(
        fget=_get_name,
        fset=_set_name,
        fdel=_del_name,
        doc="The name property."
    )
В этом фрагменте создаете класс Person. Инициализатор класса .__init__() принимает имя в качестве аргумента и сохраняет его в защищенном атрибуте с именем ._name. Затем вы определяете три непубличных метода:

_get_name() возвращает текущее значение._name
_set_name() принимает value и присваивает его в атрибут экземпляра ._name
_del_name() удаляет у экземпляра атрибут ._name
>>> person = Person('Jack')

>>> person.name
Get name
Jack

>>> person.name= 'Jamal'
Set name
>>> person.name
Get name
Jamal

>>> del person.name
Delete name
>>> person.name
Get name
Traceback (most recent call last):
    ...
AttributeError: 'Person' object has no attribute '_name'

>>> help(person)
Help on Person in module __main__ object:

class Person(builtins.object)
    ...
 |  name
 |      The name property.
"""


# без property показать и установить баланс выглядело бы так
class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float,)):
            raise ValueError('Баланс должен быть числом')
        else:
            self.__balance = value


# tanya = BankAccount(name='tanya', balance=4242)
# print(tanya.get_balance())
# tanya.set_balance(121)
# print(tanya.get_balance())
# tanya.set_balance('121')
# print(tanya.get_balance())

# с property это выглядит так
class BankAccount:

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    # def get_balance(self):
    #     print('raice get_balance')
    #     return self.__balance
    #
    # def set_balance(self, value):
    #     print('raice set_balance')
    #     if not isinstance(value, (int, float,)):
    #         raise ValueError('Баланс должен быть числом')
    #     else:
    #         self.__balance = value
    #
    # def del_balance(self):
    #     print('raice del_balance')
    #     del self.__balance
    #
    # # так:
    # balance = property(fget=get_balance, fset=set_balance, fdel=del_balance)
    #
    # # или так
    # else_balance = property()
    # else_balance = else_balance.getter(get_balance)
    # else_balance = else_balance.setter(set_balance)
    # else_balance = else_balance.deleter(del_balance)
    #
    # # или так
    # and_else_balance = property(get_balance)
    # and_else_balance = else_balance.setter(set_balance)
    # and_else_balance = else_balance.deleter(del_balance)

    # или так
    # (очень важно, эти методы нужно называть одинаково)
    @property
    def balance(self):
        print('raice get_balance')
        return self.__balance

    @balance.setter
    def balance(self, value):
        print('raice set_balance')
        if not isinstance(value, (int, float,)):
            raise ValueError('Баланс должен быть числом')
        else:
            self.__balance = value

    @balance.deleter
    def balance(self):
        print('raice del_balance')
        del self.__balance


tanya = BankAccount(name='tanya', balance=4242)
# print(tanya.balance)
# tanya.balance = 234
# print(tanya.balance)
# del tanya.balance
# # print(tanya.balance) # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
# tanya.balance = 546
# print(tanya.balance)
# # tanya.balance = '234'# ValueError: Баланс должен быть числом
# # print(tanya.balance)
#
# print(tanya.and_else_balance)
# tanya.and_else_balance = 234
# print(tanya.and_else_balance)
# del tanya.and_else_balance
# # print(tanya.else_balance) # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
# tanya.and_else_balance = 546
# print(tanya.and_else_balance)
# # tanya.else_balance = '234'# ValueError: Баланс должен быть числом
# # print(tanya.else_balance)
# # print(tanya.and_else_balance)


# tanya.balance = 234
# print(tanya.balance)
# del tanya.balance
# # print(tanya.else_balance) # AttributeError: 'BankAccount' object has no attribute '_BankAccount__balance'
# tanya.balance = 546
# print(hasattr(tanya, 'balance')) # True
# print(tanya.balance)
# del tanya.balance
# print(hasattr(tanya, 'balance')) # False
# # tanya.else_balance = '234'# ValueError: Баланс должен быть числом
# # print(tanya.else_balance)


# obj = property()
# # print(obj)
# # У объекта Property <property object at 0x000001720F1354A0>
# # появляются методы setter(), getter(), deleter()
# # Эти геттеры и сеттеры можно заранее определить, как мы это сделали в классе выше
# # передав аргументы fget, fset и т.д.
# print(obj, id(obj))
# print(obj.setter(654), id(obj.setter(654)))
# # обрати внимание, что это разные объекты. просто property и property.setter
# # obj.getter()
# # obj.deleter()


"""
--- EXAMPLE ---
Предоставление атрибутов только для чтения
Пожалуй самый элементарный вариант использования property — предоставить атрибуты 
только для чтения в ваших классах. Допустим, вам нужен неизменяемый класс Point, 
который не позволяет пользователю изменять исходное значение его координат x и y. 
Для достижения этой цели вы можете создать Person , как в следующем примере:

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
Здесь вы сохраняете входные аргументы в атрибутах ._name и ._age. 
Используем подчеркивания (_) в именах для того, чтобы сообщить другим разработчикам, 
что они являются закрытыми атрибутами и к ним нельзя обращаться с помощью записи через точку, 
например, в person._age. Далее, определяем два метода получения через декоратор @property . 
Теперь у вас есть два свойства только для чтения

>>> person = Person('Jack', 33)

>>> # Считываем значения
>>> person.name
Jack
>>> person.age
33

>>> # Пытаемся записать новое значение
>>> person.age = 42
Traceback (most recent call last):
    ...
AttributeError: can't set attribute
"""

"""
--- TASK ---

Создайте класс UserMail, у которого есть:

конструктор __init__, принимающий 2 аргумента: логин и почтовый адрес. 
Их необходимо сохранить в экземпляр как атрибуты 
login и __email (обратите внимание, защищенный атрибут)
метод геттер get_email, которое возвращает защищенный атрибут __email ;
метод сеттер set_email, которое принимает в виде строки новую почту. 
Метод должен проверять, что в новой почте есть только один символ @ и после нее есть точка. 
Если данные условия выполняются, новая почта сохраняется в атрибут __email, 
в противном случае выведите сообщение "ErrorMail:<почта>";
создайте свойство email, у которого геттером будет метод get_email, а сеттером - метод set_email
k = UserMail('belosnezhka', 'prince@wait.you')
print(k.email)  # prince@wait.you
k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
k.email = 'prince@still.wait'
print(k.email)  # prince@still.wait
"""


class ErrorMail(Exception):
    pass


class UserMail:
    def __init__(self, login, email):
        self.login = login
        self.__email = email

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if isinstance(email, str):
            if email.count('@') == 1:
                domain = email.split('@')
                if '.' in domain[-1]:
                    self.__email = email
                else:
                    raise ErrorMail(f"ErrorMail:{email}")
                    # print(f"ErrorMail:{email}")
            else:
                raise ErrorMail(f"ErrorMail:{email}")
                # print(f"ErrorMail:{email}")
        else:
            raise ErrorMail(f"ErrorMail:{email}")
            # print(f"ErrorMail:{email}")

    email = property(fget=get_email, fset=set_email)


# k = UserMail('belosnezhka', 'prince@wait.you')
# print(k.email)  # prince@wait.you
# k.email = [1, 2, 3] # ErrorMail:[1, 2, 3]
# k.email = 'prince@still@.wait'  # ErrorMail:prince@still@.wait
# k.email = 'prince@still.wait'
# print(k.email)  # prince@still.wait

"""
--- TASK ---

 Создайте класс Student, у которого есть:

конструктор __init__, принимающий 3 аргумента и создает приватные атрибуты __name, __age, __branch;
приватный метод __display_details , который выводит на экран информацию о студенте в следующем виде
Имя: <name>
Возраст: <age>
Направление: <branch>
метод access_private_method, который вызывает приватный метод __display_details
Пример использования кода

obj = Student("Adam Smith", 25, "Information Technology")
obj.access_private_method()

#Output
Имя: Adam Smith
Возраст: 25
Направление: Information Technology
"""


class Student:

    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')

    def access_private_method(self):
        return self.__display_details()


# obj = Student("Adam Smith", 25, "Information Technology")
# obj.access_private_method()

# Output
# Имя: Adam Smith
# Возраст: 25
# Направление: Information Technology

"""

--- TASK ---

  Создайте класс Notebook, у которого есть:

конструктор __init__, принимающий 1 аргумента: список записей, в принципе там могут быть любые значения. 
Необходимо сохранить его в защищенном атрибуте ._notes
свойство notes_list, которое распечатает содержимое атрибута ._notes в виде упорядоченного списка (см. пример ниже)
note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
После этого на экране вы должны увидеть

1.Buy Potato
2.Buy Carrot
3.Wash car
"""


class Notebook:

    def __init__(self, notes):
        self._notes = notes

    @property
    def notes_list(self):
        output = ''.join([str(i) + '.' + str(el) + '\n' for i, el in enumerate(self._notes, start=1)])
        print(output[:-1])


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
# note.notes_list
# repr(note.notes_list)


"""

--- EXAMPLE ---


# Обалдеть. Обрати внимание, что в инициализаторе мы используем
# атрибут экземпляра как self.side а не self._side
# Это потому что при инициализации экземпляра класса, мы используем уже объект property
# обрати внимание на print(Square.side)

class Square:

    def __init__(self, side):
        self.side = side
        print(Square.side)# <property object at 0x0000023EBB835900>

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        self._side = float(value)


    @property
    def area(self):
        return self._side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5

sq = Square(42)

# Считываем значения
print(sq.side)

print(sq.area)

# записаем новое значение
sq.area = 100

print(sq.side)
"""

"""---------------------------------------

--- EXAMPLE ---

Отличный пример, зачем нужна инкапсуляция.
Делаем возможным атрибут только записывать:

import os
import hashlib
class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def password(self):
        raise AttributeError("Пароль можно только менять, нельзя смотреть")

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", plaintext.encode("utf-8"), salt, 100_000
        )

jack = User("Jack", "secret_key")

print(jack._hashed_password)

jack.password = 'new_secret'

print(jack._hashed_password)

---------------------------------------"""

"""

--- TASK ---

Создайте класс Money, у которого есть:

конструктор __init__, принимающий 2 аргумента: dollars, cents. 
По входным аргументам вам необходимо создать атрибут экземпляра total_cents. 
свойство геттер dollars, которое возвращает количество имеющихся долларов;
свойство сеттер dollars, которое принимает целое неотрицательное число - 
количество долларов и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, 
при этом значение центов должно сохранятся. В случае, если в сеттер передано число, 
не удовлетворяющее условию, нужно печатать на экран сообщение "Error dollars";
свойство геттер cents, которое возвращает количество имеющихся центов;
свойство сеттер cents, которое принимает целое неотрицательное число меньшее 100 - количество центов 
и устанавливает при помощи него новое значение в атрибут экземпляра total_cents, 
при этом значение долларов должно сохранятся. В случае, если в сеттер передано число, 
не удовлетворяющее условию, нужно печатать на экран сообщение "Error cents";
метод __str__ (информация по данному методу), который возвращает строку вида 
"Ваше состояние составляет {dollars} долларов {cents} центов". 
Для нахождения долларов и центов в методе __str__ пользуйтесь свойствами
В экземпляр класса кроме атрибута total_cents сохранять ничего не нужно!

Bill = Money(101, 99)
print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  # 101 99
print(Bill.total_cents) # 10199
Bill.dollars = 666
print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
Bill.cents = 12
print(Bill)  # Ваше состояние составляет 666 долларов 12 центов
"""


class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents
        # self.dollars = dollars
        # self.cents = cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:
            self.total_cents = value * 100 + self.cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = self.dollars * 100 + value
        else:
            print("Error cents")

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


# Bill = Money(101, 99)
# print(Bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(Bill.dollars, Bill.cents)  # 101 99
# print(Bill.total_cents) # 10199
# Bill.dollars = 666
# print(Bill)  # Ваше состояние составляет 666 долларов 99 центов
# Bill.cents = 12
# print(Bill)  # Ваше состояние составляет 666 долларов 12 центов


class Square:

    # def __init__(self, side):
    #     self.side = side
    #     self.temporary_value = side
    #     self._area = self.side ** 2
    #
    #
    # @property
    # def area(self):
    #     if self.temporary_value == self.side:
    #         print('not calculating')
    #         return self._area
    #     print('calculating')
    #     self.temporary_value = self.side
    #     self._area = self.side ** 2
    #     return self._area

    #     или так

    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        print('some validation')
        self.__side = float(value)
        self.__area = None

    @property
    def area(self):
        if not self.__area:
            self.__area = self.side ** 2
            print('calculating')
            return self.__area
        print('not calculating')
        return self.__area


# s = Square(3)
# print(s.area)
# s.side = 10
# print(s.area)
# print(s.area)


"""

--- TASK ---

Создайте класс Rectangle, у которого есть:

конструктор __init__, принимающий 2 аргумента: длину и ширину. 
свойство area, которое возвращает площадь прямоугольника;
r1 = Rectangle(3, 5)
r2 = Rectangle(6, 1)

print(r1.area) # 15
print(r2.area) # 6


# class Rectangle:
# 
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#     @property
#     def area(self):
#         return self.length * self.width
# 
# r1 = Rectangle(3, 5)
# r2 = Rectangle(6, 1)
# 
# print(r1.area)  # 15
# print(r2.area)  # 6

"""

# ---------------------------------------------------------------------------
"""

--- TASK ---

  Создайте класс Date, у которого есть:

конструктор __init__, принимающий 3 аргумента: день, месяц и год. 
свойство date , которое возвращает строку определенного формата "<день>/<месяц>/<год>";
свойство usa_date, которое возвращает строку определенного формата "<месяц>-<день>-<год>";
d1 = Date(5, 10, 2001)
d2 = Date(15, 3, 999)

print(d1.date) # 05/10/2001
print(d1.usa_date) # 10-05-2001
print(d2.date) # 15/03/0999
print(d2.usa_date) # 03-15-0999
Обратите внимание, что дни и месяцы занимают 2 символа в выводе, 
а отображение года- 4 символа(заполняются нулями спереди до нужной длины). 


# class Date:
# 
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
# 
#     # def mapping_date(self, day, month, year):
#     #     if day < 10:
#     #         day = '0' + str(day)
#     #
#     #     if month < 10:
#     #         month = '0' + str(month)
#     #     return day, month, (4 - len(str(year))) * '0' + str(year)
# 
#     @property
#     def date(self):
#         # day, month, year = self.mapping_date(self.day, self.month, self.year)
#         # return f"{day}/{month}/{year}"
#         return f"{self.day:02}/{self.month:02}/{self.year:04}"
# 
#     @property
#     def usa_date(self):
#         # month, day, year = self.mapping_date(self.month, self.day, self.year)
#         # return f"{month}-{day}-{year}"
#         return f"{self.month:02}-{self.day:02}-{self.year:04}"
# 
# d1 = Date(5, 10, 2001)
# d2 = Date(15, 3, 999)
# 
# print(d1.date) # 05/10/2001
# print(d1.usa_date) # 10-05-2001
# print(d2.date) # 15/03/0999
# print(d2.usa_date) # 03-15-0999
"""
# ---------------------------------------------------------------------------
"""

--- EXAMPLE ---


# from string import (
#     ascii_lowercase,
#     ascii_uppercase,
#     digits,
# )
# 
# 
# class ValidationError(BaseException):
#     pass
# 
# 
# class User:
# 
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.__secret = 'abracadabra'
# 
#     @property
#     def get_secret(self):
#         value = input('Enter your password: ')
#         if self.password == value:
#             return self.__secret
#         raise ValidationError('the password is wrong')
#         # return 'the password is wrong'
# 
#     @staticmethod
#     def numbs_validate(value):
#         try:
#             assert len(set(value).intersection(set(digits))) >= 2
#         except AssertionError:
#             raise ValidationError('password must contain two numbers')
#         # return len(set(value).intersection(set(digits))) >= 2
# 
#     @staticmethod
#     def letters_validate(value):
#         try:
#             value = set(value)
#             check_one = len(value.intersection(set(ascii_lowercase)))
#             check_two = len(value.intersection(set(ascii_uppercase)))
#             assert (check_one and check_two) >= 2
#         except AssertionError:
#             raise ValidationError('password must contain two capital letters and two lower letters')
# 
#         # value = set(value)
#         # check_one = len(value.intersection(set(ascii_lowercase)))
#         # check_two = len(value.intersection(set(ascii_uppercase)))
#         # return (check_one and check_two) >= 2
# 
#     @staticmethod
#     def not_simple_password_validate(value):
#         try:
#             with open('passwords_for_exercise.txt', 'r') as f:
#                 simple_passwords = f.read().split('\n')
#                 assert value.lower() not in simple_passwords
#         except AssertionError:
#             raise ValidationError('password must not be so simple')
# 
#         # with open('passwords_for_exercise.txt', 'r') as f:
#         #     simple_passwords = f.read().split('\n')
#         #     return value not in simple_passwords
# 
#     @property
#     def password(self):
#         return self.__password
# 
#     @password.setter
#     def password(self, value):
#         if isinstance(value, str):
#             try:
#                 User.not_simple_password_validate(value)
#                 User.letters_validate(value)
#                 User.numbs_validate(value)
#                 self.__password = value
#             except ValidationError as err:
#                 raise err
#         else:
#             raise ValidationError('password should be string')
#             # print('password should be string')
# 
#         # if isinstance(value, str):
#         #     ls = [
#         #         User.letters_validate(value),
#         #         User.numbs_validate(value),
#         #         User.not_simple_password_validate(value)
#         #     ]
#         #     if all(ls):
#         #         self.__password = value
#         #     else:
#         #         raise ValidationError('password invalid')
#         #         # print('password invalid')
#         # else:
#         #     raise ValidationError('password should be string')
#         #     # print('password should be string')
# 
# 
# def main():
#     tom = User('Tom', password='23423asaASD')
#     jerry = User('Jerry', password='412fdsDDDDDDDDDDQ')
#     # donald_duck = User('donald_duck', password='412fdsD') # password invalid
#     scrooge_mcduck = User('Scrooge_Mcduck', password='412fASA')
#     # russi_taylor = User('Russi_Taylor', password=2342) # password should be string
#     chuck_mcCann = User('Chuck_McCann', password='@@#FDWFgfdg43')
#     print(tom.username)
#     print(jerry.password)
#     # chuck_mcCann.password = 'qwerty'
#     print(tom.get_secret)
# 
# if __name__ == '__main__':
#     main()
"""

"""

--- TASK ---

Давайте создадим класс Registration, который поможет зарегистрировать пользователя с безопасным паролем

В классе Registration необходимо реализовать

Конструктор __init__ принимающий 2 аргумента (login, password). В конструкторе вы сохраняете переданные login 
и password через сеттеры (см пункт 3 и пункт 5). То есть когда отработает данный код 
def __init__(self, логин, пароль):
    self.login = логин # передаем в сеттер login значение логин 
    self.password = пароль # передаем в сеттер password значение пароль 
должны сработать свойства сеттер login из пункта 3 и сеттер password из пункта 5 для проверки валидности переданных значений

Cвойство геттер login, которое возвращает значение self.__login;
Свойство сеттер login, принимает значение емайла в случае если:
Емайл(login) содержит хотя бы 1 символ "@". 
В случае ошибки выводим ValueError("Login must include at least one ' @ '")
Email(login) содержит хотя бы 1 символ " . ".
В случае ошибки выводим ValueError("Login must include at least one ' . '")
Если значение проходит проверку новое значение логина сохраняется в атрибут (self.__login)
Свойство геттер password, которое возвращает значение self.__password;
Свойство сеттер password, принимает значение пароля в случае если:
Password является строкой(не список, словарь и т.д. ) в противном случае вызываем исключение 
TypeError("Пароль должен быть строкой")
Длина password должна быть от 5 до 11 символов, в противном случае вызывать исключение 
ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
Должен содержать хотя бы одну цифру. 
Для этого нужно в staticmethod создать функцию is_include_digit которая, 
которая проходит по всем элементам строки и проверяет их наличие в digits. 
В случае ошибки выводим: ValueError('Пароль должен содержать хотя бы одну цифру')
Строка password должна содержать элементы верхнего и нижнего регистра. 
В staticmethod создаем метод (is_include_all_register), 
который с помощью цикла проверяет элемента строчки на регистр. 
В случае ошибки выводит: ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')
Строка password должна содержать только латинские символы. 
Импортируем библиотеку string ,в staticmethod создаем метод(is_include_only_latin), 
которым проверяем, каждый элемент на наличие в string(проверка должна быть как в верхнем, 
так и нижнем регистре). В случае ошибки ValueError('Пароль должен содержать только латинский алфавит')
Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt. 
Сохраните данный файл к себе в папку с вашей программой и не меняйте название. 
С помощью staticmethod создаем метод check_password_dictionary 
и проверяем наличие нашего пароля в данном файле. 
Если значение совпадет со значением из файла, 
то в сеттер добавляем исключение и выводим ошибку: ValueError('Ваш пароль содержится в списке самых легких')
"""

import string
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits,
)
# 'side': <property object at 0x0000019105B99810>

# ascii_letters
# digits
#     ascii_lowercase,
#     ascii_uppercase,
class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(value):
        if not set(value).intersection(set(string.digits)):
            raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(value):
        first_check = len(set(value).intersection(string.ascii_lowercase)) >= 2
        second_check = len(set(value).intersection(string.ascii_uppercase)) >= 2
        if not all([first_check, second_check, ]):
            raise ValueError('Пароль должен содержать хотя бы 2 заглавные буквы')

    @staticmethod
    def is_include_only_latin(value):
        ascii_letters = string.ascii_letters
        if len(list(filter(lambda x: x.isdigit() or x in ascii_letters, value))) != len(value):
            raise ValueError('Пароль должен содержать только латинский алфавит')

    @staticmethod
    def check_password_dictionary(value):
        with open('easy_passwords.txt', 'r') as f:
            data = f.read().split('\n')
            if value in data:
                raise ValueError('Ваш пароль содержится в списке самых легких')

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, value):
        if value.count('@') < 1:
            raise ValueError("Login must include at least one ' @ '")
        elif value.count('.') < 1:
            raise ValueError("Login must include at least one ' . '")
        self.__login = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            if 4 < len(value) < 12:
                try:
                    Registration.is_include_digit(value)
                    Registration.is_include_all_register(value)
                    Registration.is_include_only_latin(value)
                    Registration.check_password_dictionary(value)
                    self.__password = value
                except ValueError as err:
                    raise err
            else:
                raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        else:
            raise TypeError("Пароль должен быть строкой")
