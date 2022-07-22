"""
# задание было таким
import string


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
        check_one = len(set(value).intersection(set(string.ascii_lowercase))) >= 2
        check_two = len(set(value).intersection(set(string.ascii_uppercase))) >= 2
        if not all([check_one, check_two, ]):
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


Допустим, у нас есть сайт и для успешной регистрации на нем необходимо придумать логин и пароль.
Но мы хотим, чтобы при этом выполнялись определенные проверки с предоставленной пользователем информацией,
например, чтобы пароль был непростым. Мы можем делегировать данные проверки классу Registration ,
который вам необходимо создать.

Задача будет состоять из двух частей.

Часть 1
Создайте класс Registration, который пока будет проверять только введенный логин.
Под логином мы будем подразумевать почту пользователя, поэтому необходимо будет сделать некоторые проверки.

В классе Registration необходимо реализовать:

метод __init__ принимающий один аргумент логин пользователя.
Метод __init__ должен сохранить переданный логин через сеттер (см пункт 3).
То есть когда отработает данный код
def __init__(self, логин):
    self.login = логин # передаем в сеттер login значение логин
должно сработать свойство сеттер login из пункта 3 для проверки валидности переданного значения

Cвойство геттер login, которое возвращает значение self.__login;
Свойство сеттер login, принимает значение нового логина. Новое значение мы должны проверить на следующее:
логин, так как является почтой, должен содержать один символ собаки «@».
В случае, если в логине отсутствует символ «@»,
вызываем исключение при помощи строки raise ValueError("Логин должен содержать один символ '@'")
логин должен содержать символ точки «.» после символа «@».
В случае, если после @ нету точки, вызываем исключение
при помощи строки raise ValueError("Логин должен содержать символ '.'")
Если значение проходит проверку новое значение логина сохраняется в атрибут self.__login
Про исключения и команду raise мы с вами поговорим позже, просто вставляйте эту строчку как есть
if error:
    raise ValueError("Login must include at least one ' @ '")
Пример работы класса Registration

r1 = Registration('qwerty@rambler.ru') # здесь хороший логин
print(r1.login)  # qwerty@rambler.ru

# теперь пытаемся запись плохой логин
r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")

r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")
"""


class Registration:
    def __init__(self, login):
        self.login = login

    @property
    def login(self) -> str:
        return self.__login

    @login.setter
    def login(self, log):
        if isinstance(log, str):
            if log.count('@') == 1:
                if '.' in log.split('@')[-1]:
                    self.__login = log
                else:
                    raise ValueError("Логин должен содержать символ '.'")
            else:
                raise ValueError("Логин должен содержать один символ '@'")
        else:
            raise ValueError("Логин должен должен быть строкой")

if __name__ == '__main__':
    r1 = Registration('qwerty@rambler.ru')  # здесь хороший логин
    print(r1.login)  # qwerty@rambler.ru

    # теперь пытаемся запись плохой логин
    r1.login = '123456'  # ValueError("Логин должен содержать один символ '@'")
    #
    # r2 = Registration('qwerty.ru')  # ValueError("Логин должен содержать один символ '@'")
    # r3 = Registration('qwerty@ru')  # ValueError("Логин должен содержать символ '.'")