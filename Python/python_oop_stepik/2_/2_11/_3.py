"""

У нас уже имеется с предыдущего урока класс Registration. Давайте добавим в него следующее:

в метод  __init__ добавляется еще один аргумент: пароль.
Как в примере с логином, вы должны будете сохранить переданный пароль через password
через сеттер  password (см пункт 3 в этом задании). Примерный код метода __init__
def __init__(self, логин, пароль):
    self.login = логин # передаем в сеттер login значение логин
    self.password = пароль # передаем в сеттер password значение пароль
Должны сработать свойства сеттер login из предыдущего задания  и сеттер password из пункта 3
для проверки валидности переданных значений

Свойство геттер password, которое возвращает значение self.__password;
Свойство сеттер password, принимает значение нового пароля.
Его необходимо перед сохранением проверить на следующее:
новое значение пароля должно быть строкой(не список, словарь и т.д. )

в противном случае вызываем исключение TypeError("Пароль должен быть строкой")
Длина нового пароля должна быть от 5 до 11 символов,
в противном случае вызывать исключение ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
Новый пароль должен содержать хотя бы одну цифру.
Для этого создаем staticmethod is_include_digit , который проходит по всем элементам строки и проверяет наличие цифр.
В случае отсутствия цифрового символа вызываем исключение: ValueError('Пароль должен содержать хотя бы одну цифру')
Строка password должна содержать элементы верхнего и нижнего регистра.
Создаем staticmethod is_include_all_register, который с помощью цикла проверяет элемента строчки на регистр.
В случае ошибки вызываем: ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
Строка password помимо цифр должна содержать только латинские символы.
Для этого создайте staticmethod is_include_only_latin ,
который проверяет каждый элемент нового значения на принадлежность к латинскому алфавиту
(проверка должна быть как в верхнем, так и нижнем регистре).
В случае, если встретится нелатинский символ, вызвать ошибку ValueError('Пароль должен содержать только латинский алфавит').
Подсказка: из модуля string можно импортировать переменную ascii_letters,
она хранит в себе все латинские символы в верхнем и нижнем регистре

Пароль не должен совпадать ни с одним из легких паролей, хранящихся в файле easy_passwords.txt.
Сохраните данный файл к себе в папку с вашей программой и не меняйте название.
С помощью staticmethod создаем метод check_password_dictionary и проверяем наличие нашего пароля в данном файле.
Если значение совпадет со значением из файла,
то в сеттер вызываем исключение: ValueError('Ваш пароль содержится в списке самых легких')
Пример работы класса Registration

r1 = Registration('qwerty@rambler.ru', 'QwrRt124') # здесь хороший логин
print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

# теперь пытаемся запись плохие пароли
r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
r1.password = 43  # raise TypeError("Пароль должен быть строкой")
"""

# TypeError("Пароль должен быть строкой")
# ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
# ValueError('Пароль должен содержать хотя бы одну цифру') is_include_digit
# ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра') is_include_all_register
# ValueError('Пароль должен содержать только латинский алфавит') is_include_only_latin

# easy_passwords.txt check_password_dictionary
# ValueError('Ваш пароль содержится в списке самых легких')
#
from string import (
    ascii_letters,
    ascii_uppercase,
    ascii_lowercase,
)


class Registration:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @staticmethod
    def is_include_digit(password):
        for elem in password:
            if elem.isdigit():
                return True
        raise ValueError('Пароль должен содержать хотя бы одну цифру')

    @staticmethod
    def is_include_all_register(password):
        # lower_counter = 0
        # upper_counter = 0
        # for elem in password:
        #     if elem.islower():
        #         lower_counter += 1
        #     elif elem.isupper():
        #         upper_counter += 1
        # if lower_counter and upper_counter:
        #     return True
        uppercase = set(ascii_uppercase)
        lowercase = set(ascii_lowercase)

        if uppercase.intersection(password) and lowercase.intersection(password):
            return True
        raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

    @staticmethod
    def is_include_only_latin(password):
        set_password = set(password)
        set_password.difference_update(ascii_letters)
        if set_password < password and set_password.isdigit():
            return True
        raise ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')

    @staticmethod
    def check_password_dictionary(password):
        with open(file='dependencies/easy_passwords.txt', mode='r') as file:
            easy_passwords = file.read().split('\n')
            if password not in easy_passwords:
                return True
        raise ValueError('Ваш пароль содержится в списке самых легких')

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

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if isinstance(value, str):
            if 4 < len(value) < 12:
                self.is_include_digit(value)
                self.is_include_all_register(value)
                self.is_include_all_register(value)
                self.check_password_dictionary(value)
                self.__password = value
            else:
                raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
        else:
            raise TypeError("Пароль должен быть строкой")


if __name__ == '__main__':
    r1 = Registration('qwerty@rambler.ru', 'QwrRt124')  # здесь хороший логин
    print(r1.login, r1.password)  # qwerty@rambler.ru QwrRt124

    # теперь пытаемся запись плохие пароли
    # r1.password = '123456'  # ValueError('Пароль должен содержать хотя бы один символ верхнего и нижнего регистра')
    # r1.password = 'LoW'  # raise ValueError('Пароль должен быть длиннее 4 и меньше 12 символов')
    # r1.password = 43  # raise TypeError("Пароль должен быть строкой")
