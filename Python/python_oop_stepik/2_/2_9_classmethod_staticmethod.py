"""

Base:
1) функция с @staticmethod можно одинаково вызывать от экземпляра и от класса
2) функция с @classmethod принимает обязательный аргумент cls
   и вызывается ТОЖЕ от класса и от экземпляра (полезно при наследовании)
   (просто с экземпдяром self ты не сможеь работать внутри этой функции)



class C:

    @classmethod
    def met(cls):
        return f' - - - {cls} - - - '

c = C()
c.met() # " - - - <class '__main__.C'> - - - "
C.met(C) # TypeError: met() takes 1 positional argument but 2 were given
C.met() # " - - - <class '__main__.C'> - - - "

"""


