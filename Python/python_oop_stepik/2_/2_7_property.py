"""

----- Самый элементарный способ использовать property
это создавать атрибуты только для чтения

class Person:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


if __name__ == '__main__':
    person = Person('Jack', 33)

    # Считываем значения
    print(person.name)  # Jack
    print(person.age)  # 33

    # Пытаемся записать новое значение
    person.age = 42  # AttributeError: can't set attribute

# усё


----- интересный пример использования property

class Square:

    def __init__(self, side):
        self.side = side

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = float(value)

    @property
    def area(self):
        return self.side ** 2

    @area.setter
    def area(self, value):
        self.side = value ** 0.5


if __name__ == '__main__':
    sq = Square(42)

    # Считываем значения
    print(sq.side)  # 42.0

    print(sq.area)  # 1764.0

    # записаем новое значение
    sq.area = 100

    print(sq.side)  # 10.0



----- пример создания атрибута только для записи
без возможности чтения

import os
import hashlib

class AccessError(Exception): pass

class User:

    def __init__(self, name, password):
        self.password = password
        self.name = name

    @property
    def password(self):
        raise AccessError('Not for reading')

    @password.setter
    def password(self, value):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac(
            "sha256", value.encode("utf-8"), salt, 100_000
        )


if __name__ == '__main__':
    jack = User("Jack", "secret_key")
    print(jack._hashed_password)
    # print(jack.password) # AccessError: Not for reading
    jack.password = "new_secret"
    print(jack._hashed_password)
"""
