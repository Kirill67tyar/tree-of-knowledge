"""
---------------------------------------------- Итераторы и генераторы ----------------------------------------------
sources:
    https://habr.com/ru/post/320288/


----------------------------------------------------------------------------
sources:
    https://habr.com/ru/post/320288/
                                    Итераторы и генераторы

-- Итераторы:
1. В python есть итерабельные типы данных и неитерабельные
2. у итерабельных типов данных определены методы __iter__() и/или __getitem__()
3. итератор - это новый объект, который управляет получением значений (переборкой) из итерабельного объекта
4. характеристики итератора:
    - одноразовый
    - отдельный объект в памяти
    - вызывается функцией iter() которая вызывает метод __iter__() у итерабельного объекта
    - если не находит метод __iter__() то ищет метод __getitem__() (метод для ключей или индексов)
      но работать __getitem__ будет только если объект работает с индексом а не ключом
    - у итератора тоже должен быть метод __iter__(self) который возвращает self. Это нужно для цикла for.
      любой итератор тоже является итерабельным объектом, и может быть использован везде
      где принимаются итерабельные объекты. 
    - у итератора есть метод __next__(), который и предоставляет элемент итератора
    - основные события происходят именно в __next__. в __next__ нужно показать следующий элемент
      каким-либо способом. И если они заканчиваются то вызвать StopIteration
5. функции reversed(), sorted(), map(), filter(), zip(), enumerate() - являются итераторами


-- Генераторы
1. генератор - вид функции в python. При вызове возвращает специальный итерабельный объект
   который управляет выполнением данной функции, позволяет её ставить на паузу или продолжать
2. Есть функция генератор, есть итератор генератора
3. При вызове функции генератора, код, который внутри неё не выполняется.
   Мы просто получим специальный объект генератора (ленивая функция)
4. функция генератор - это функция, которая объект генератора возвращает
   (любая функция внутри которой есть ключевое слово yield).
5. методы __iter__ и __next__ у генераторов создаются автоматически (pp(dir(generator())))
6. с вызовом __next__ происходит итерация функции генератора
7. одна итерация заканчивается на ключевом слове yield
8. значение, которое указано после ключевого слова yield становится
   текущим значением генератора, который и управляет работой данной функции
9. после завершения работы функции интерпретатор вызывает исключение StopIteration
   закончился перебор yield или функция дошла до return - будет StopIteration
10. в принципе генераторы примерно тоже самое, что и итераторы, но писать их проще
11. по сути ключевое слово yield вызывает __next__() у итератора.

 # Внимательно посмотри:
        # Есть функция генератор
        def gen():
            yield 1
            yield 2

        # 1)
        print(gen) # здесь gen обычная функция - <function gen at 0x000002B8D0FACEE0>
        print(*dir(gen), sep='\n') # методов __iter__ и __next__ нету

        # 2)
        print(gen()) # при вызове gen() становится генератором - <generator object gen at 0x000001559F85CCF0>
        print(*dir(gen()), sep='\n') # __iter__ и __next__ появляются

        # 3)
        gen_obj = gen() # присваиваем переменной
        # присваиваем наш генератор переменной gen_obj, создаётся отдельный объект в памяти
        print(gen_obj) # <generator object gen at 0x000002A8AAB8CCF0>
        print(id(gen_obj)) # id gen_obj - 2766960643312
        print(id(gen())) # id gen() - 2099079923296
        # id у gen_obj и gen() различаются, это разные объекты

        # 4)
        print(next(gen_obj)) # 1
        print(gen_obj.__next__()) # 2
        print(gen_obj.__next__()) # StopIteration
        # сравни
        print(next(gen())) # 1
        print(next(gen())) # 1
        print(next(gen())) # 1
        # сам по себе генератор не продолжает итерацию,
        # только если его присвоить переменной
        # но
        print(list(gen())) # [1, 2,]
        # отлично итерируется

        # 5)
        print(type(gen)) # <class 'function'>
        print(type(gen())) # <class 'generator'>
        print(type(gen_obj)) # <class 'generator'>

        # 6)
        gen_obj до итерации и gen после итерации в памяти будут обозначаться одинаково
        <generator object gen at 0x00000227D906C660>

-- Генераторы выражения
1. лучшая аналогия - генераторы выражения по отношению к генераторам
тоже что и lambda по отношению к обычной функции

Приверы генераторов выражения:
    generator2 = (x * y for x in range(5) for y in range(4) if x * y % 2 == 0)
    generator3 = sum(x ** 2 for x in range(10))

-- Подгенераторы
1. использует связку ключевых слов yield from
2. работает в точности также как цикл вложенный в цикл
поднегератор завершает свою работу и внешний генератор её продолжает
3. также использует метод __next__() и ошибку StopIteration

    def generator():
        ...
        yield from subgenerator()
        ...
4. вместо subgenerator() может быть range() или выражение генератора,
или любая друая последовательность - работать будет также

    def subgenerator():
        result = 2
        yield result # 2
        result **= 2
        yield result # 4

    def generator():
        yield 'Hello'
        yield from subgenerator()
        yield 'Bye-Bye'

    for i in generator():
        print(i)

    # # or
    def generator():
        yield 'Hello'
        yield from {1:'a',2:'b',3:'c',}
        yield 'Bye-Bye'

    g = generator()
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

----------------------------------------------------------------------------

***** Итерабельные объекты

Контейнер - это тип данных, который инкапсулирует в себе значение других типов.

Итерабельный объект (iterable) - это объект, который может возвращать значение по одному за раз.
Примеры:
все контейнеры и последовательности (списки, строки и т.д.), файлы, а также экземпляры любых классов,
в которых определён метод __iter__() и/или __getitem__()

Итерабельные объекты могут быть использованы внутри цикла for, а также во многих других
случаях, когда ожидается последовательность (sum, zip, map)

Когда итерабильный объект передаётся во встроенную цункцию iter, она возвращает
итератор для данного объекта, который позволяет один раз пройти по значениям итерабельного объекта


***** Итератор

Итератор - это новый объект, который управляет получением значений из итерабельного объекта
При итерации, из итерируемых оъектов строится такой объект как итератор
Вызов метода __iter__() - возвращает итератор

    print('sdf'.__iter__()) # <str_iterator object at 0x0000016615001160>
    print(iter((1,2,3,))) # <tuple_iterator object at 0x0000016615001160>

Итератор - это объект, который предоставляет поток данных.
Повторяемые вызовы метода __next__() итератора или передача его
его встроенной функции next() возвращает последующие элементы потока.

Если больше не осталось данных, выбрасывается исключение StopIteration.
После этого итератор исчерпан, и любые последующие вызовы метода __next__()
также генерируют исключение StopIteration

Неочевидное - Итераторы ОБЯЗАНЫ ИМЕТЬ МЕТОД __iter__, который возвращает сам объект итератора,
так что любой итератор также является итерабельным объектом и может быть использован
почти везде, где принимают итерабельные объекты

    t = iter(list((1,2,3,)))

    # print(t)
    # print(*dir(t), sep='\n') # тут тоже есть __iter__

    tt = iter(t)
    print(tt)
    print(*dir(tt), sep='\n') # и тут тоже есть __iter__

И выходит, что это один и тот же объект:
    t = iter((1,2,3,))
    tt = t.__iter__()
    t # <tuple_iterator object at 0x00000188EB8D5730>

    tt # <tuple_iterator object at 0x00000188EB8D5730>

    print(id(t)) #  1687579088688
    print(id(tt)) # 1687579088688



итератор - это новый объект, который соответствует итерабельному объекту
при вызове у этого объекта метода __iter__()

Итератор одноразовый, после того как прошлись по этому итератору выбрасывается StopIteration
и нужно заново вызывать итерабельный объект

    s = 'asda'
    for i in s:
        print(s.index(i), i)
        raise StopIteration
    print('finish')

итератор вызывается  функцией iter() которая вызывает метод __iter__() у итерабельного объекта
Если такого метода у объекта нет, то тогда функция ищет метод __getitem__()

__getitem__() - позволяет обращаться к значениям объекта по ключам или индексам

    ls = list(range(5, 15, 2))
    print(ls)
    print(ls[-1]) # 13
    print(ls.__getitem__(-1)) # 13
    print(ls[2]) # 9
    print(ls.__getitem__(2)) # 9

    d = {'a': True, 'b': False,}
    print(d)
    print(d['a']) # True
    print(d.__getitem__('a')) # True

    print(d['b']) # False
    print(d.__getitem__('b')) # False
    print(d.__getitem__('y')) # KeyError: 'y'

Если у итерабельного объекта нет метода __iter__, но есть метод __getitem__,
то если передасть в функцию iter() этот объект,
то она сама для него построит метод __iter__
Но это работает только для __getitem__ который принимает индексы, с ключами это не сработает

Интерфейс итератора состоит из двух методов:
__next__() - основной метод
__iter__() - тоже присутствует у каждого итератора

Любой итератор тоже является итерабельным объектом, и может может быть использован везде
где принимаются итерабельные объекты

Как работает итератор (допрустим при цикле for)

    ls = ['a', 'b', 'c', 'e',]
    it = iter(ls)
    print(next(it)) # a
    print(next(it)) # b
    print(it.__next__()) # c
    print(it.__next__()) # d
    print(it.__next__())# StopIteration

Или так:

    ls = ['a', 'b', 'c', 'e',]
    it = iter(ls)
    while True:
        try:
            print(it.__next__())
        except StopIteration:
            break

Или так:

    def my_for(iterable_obj, callback):
        it = iter(iterable_obj)
        while True:
            try:
                value = it.__next__()
                callback(value)
            except StopIteration:
                break

    def loop_body(value):
        print(f'Next value received - {value}')

    my_for(range(10), callback=loob_body)

***** range(value)

range - итерабельный объект

    r = range(10)
    print(r) # range(0, 10)
    print(type(r)) # <class 'range'>



range() - это по сути способ, сделать объект класса int итерабельным объектом

у int нету метода __iter__ и __getitem__

вот range его и предоставляет, изменяя конечно поведение int

    range(5) + range(7) # TypeError: unsupported operand type(s) for +: 'range' and 'range'

функции reversed(), sorted(), map(), filter(), zip() - являются итераторами
range() - это не итератор, а тип данных


***** генераторы

Функция-генератор - это функция, которая возвращает специальный итератор генератора (generator iterator)
(также объект-генератор - generator object). Она характеризуется наличием ключевого слова yield внури функции

Методы __iter__ и __next__ у генераторов создаются автоматически.

yield замораживает состояние функции генератора и возвращает текущее значение.
После следующего вызова __next__() функция генератор продолжает своё выполнение с того места, где она была
пристановлена.

Когда выполнение функции-генератора завершается (при помощи ключевого слова return
или достижения конца функции), возникает исключение StopIteration

    for i in range(5):
        if i < 3:
            yield i
        else:
            return 'the end'

    gg = g()
    gg.__next__() # 0
    gg.__next__() # 1
    gg.__next__() # 2
    gg.__next__() # StopIteration: the end

Изначально был создан, чтобы упростить написание итераторов
но получился очень мощный механизм, который широко используется в асинхронном программировании

Есть функция генератор, есть итератор генератора

функция генератор - это функция, которая объект генератора возвращает
это любая функция, внутри которой есть ключевое слово yield

Если внутри функции есть ключевое слово yield, то тогда python
сам подстроит вместо функции объект функции генератора

При вызове функции генератора, код, который внутри неё не выполняется.
Мы просто получим специальный объект генератора, который является в свою очередь генератором
И уже при итерации этого объекта будем по кусочкам выполнять данную функцию

Она выполняется до следующего ключевого слова yield
одно выполнение до ключевого слова yield - одна итерация

Простой пример генератора:

    def gen():
        yield 1
        yield 2



    if __name__ == '__main__':

        print(gen) # <function gen at 0x00000189397DCEE0>
        print(gen()) # <generator object gen at 0x00000189392ACCF0>
        # присваиваем этот генератор переменной
        g = gen()
        print(g) # <generator object gen at 0x00000296F49BCCF0>
        print(next(g)) # 1
        print(g.__next__()) # 2
        print(g.__next__()) # StopIteration
        # НО
        print(gen().__next__()) # 1
        print(gen().__next__()) # 1
        # если не присвоить отдельной переменной, то генератор будет запускать функцию заново
        # НО
        print(list(gen())) # [1, 2]
        # итерировать одну функцию можно
        gg = gen()
        # print(*dir(gg), sep='\n')
        # print(gg.close()) # закрывает генератор
        print(gg.gi_code)
        print(gg.gi_frame)
        print(gg.gi_running)
        print(gg.gi_yieldfrom)
        print(gg.send(None))
        print(gg.send(None))
        # print(gg.throw(BaseException)) # BaseException
        # print(gg.__next__())

        # Внимательно посмотри:
        # Есть функция генератор
        def gen():
            yield 1
            yield 2

        # 1)
        print(gen) # здесь gen обычная функция - <function gen at 0x000002B8D0FACEE0>
        print(*dir(gen), sep='\n') # методов __iter__ и __next__ нету

        # 2)
        print(gen()) # при вызове gen() становится генератором - <generator object gen at 0x000001559F85CCF0>
        print(*dir(gen()), sep='\n') # __iter__ и __next__ появляются

        # 3)
        gen_obj = gen() # присваиваем переменной
        # присваиваем наш генератор переменной gen_obj, создаётся отдельный объект в памяти
        print(gen_obj) # <generator object gen at 0x000002A8AAB8CCF0>
        print(id(gen_obj)) # id gen_obj - 2766960643312
        print(id(gen())) # id gen() - 2099079923296
        # id у gen_obj и gen() различаются, это разные объекты

        # 4)
        print(next(gen_obj)) # 1
        print(gen_obj.__next__()) # 2
        print(gen_obj.__next__()) # StopIteration
        # сравни
        print(next(gen())) # 1
        print(next(gen())) # 1
        print(next(gen())) # 1
        # сам по себе генератор не заканчивается
        # но
        print(list(gen())) # [1, 2,]
        # отлично итерируется


Генератор с fibonacci:

    def fibonacci(count):
        first, second = 0, 1
        for _ in range(count):
            yield second
            first, second = second, first + second
        print('loop was ended')
        # здесь return None вызывает StopIteration

    f = fibonaccy(5)
    print(f.__next__()) # 1
    print(f.__next__()) # 1
    print(next(f)) # 2
    print(next(f)) # 3
    print(next(f)) # 5
    print(next(f)) # StopIteration

    ff = fibonacci(10)
    fff = fibonacci(15)

    print(list(ff)) # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    for i in fff:
        print(i)

yield отлично подходит для фибоначчи, т.к. без него всё вычисление начинается с 0 (?)


***** выражения генераторы

Это просто пример синтаксиса генератора:

    def gen_func():
        for x in range(5):
            for y in range(4):
                result = x * y
                if result % 2 == 0:
                    yield result


    generator = gen_func()
    print(gen_func) # <function gen_func at 0x000001B2E547CEE0>
    print(gen_func()) # <generator object gen_func at 0x000001B2E546C660>
    print(generator) # <generator object gen_func at 0x000001B2E53FCCF0>

    for item in generator:
        print(item)

а можно этот же самый генератор записать в виде одной строки:

    generator2 = (x * y for x in range(5) for y in range(4) if x * y % 2 == 0)

    for item in generator2:
        print(item)

    print(generator2) # <generator object <genexpr> at 0x0000027315F7C9E0>

Это будет тоже самое.

Этакой такой сокращённый способ записи подобных генераторов
по аналогии как обычная функция и lambda
как объект выводится так - <generator object <genexpr> at 0x00000214EFD5CAC0>

вот тоже пример генератора genexpr:

    # сумма всех кватратов от 0 до 9
    result = sum(x ** 2 for x in range(10))
    print(result) # 285


***** подгенераторы

Подгенераторы (subgenerators) - делегирование к подгенераторам если в функции-генераторе
встречается пара коючевых слов yield from, после которых следует объект генератор,
то данный генератор делегирует доступ к подгенератору, пока он не завершится
(не закончатся его значения), после чего продолжает своё исполнение.

def generator():
    ...
    yield from subgenerator()
    ...

Очень похоже на вложенный цикл. Работает также.
Не даром yield from работает с любым итерабельным объектом

Пример подгенератора (скорее подитератора)

    def generator_with_subiterator():
        yield 'Hello'
        yield from range(10)
        yield 'Bye-Bye'

    for i in generator_with_subiterator():
        print(i)

пример подгенератора (выражения генератора):

    def generator_with_subgenerator():
        yield 'Hello'
        yield from (x ** 2 for x in range(5))
        yield 'Bye-Bye'

    for i in generator_with_subgenerator():
        print(i)

ну и полноценный подгенератор:

    def subgenerator():
        result = 2
        yield result # 2
        result **= 2
        yield result # 4

    def generator():
        yield 'Hello'
        yield from subgenerator()
        yield 'Bye-Bye'

    for i in generator():
        print(i)

Т.е. когда итерируется выражение подгенератора, то также используется метод __next__()
Дальше при использовании подгенератора, когда итерация заканчивается
вызывается исключение StopIteration, и внешний итератор после
StopIteration от подгенератора - продолжает свою работу


***** методы генераторов

    def generator():
        yield 'Hello'
        yield from range(10)
        yield 'Bye-Bye'
    print(*dir(generator()), sep='\n')

Есть такие:
    - __next__() - начинает или продолжпет исполнение функции генератора. Результат текущего
                yield-выражения, будет равен None. Выполнение затем продолжается до следующего
                yield-выражения, которое выдаёт значение туда, где был равен __next__.
                Если генератор завершается без выдачи значения при помощи yield,
                возникает исключение StopIteration. Метод обычно вызывается неявно,
                т.е. циклом for или встроенной функцией next()
    - close() - выбрасывает исключение GeneratorExit в месте где был приостановлен генератор
                Если генератор возвращает очередное значение, выбрасывается исключение RuntimeError
    - gi_code
    - gi_frame
    - gi_running
    - gi_yieldfrom
    - send(value) - продолжает выполнение и отправляет значение в функцию-генератор.
                    аргумент value становится значением текущего yield-выражения.
                    Возвращает выдданое значение. Если send() используется для запуска генератора
                    , то единственным допустимым значением является None, т.к. ещё не было выполнено ни одно
                    yield-выражение, которому можно присвоить это значение.
    - throw(type, [, value[, traceback]])  - выбрасывает исключение типа type в месте, где был приостановлен
                    генератор, и возвращает следующее значение генератора (или выбрасывает StopIteration)


***** выражение yield

На самом дела yield вляется выражением. Оно может принимать значения,
которые отправляются в генератор. Если в генератор не отправляются значения,
результат даного выражения равен None

yield from также является выражением. Его результатом является то значение,
которое подгенератор возвращает в исключении StopIteration (для этого значение возвращается
при помощи ключевого слова return).

yiled вообще как-то сильно связан с асинхронным программированием,изучи этот вопрос получше

    def generator():
        ...
        data = yield
        ...


***** Сопрограмма

sources:
    https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0

Сопрограмма (coroutine) - компонент программы, обощающий понятие подпрограммы,
который дополнительно поддерживает множество входных точек (а не одну, как подпрограмма)
и остановку и продолжение выполнения с сохранением определённого положения.

Расширенные возможности генераторов в python (выражение yield и yield from, отправка
значений в генераторы) используются для реализации сопрограмм

Сопрограммы полезны для реализации асинхронных неблокирующих операций
и кооперативной многозадачности в одном потоке без использования функций
обратного вызова (callback-функций) и написания асинхронного кода
в синхронном стиле

Python включает в себя поддержку сопрограмм на уровне языка. Для этого используется
ключевые слова async и await


По сути выражение yield и нужно для этих сопрограмм

Нужно выполнить такую-то асинхронную операцию и подождать её результата

если говорить в терминах генератора, то фраза "подождать результата" и означает yield from

отличный пример реализации сопроцедуры

ctrl + r
******** 5)

---------- practice -----------

******** 1)
Простой итератор, основанный на __getitem__

    # class SimpleIterator:
    #     def __getitem__(self, item):
    #         if 0 <= item <= 5:
    #             return item ** 2
    #         else:
    #             raise IndexError
    #
    # iterable_obj = SimpleIterator()
    #
    # for i in iterable_obj:
    #     print(i)
    #
    # it = iter(iterable_obj) # it - итератор
    # print(*dir(it), sep='\n') # у итератора появляется метод __iter__,
    # # хотя в SimpleIterator мы его не определяли

при инетерации через цикл for появится итератор как объект,
который сам создаст метод __iter__


******** 2)
Пример MyRange (аналог range) который строит итератор на основе __getitem__ и на основе __iter__

    # from math import ceil
    #
    #
    # class MyRange:
    #
    #     def __init__(self, start, end=None, step=1):
    #         if end is not None:
    #             self.start = start
    #             self.end = end
    #         else:
    #             self.start = 0
    #             self.end = start
    #
    #         if step != 0:
    #             self.step = step
    #         else:
    #             raise ValueError("step cannot be zero")
    #
    #         self.length = ceil((self.end - self.start) / self.step)
    #
    #     def __len__(self):
    #         return self.length
    #
    #     def __getitem__(self, item):
    #         if 0 <= item < len(self):
    #             return self.start + item * self.step
    #         else:
    #             raise IndexError('Index out of MyRange')
    #
    #     def __iter__(self):
    #         # return IteratorForMyRange(self) # это если использвать обычный итератор
    #
    #         # ниже идёт генератор. он заменяет
    #         # итератор IteratorForMyRange полностью
    #         current = self.start
    #         for _ in range(len(self)):
    #             yield current
    #             current += self.step
    #
    #
    #     def __repr__(self):
    #         return f"MyRange({self.start}, {self.end}, {self.step})"
    #
    #
    # class IteratorForMyRange:
    #     def __init__(self, iterable_obj):
    #         self.iterable_obj = iterable_obj
    #         self.next_value = self.iterable_obj.start
    #         self.end = self.iterable_obj.end
    #         self.step = self.iterable_obj.step
    #
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         if any((
    #                 (self.next_value > self.end and self.step > 0),
    #                 (self.next_value < self.end and self.step < 0),
    #         )):
    #             raise StopIteration
    #         else:
    #             result = self.next_value
    #             self.next_value += self.step
    #             return result
    #
    #
    # def main():
    #     # it = MyRange(10)
    #     # for i in it:
    #     #     print(i)
    #     # print()
    #     # it2 = MyRange(3, 16, 3)
    #     # for i in it2:
    #     #     print(i)
    #     # print()
    #     it3 = MyRange(20, 1, -1)
    #     # for i in it3:
    #     #     print(i)
    #
    #     itt = iter(it3)
    #     # уже при использовании генератора вместо итератора как отдельного класса:
    #     print(itt) # <generator object MyRange.__iter__ at 0x000001A638539660>
    #     print(itt.__next__())
    #     print(next(itt))
    #     print('*'*50)
    #     for i in itt:
    #             print(i)
    #
    #
    # if __name__ == '__main__':
    #     main()


******** 3)

про односвязный список
sources:
    просто гугли
sources:
    https://otus.ru/nest/post/664/

Здесь мы реализовали односвязный список.
Односвязанный список - это такая сруктура в которой у вас есть последовательность элементов
лежащие в разных местах памяти, каждый из которых хранит значение этого элемента
и ссылку на следующий элемент данного списка
У такого списка будут значительно медленнее получение элементов по индексу,
но значительно быстрее вставка элемента в произвольное место

До конца в этом коде не разобрался, он работает как-то рекурсивно, если верить дебаггеру

Скорее всего вся суть в этих строчках:
        if len(self) == 0:
            self._head = self._tail = node
        else:
            # типо здесь <self._tail._next = node> не только для self._tail._next сохраняется
            # но и для self._head._next, мне так кажется
            self._tail._next = node
            self._tail = node

Типо значение сохраняется по цепочке

В методе __getitem__ где строчка:
    node = self._head

залочь точку для дебаггера и посмотри,
особенно значение переменных, особенно _next

# class List:
#     class _Node:
#
#         __slots__ = ('value', '_next',)
#
#         def __init__(self, value, _next=None):
#             self.value = value
#             self._next = _next
#
#     class _NodeIterator:
#         '''
#             наш итератор, который ускоряет перебор элементов в этом списке
#             если мы просчитываем по __getitem__ то итератор будет возвращаться каждый раз в начало
#             это замедляет работу.
#             С помощью этого итератора переборпроисходит быстрее
#         '''
#
#         def __init__(self, first):
#             self._next_node = first
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             if self._next_node is None:
#                 raise StopIteration
#
#             result = self._next_node.value
#             self._next_node = self._next_node._next
#
#             return result
#
#     def __init__(self, iterable=None):
#         self._head = None  # первый элемент списка
#         self._tail = None  # хвост, или конец списка
#         self._length = 0
#
#         if iterable is not None:
#             self.extend(iterable=iterable)
#
#     def __len__(self):
#         return self._length
#
#     def append(self, obj):
#         node = List._Node(obj)
#
#         if len(self) == 0:
#             self._head = self._tail = node
#         else:
#             # т.е. получается здесь и для self._head._next мы тоже изменяем
#             self._tail._next = node
#             self._tail = node
#
#         self._length += 1
#
#     def extend(self, iterable):
#         for obj in iterable:
#             self.append(obj)
#
#     def __getitem__(self, index):
#         if index < 0:
#             index += len(self)
#
#         if not 0 <= index < len(self):
#             raise IndexError('my List index out of range')
#
#         node = self._head  # здесь залочить точку для дебага
#         for i in range(index):
#             node = node._next
#
#         return node.value
#
#     def __iter__(self):
#
#         '''
#             наш итератор, который ускоряет перебор элементов в этом списке
#             если мы просчитываем по __getitem__ то итератор будет возвращаться каждый раз в начало
#             это замедляет работу.
#             С помощью этого итератора перебор происходит быстрее
#         '''
#         # return List._NodeIterator(self._head) # итератор определённый выше
#         # or
#         # return self._NodeIterator(self._head)
#         # or
#         # Мы можем использовать генератор с yield и он полностью нам заменит
#         # генератор _NodeIterator:
#         node = self._head
#         while node:
#             yield node.value
#             node = node._next
#         # и также итератор не будет начинать с первого элемента,
#         # как он это делает, когда итерирует с помощью __getitem__
#
#
#
#
# l = List([4, 3, 2, 754, 23])
# # print(l[0])
# # print(l[1])
# # print(l[2])
#
# # for i in l:
# #     print(i)
# data = List(range(1000 ** 2))
# print(iter(data)) # <generator object List.__iter__ at 0x000002368920ED60>
#
# # попробуй запустить этот цикл с итератором
# # и выключенным итератором (методом __iter__),
# # for i in data:
# #     if i % 1000 == 0:
# #         print(i)


******** 4) Уже мой пример - класс  Int

Int можно итерировать и доставать элементы по индексам,
но конечно если попытаться сложить с чем то, или сделать другую операцию,
то Int превратится в обычный int
для операций в этом классе нужно определить волшебные методы

    # class IteratorInt:
    #
    #     def __init__(self, integer):
    #         self._next = 0
    #         self._tail = integer
    #
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         if self._next < self._tail and 0 < self._tail:
    #             result = self._next
    #             self._next += 1
    #             return result
    #         elif self._next > self._tail and 0 > self._tail:
    #             result = self._next
    #             self._next -= 1
    #             return result
    #         else:
    #             raise StopIteration
    #
    # class Int(int):
    #
    #     def __iter__(self):
    #         # return IteratorInt(self)
    #         # # or
    #         for _ in range(self):
    #             yield _
    #
    #
    #
    #     def __getitem__(self, item):
    #         return range(self)[item]
    #
    #     def print_int(self):
    #         print(self)
    #         return self
    #
    #
    # i = Int(5)
    # print(i)
    # print(type(i))
    # print(i + 5)
    # i = Int(i ** 2)
    # print(i)
    # print(type(i))
    # # print(i.print_int())
    # print(list(i))
    # for _ in i:
    #     print(_)
    # print(i[2])


******** 5)

Пример кооперативной многозадачности (сопроцедуры)

Здесь мы реализовали два бесконечных цикла,
которые исполняются параллельно, и один из них
отправляет данные в другой.
И всё это происходит в одном потоке исполнения, с точки
зрения операционной системы.
Это пример кооперативной многозадачности
Вот примерно для этого и нужны сопроцедуры

Именно таким образом реализуются сопроцедуры в python

    # import time
    # import random
    #
    # def sleep(seconds):
    #     start = time.time()
    #     while time.time() - start < seconds:
    #         yield
    #
    #
    # def produce(consumer):
    #     while True:
    #         yield from sleep(1)
    #         data = random.randint(1, 100)
    #         consumer.send(data)
    #         # здесь мы посылаем это consumer (функция consume())
    #
    #
    # def consume():
    #     _sum = 0
    #     _count = 0
    #
    #     while True:
    #         # а здесь получается yield будет то число, которое мы послали в функции produce()
    #         # т.е. мы из функции produce передаём данные для yield
    #         data = yield
    #         print(f'Count: {_count}', '*'*_count)
    #         print(f'Got data: {data}')
    #         _sum += data
    #         _count += 1
    #
    #         print(f'Sum: {_sum}')
    #         print(f'Average: {_sum / _count}')
    #         print()
    #
    # def another_task(): # типо какай то код, который будет выполняться параллельно
    #     while True:
    #         print('\n','Hello from another task', '\n')
    #         yield from sleep(2)
    #
    # if __name__ == '__main__':
    #     consumer = consume()
    #     consumer.__next__()
    #
    #     producer = produce(consumer=consumer)
    #     task = another_task()
    #     while True:
    #         task.__next__() # пример того, что мы можем выполнять что-то на фоне этих функций
    #         next(producer)


******** 6)

Реализация сопроцедуры в пункте 5) только с пакетом asyncio
Но в итоге так не получилось (не работает consume())

    # import time
    # import asyncio
    #
    #
    #
    # async def produce():
    #     await asyncio.sleep(0.5)
    #     data = random.randint(1, 100)
    #     return data
    #
    #
    # async def consume():
    #     _sum = 0
    #     _count = 0
    #
    #     while True:
    #         # а здесь получается yield будет то число, которое мы послали в функции produce()
    #         data = await produce()
    #         print(f'Count: {_count}', '*'*_count)
    #         print(f'Got data: {data}')
    #         _sum += data
    #         _count += 1
    #
    #         print(f'Sum: {_sum}')
    #         print(f'Average: {_sum / _count}')
    #         print()
    #
    # async def another_task():
    #     while True:
    #         print('\n','Hello from another task', '\n')
    #         await asyncio.sleep(1)
    #
    #
    # if __name__ == '__main__':
    #     loop = asyncio.get_event_loop()
    #     tasks = [consume(), another_task()]
    #     loop.run_until_complete(asyncio.wait(tasks))
  """
