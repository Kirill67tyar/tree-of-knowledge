"""

----- Вычисляемые атрибуты
"""


class Square:
    def __init__(self, side):
        self.side = side
        # self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if not self.__area:
            self.__area = self.side ** 2
        return self.__area

if __name__ == '__main__':
    s = Square(5)
    print(s.area)
    s.side = 16
    print(s.area)