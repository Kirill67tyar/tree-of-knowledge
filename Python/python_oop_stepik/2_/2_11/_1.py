class MyFileError(Exception):
    pass


class User:

    def __init__(self, username, password, secret):
        self.username = username
        self.password = password
        self.__secret = secret

    @property
    def get_secret(self):
        s = input()
        if s == self.password:
            return self.__secret
        raise ValueError('Forbidden')

    @staticmethod
    def digit_validator(password):
        for elem in password:
            if elem.isdigit():
                return True
        return False

    @staticmethod
    def common_password_validator(password):
        try:
            with open(file='dependencies/common-passwords.txt', mode='r') as f:
                passwords = f.read().split('\n')
                passwords = set(filter(bool, passwords))
                return password not in passwords
        except FileNotFoundError:
            raise MyFileError('Файла нет, повремени мгновение')

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not isinstance(value, str):
            raise TypeError('password must be string')
        if len(value) <= 4:
            raise TypeError('password is too short')
        if len(value) >= 12:
            raise TypeError('password is too big')
        if not self.common_password_validator(password=value):
            raise TypeError('password is easy')
        if not User.digit_validator(password=value):
            raise TypeError('password must contain minimum one number')

        self.__password = value


if __name__ == '__main__':
    u = User('qwe', 'qwertyqwe2', 'some secret')
    print(u.get_secret)
    u.password = '321eqew'
    print(u.get_secret)