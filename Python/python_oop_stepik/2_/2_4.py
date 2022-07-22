"""



Моносостояние для экземпляров класса



2.4-----------------------------------------------------------------------------------------------------------------2.4


Похоже на синглтон, но не совсем.
Изменение, или добавление атрибута в одном экземпляре изменяет этот атрибут,
или добавляет этот атрибут во все экземпляры.

__dict__ экземпляра класса будет отдельным от класса пространством имён
    1. изменение или добавления аттрибута экземпляра затрагивает все остальные экземпдяры
    2. изменение атрибута класса ниакак не затрагивает экземпляры класса
"""
from pprint import pprint as pp


# пример:
class Cat:
    __shared_attributes = {
        'breed': 'pers',
        'color': 'black',
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attributes


if __name__ == '__main__':
    c = Cat()
    c2 = Cat()
    c3 = Cat()
    pp(c.__dict__)  # {'breed': 'pers', 'color': 'black'}
    pp(Cat.__dict__)  # {'__module__': '__main__', '_Cat__shared_attributes': {'breed': 'pers', 'color': 'black'}, '__init__': <fun
    c3.breed = 'main coon'
    pp(c.__dict__)  # {'breed': 'main coon', 'color': 'black'}
    pp(Cat.__dict__)  # {'__module__': '__main__', '_Cat__shared_attributes': {'breed': 'main coon', 'color': 'black'}, '__init__': <fun
    c2.age = 5
    pp(c3.__dict__)  # {'breed': 'main coon', 'color': 'black', 'age': 5}
    pp(Cat.__dict__)  # {'__module__': '__main__', '_Cat__shared_attributes': {'breed': 'main coon', 'color': 'black', 'age': 5}, '__init__': <fun

    # # НО
    # pp(Cat.age)  # AttributeError: type object 'Cat' has no attribute 'age'
    # pp(Cat.breed)  # AttributeError: type object 'Cat' has no attribute 'breed'

    # но при изменении аттрибута класса, при таком паттерне
    # аттрибуты экземпляра меняться или добавляться не будут
    Cat.new_attr = 'foo bar'
    pp(c3.__dict__)  # {'age': 5, 'breed': 'main coon', 'color': 'black'}
    pp(Cat.__dict__)
