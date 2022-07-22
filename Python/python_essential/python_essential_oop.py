"""
-------------------------------------------------- 1 Введение в ООП --------------------------------------------------

sources:
    https://gos-it.fandom.com/wiki/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D0%BD%D1%8B%D0%B5_%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B_%D0%9E%D0%9E%D0%9F:_%D0%B8%D0%BD%D0%BA%D0%B0%D0%BF%D1%81%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F,_%D0%BD%D0%B0%D1%81%D0%BB%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5,_%D0%BF%D0%BE%D0%BB%D0%B8%D0%BC%D0%BE%D1%80%D1%84%D0%B8%D0%B7%D0%BC#.D0.90.D0.B1.D1.81.D1.82.D1.80.D0.B0.D0.BA.D1.86.D0.B8.D1.8F

ООП - парадигма программирования, в которой основные концепции - понятия КЛАССОВ и ОБЪЕКТОВ

Принципы ООП:

1. Абстракция
2. Инкапсуляция
3. Полиморфизм
4. Наследование

***** Абстракция
Абстра́кция в объектно-ориентированном программировании — это использование только тех
характеристик объекта, которые с достаточной точностью представляют его в данной системе.
Основная идея состоит в том, чтобы представить объект минимальным набором полей и методов
и при этом с достаточной точностью для решаемой задачи.


***** Инкапсуляция

Если максимально кратко, инкапсуляция - разделение деталей реализации и публичного интерфейса, в этом суть.

Инкапсуляция — свойство программирования, позволяющее пользователю не задумываться о сложности реализации
используемого программного компонента (что у него внутри?), а взаимодействовать с ним посредством предоставляемого интерфейса
(публичных методов и членов), а также объединить и защитить жизненно важные для компонента данные.
При этом пользователю предоставляется только спецификация (интерфейс) объекта.

Инкапсуляция (англ. encapsulation, от лат. in capsula) — в информатике размещение в одном компоненте данных и методов,
которые с ними работают. В реализации большинства языков программирования (C++, C#, Java и другие),
обеспечивает механизм сокрытия, позволяющий разграничивать доступ к различным частям компонента.


!!! Основной смысл инкапсуляуии, в том, чтобы пользователь работал с интерфейсом,
по протоколу, но не трогал внутреннюю реализацию !!!

Инкапсуляция обеспечивается следующими средствами:
- контроль доступа (атрибуты начинающиеся с _ и __)
- методы доступа (property(fget=Non
e, fset=None, fdel=None, doc=None))
- свойство объекта

-- контроль доступа

Атрибуты и методы в python бывают: публичные (public)
                                   _приватные (private)
                                   __защищённые (protected)


Все атрибуты и методы в python по умолчанию публичные

атрибуты начинающиеся с _ приватные атрибуты, но без механизма защиты
атрибуты начинающиеся с _ говорят разработчикам, что их менять (или даже использовать) не надо,
что это механизм внутренней реализации

атрибуты начинающиеся с __ и не заканчивающиеся __ считаются приватными-защищёнными
К ним применяется механизм 'name mangling' (коверкание имени)
добавляется к атрибуту _<ClassName>
они защищены, но всё равно в python можно менять приватные атрибуты даже защищённые
просто сделать это сложнее.
Важный момент, внутри класса, где они определены - доступ к этим атрибутам есть
Эта защита от случайного переопределения этих атрибутов,
например при наследовании

class BankAccount:
#
#     def __init__(self, name, balance, password):
#         self.__name = name
#         self.__balance = balance
#         self.__password = password
#
#     def print_info(self):
#         return self.__print_info()
#
#     def __print_info(self):
#         print(f'Name - {self.__name};\nBalance - {self.__balance};\nPassword - {self.__password}')
#
# if __name__ == '__main__':
#     ac = BankAccount(name='Пипетос', balance=100000000, password='fdsf3423@#$Dfs23d')
#     ac.print_info()
#     print('\n')
#     ac._BankAccount__print_info()


Ну и если нужно действительно защитить атрибуты,
то есть библиотека accessify https://pypi.org/project/accessify/



-- методы доступа

Методы доступа это про getattr, setattr, hasattr, delattr и property

sources:
    https://realpython.com/python-property/#:~:text=Python's%20property()%20is%20the,use%20it%20without%20importing%20anything.
    https://habr.com/ru/company/otus/blog/557804/
    https://www.programiz.com/python-programming/property

Как сделать так, чтобы когда записываешь какой-то атрибут - чтобы значение автоматически определялось на корректность?
Самый простой способ - описать методы для установки значения или получения значения этого атрибута (get и set)
Для этого и нужны методы доступа

** функция property

изначально property это функция




# class C:
#
#     def __init__(self):
#         self.__private_Attr = 99
#
#     @property
#     def attribute(self):
#         return self.__private_Attr
#
#     @attribute.setter
#     def attribute(self, value):
#         if value < 100:
#             self.__private_Attr = value
#         else:
#             print('Повремени мгновение, пока не схлопотал')
#             # raise ValueError
#
# if __name__ == '__main__':
#     c = C()
#     print(c.attribute) # 99
#     c.attribute = 30
#     print(c.attribute) # 30
#     c.attribute = 3054545
#     print(c.attribute) # Повремени мгновение, пока не схлопотал




-- свойство объекта

class C:
    __private_attr = 'some data'

print(C._C__private_attr)


# class C:
#
#     def __init__(self):
#         self.__private_Attr = 432432
#
#     def get_private_attr(self):
#         return self.__private_Attr

#     def set_private_attr(self):
#         return self.__private_Attr
#
# if __name__ == '__main__':
#     c = C()
#     print(c.get_private_attr())
#     print(C.get_private_attr(c))
#     print(c._C__private_Attr)
#     print(*dir(c), sep='\n', end='\n' * 3 + '*' * 5)
#     print(*dir(C), sep='\n')



***** Полиморфизм

Полиморфизм - это способность одинаковым образом обрабатывать данные разных типов.
Полиморфизм является фундаментальным свойством системы типов

Полиморфизм бывает:

- специальный полиморфизм
- параметрический полиморфизм
- полиморфизм подтипов (включений)

специальный полиморфизм - один интерфейс, множество реализаций. один метод на множество реализаций

параметрический полиморфизм - противоположность параметрического. одна реализация - множество интерфейсов

полиморфизм подтипов - это и есть то, что понимают под полиморфизмом в ООП.

Если у нас есть класс B который наследуется от класса A,
то в любой экземпляр класса B можно использовать там где ожидается экземпляр класса A
и он будет работать точно также (спорно, а если мы метод переопределили)
В это и есть суть полиморфизма в ООП

Динамическая типизация python (и не только), по праву может считаться одним из видов полиморфизма

Полиморфизм в языках с динамической типизацией - это что-то собой разумеещеся.
Он просто достигается за счёт динамической типизации

!!! В python нас не интересует тип данных объекта. Мы просто берём, и вызываем те методы, которые нас интересуют
Это и есть тот принцип с помощью которого реализуется полиморфизм и абстракция данных
в языках с динамической типизацией. Утиная типизация
DUCK TYPING. УТИНАЯ ТИПИЗАЦИЯ. УТЯ.

"if it looks like a duck, swims like a duck and quacks like a duck, the it probably is a duck"
("Если это выглядит как утка, плавает как утка и крякает как утка, то вероятно, это утка")

Неявная типизация, латентная типизация, утиная типизация - вид динамической типизации,
при которой границы использования объектав определяются его текущим набором методов и свойств,
в противоположность наследованию от определённого класса. Т.е. считается, что объект реализует ИНТЕРФЕЙС,
если он содержит все методы этого интерфейса, независимо от связей в иерархии наследования и принадлежности
к какому-либо конкретному классу.

Мы ведь нигде заранее тип данных не указываем, как если при статической типизации?
Интерпретатор сам определяет типы данных

Полиморфизм в языках с динамической типизацией означает, что объект нам подходит
не в том случае, если он является экземпляром какого-то класса,
а если у него есть нужные нам методы и атрибуты
Только набор методов определяют интерфейс объекта в языках с динамической типизацией


***** Наследование
Наследование — один из четырёх важнейших механизмов объектно-ориентированного программирования,
позволяющий описать новый класс на основе уже существующего (родительского), при этом свойства и
функциональность родительского класса заимствуются новым классом.

Наследование - механизм языка, позволяющий описать класс на основе уже существующего

Базовый класс, от котого наследуются все встроенные типы данных (классы) в python - object

Но есть ещё метакласс type.
Так как всё в python является объектами, то и сами классы являются объектами - экземплярами метаклассов
Гланым метаклассом является метакласс type
Мета-класс type - абстракция понятия типа данных

Метапрограммирование — вид программирования, связанный с созданием программ, которые порождают другие программы
как результат своей работы (в частности, на стадии компиляции их исходного кода) либо программ,
которые меняют себя во время выполнения (самомодифицирующийся код).

class Person:

    def print_info(self):
        print(self.name + ' is ' self.age)

john = Person()
Вызов john.print_info() вызывает Person.print_info(john)
так это работает



Интересный момент представлен ниже. В дочернем классе мы вызываем метод,
который будет показывать имя класса (__class__.__name__)
и имя экземпляра класса (type(self).__name__)
Так вот, если имя класса то выдаёт имя родительского класса,
даже не смотря на то, что вызывается в дочернем
А вот имя экземпляра класса показывает класс,
экземпляром которого является объект
Но это только в методе, от котого унаследован дочерний класс.
если мы в своём новом методе дочернего класса посмотрим какой __class__.__name__
то нам покажет актуальный класс

# class Base:
#     def method(self):
#         print('Method class {}'.format(__class__.__name__))
#         print('Instance class {}'.format(type(self).__name__))
#         print('\nMRO for parent:', *__class__.mro(), sep='\n')
#         print('\nMRO for instance:', *type(self).mro(), sep='\n')
#
# class Child(Base):
#     def else_method(self):
#         print('Method class {}'.format(__class__.__name__))
#         print('Instance class {}'.format(type(self).__name__))
#         print('\nMRO for parent:', *__class__.mro(), sep='\n')
#         print('\nMRO for instance:', *type(self).mro(), sep='\n')
#
#
# def main():
#     ins = Child()
#     ins.method()
#     print()
#     ins.else_method()
#
# if __name__ == '__main__':
#     main()


MRO - method resolution order (порядок разрешения методов)
это такой способ линеаризации (по определённому алгоритму - C3-линеаризация)


Наследование двжется с лева направо, в виде молнии:

# class A:
#     def method(self):
#         print(f'method {__class__.__name__} for {type(self).__name__}')
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def method(self):
#         print(f'method {__class__.__name__} for {type(self).__name__}')
#
#
# class D(B, C):
#     pass
#
#
# class E(B):
#     pass
#
#
# def main():
#     d = D()
#     e = E()
#     d.method()
#     e.method()
#     print()
#     print(*type(d).mro(), sep='\n', end='\n\n')
#     print(*type(e).mro(), sep='\n', end='\n\n')
#
#
# if __name__ == '__main__':
#     main()

# for cls in [A, B, C, D, E,]:
#     print(cls.__name__,' - ', cls.mro())



функция super():

# class A:
#     def method(self, a):
#         # print(f'method {__class__.__name__} for {type(self).__name__}')
#         return 5 + a
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def method(self, *args, **kwargs):
#         r = super().method(*args, **kwargs)
#         r **= 2
#         return f'result {r}'
#
#
# class D(B, C):
#     pass
#
#
# class E(B):
#     pass
#
#
# def main():
#     c = C()
#     print(c.method(a=5)) # 100
#
#
# if __name__ == '__main__':
#     main()
#

Вот ещё один пример использования функции super()
на примере заимствования конструктора.
Мы заимствуем старый конструктор, и добавляем что-то своё

# class C:
#     def __init__(self):
#         self.a = 5
#
#
# class CC(C):
#     def __init__(self):
#         super(CC, self).__init__()
#         self.b = 7
#
# c = CC()
#
# print(c.a, c.b, sep='\n') # 5 7


Ну и последний пример заимствования:

# class Animal:
#
#     def __init__(self):
#         self.can_fly = False
#         self.can_run = False
#         self.can_droch = 'XZ'
#
#     def print_abilities(self):
#         print(f'{type(self).__name__} can run? - {self.can_run}')
#         print(f'{type(self).__name__} can fly? - {self.can_fly}')
#         print('\n')
#
#
# class Horse(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_run = True
#         self.can_droch = 'horse'
#
# class Bird(Animal):
#     def __init__(self):
#         super().__init__()
#         self.can_fly = True
#         self.can_droch = 'bird'
#
# class Pegasus(Horse, Bird):
#     pass
#
#
# def main():
#     horse = Horse()
#     bird = Bird()
#     pegasus = Pegasus()
#     horse.print_abilities()
#     bird.print_abilities()
#     pegasus.print_abilities()
#     print(pegasus.can_droch)
#
#
# if __name__ == '__main__':
#     main()


isinstance и issubclass

# def check_instance(obj, cls):
#     if type(obj) == type and cls != type:
#         return False
#     return check_subclass(type(obj), cls)
#
#
#
# def check_subclass(child, base):
#     if child != base:
#         for cls in child.__bases__:
#             if cls == base:
#                 return True
#             return check_subclass(cls, base)
#         return False
#     return True
#
# class L(list):
#     pass
#
# class LL(L):
#     pass
# class C(ZeroDivisionError):
#     pass
#
# l = L()
# c = C()
#
# def main():
#     ls = [
#         isinstance(l, L),  #        1) True
#         isinstance(l, list) , #     2) True
#         isinstance(l, C),  #        3) False
#         isinstance(L, list),  #     4) False
#         isinstance(list, list),#    5) False
#         check_instance(l, L),  #    6) True
#         check_instance(l, list),  # 7) True
#         check_instance(l, C),  #    8) False
#         check_instance(L, list),  # 9) False
#         isinstance(list, list),  #  10) False
#         '-' * 30,
#         issubclass(L, C),  #        12) False
#         issubclass(C, L),  #        13) False
#         issubclass(L, list),  #     14) True
#         issubclass(C, object),  #   15) True
#         check_subclass(L, C),  #    16) False
#         check_subclass(C, L),  #    17) False
#         check_subclass(L, list),  # 18) True
#         check_subclass(C, object), #19) True
#         check_subclass(str, bool), #20) False
#         isinstance(str, type), #    21) True
#         check_instance(str, type), #22) True
#         isinstance(object, type), #    23) True
#         check_instance(object, type), #24) True
#     ]
#     for i, elem in enumerate(ls, start=1):
#         print(str(i) + ') ', elem)
#
# if __name__ == '__main__':
#     main()
#     print(L.__bases__)
#     print(LL.__bases__)



***** staticmethod

Пример использования staticmethod:

# class MyObject(object):
#
#     class_attr = 32
#
#     def __init__(self):
#         self.instance_attr = 78
#
#
#     def instance_method(self):
#         return self.instance_attr
#
#     def else_instance_method(self):
#         return MyObject.class_attr
#
#     @staticmethod
#     def static_method():
#         return MyObject.class_attr
#
# if __name__ == '__main__':
#     obj = MyObject()
#     print(MyObject.static_method())# 32
#     print(obj.instance_method())# 78
#     print(obj.static_method())# 32
#     print(obj.else_instance_method())# 32
#     print(obj.class_attr)# 32
#     print(MyObject.__dict__)
#     print(obj.__dict__)

Как видно из примера выше - можно доставать атрибуты класса напрямую,
и или из методов экземпляра (если реализована такая возможность)

Мне кажется staticmethod нужен для того, чтобы делать какие-то вычисления
с атрибутами класса. Чтобы при вызове статического метода уже был готовый результат.

Как видно из примера - статический метод никуда не привязан. Так как туда не передаётся аргумент self
Но вызывать его можно как из класса, так и из экземпляра класса

Вообще загугли, для чего на практике он нужен.

По предназначению статический метод похож на атрибут класса.
Если нужно будет определить атрибут класса, но только в виде функции,
то можно воспользоваться статическим методом.


***** classmethod

Как определить методы, которые привязаны к классам, а не их экземплярам?

В отличие от обычных методов классовые методы не работают с экземплярами класса,
не имеют доступа к их атрибутам и т.д.

Для классового метода используется декоратор @classmethod и первый аргумент классового метода вместо self - cls

class Rectangle(object):
#
#     def __init__(self, side_a, side_b):
#         self.side_a = side_a
#         self.side_b = side_b
#
#     def __repr__(self):
#         return 'Rectangle (%.1f, %.1f)' % (self.side_a, self.side_b)
#
#
# class Circle:
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __repr__(self):
#         return 'Circle (%.1f)' % (self.radius)
#
#     @staticmethod
#     def from_rectangle_first(rectangle):
#         radius = (rectangle.side_a ** 2 + rectangle.side_a ** 2) ** 0.5 / 2
#         return Circle(radius=radius)
#
#     @classmethod
#     def from_rectangle_second(cls, rectangle):
#         radius = (rectangle.side_a ** 2 + rectangle.side_a ** 2) ** 0.5 / 2
#         return cls(radius)
#
#
# if __name__ == '__main__':
#     rectangle = Rectangle(5, 5)
#     rectangle2 = Rectangle(20, 25)
#     circle = Circle(30)
#     print(rectangle)# Rectangle (5.0, 5.0)
#     print(rectangle2)# Rectangle (20.0, 25.0)
#     print(circle)# Circle (30.0)
#     print(circle.from_rectangle_first(rectangle))# Circle (3.5)
#     print(circle.from_rectangle_second(rectangle2))# Circle (14.1)
#     print(circle.from_rectangle_second(rectangle))# Circle (3.5)


В чём смысл классовых методов? для чего они нужны?
Допустим от класса Circle унаследуется другой класс

Если в это другом классе вызвать метод from_rectangle_first
то он будет возвращать объект класса Circle
а это не дело
а если вызвать классовый метод from_rectangle_second
то он верёт экземпляр того класса, от котого унаследовался.
По возможности злоупотреблять классовыми методами не стоит,
если есть возможность определить статический метод, то лучше его и определять


***** Специальные атрибуты и методы (волшебные)

Встроенные методы и атрибуты.
Задают свойства объектов
С помощью этих методов можно:
    - задать особое поведение объектов,
    - переопределить всетроенное поведение функций, таких как len, и операторов (> и т.д.)

Собственно говоря, весь функционал типа данных, мы определяем с помощью этих методов
и это накладывается на утиную типизацию.
Какой функционал, с помощью волшебных методов, мы определим для объекта,
таким тип данных этого объекта и будет.
Для этого в Python есть целый набор специальных (волшебных) методов.
Хочешь придать своему типу данных какие-то черты, функционал -
определяй в нём эти специальные методы.

Не рекомендуется объявлять свои собственные методы и атрибуты,
которые начинаются с __ и заканчиваются __
Атрибуты с такими подчёркиваниями Python обрабатывает особым образом,
и доступ к ним не всегда такой как к обычным
+ есть риск переопределить встроенный волшебный метод

Пример использования волшебных (специальных) методов

# class Complex:
#
#     def __init__(self, real=0.0, imaginary=0.0):
#         self.real = real
#         self.imaginary = imaginary
#
#     def __repr__(self):
#         return f'Complex({self.real}, {self.imaginary})'
#
#     def __str__(self):
#         return f'{self.real}{self.imaginary}i'
#
#     def __add__(self, other):
#         return Complex(self.real + other.real, self.imaginary + other.imaginary)
#
#     def __neg__(self):
#         return Complex(-self.real, -self.imaginary)
#
#     def __sub__(self, other):
#         return self + (-other)
#
#     # кстати, что такое abs функция - вот отличный пример что она делает
#     def __abs__(self):
#         return (self.real ** 2 + self.imaginary ** 2) ** 0.5
#
#     # __ne__ - метод неравно. достаточно определить что-то одно __eq__ или __ne__
#     def __eq__(self, other):
#         return self.real == other.real and self.imaginary == other.imaginary


Кстати, __init__ используется даже не во время создания экземпляра класса, а после
но всё равно для его полной инициализации

А для создания экземпляров класса используется метод __new__(cls) (да, он классовый, но @classmethod для него не требуется)

Создадим класс singleton, у которого может быть только один экземпляр (объект в памяти)

# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     def __init__(self):
#         self.value = 'some value'
#
#
# if __name__ == '__main__':
#     c = Singleton()
#     print(c, id(c), sep='\n')# <__main__.Singleton object at 0x000002BC6A85FFA0>
#                              # 3008264273824
#
#     cc = Singleton()
#     print(cc, id(cc), sep='\n')# <__main__.Singleton object at 0x000002BC6A85FFA0>
#                                # 3008264273824
#
#     print(type(c), Singleton.mro(), sep='\n')# <class '__main__.Singleton'>
                                               # [<class '__main__.Singleton'>, <class 'object'>]

"""
