"""
-------------------------------------------------- Множества и отображения --------------------------------------------------

-------------------------------------------------------------------------------------------------------
Множекства:
    - set
    - frozenset

Отображения:
    - dict

*** хешируемые объекты
1) хеш значение - это какое-то целое число, которое характеризирует значение данного объекта
   в виде одного единственного целого числа
2) равные хешируемые объекты имеют равные хеш-значения.
   поэтому сравнения хешируемых объектов идет по хеш-значениям
3) хеш-значение объекта не должно изменяться на протяжении жизни объекта -
   от создания, до удаления из памяти
4) только хешируемые объекты могут быть использованы как ключи словарей и члены множеств
   на основе хеш-значений, и на основе вычислений хеш-функций объектов
   строятся все алгоритмы хранения значений set, frozenset и dict
5) у хешируемого объекта должны быть реализованы методы __hash__() и __eq__()
   это нужно чтобы очень сложные по структуре объекты очень быстро сравнивать на рвенства
   но у нехешируемые объектов тоже есть эти методы, просто __hash__ вызываться не будет (TypeError)

        hasattr(object, '__hash__') # True
        hasattr(object, '__eq__') # True
        [1,2,3,].__hash__() # TypeError


6) все стандартные НЕизменяемые объекты хешируемые.
7) все стандартные изменяемые объекты НЕ хешируемые.
   если объект изменяемый, и его изменеие влияет на сравнение на
   равенство с другими объектами то такой объект не может быть хешированным
8) у хешированных объектов python при сравнении этих объектов сравнивает их хеш-значения
   это нужно чтобы очень сложные по структуре объекты
   очень быстро сравнивать на рвенства.

    'abc' == 'abc'
    hash('abc') == hash('abc')
    360844340944764323 == 360844340944764323

9) хеш-значение от int - это само число

    hash(23) # 23

Хешируемые объекты:
    - tuple
    - frozenset
    - str
    - int
    - float
    - range
    - bytes

Не хешируемые объекты:
    - dict
    - set


*** множества set

1) множество - это неупорядоченная коллекция хешируемых объектов, которые не повторяются
2) обычно используется для выполнения таких операций, как
    - вхождение в множество
    - удаление повторений элементов
    - объединение
    - пересечение
    - разница
    - симметрическая разница

3) в множестве нет понятия позиции элемента, они не поддерживают индексауию и срезы
   в множестве нет порядка у элемента, он может идти как угодно
4) только хешируемый объект может стать элементом множества
5) set - изменяемое множество (НЕхешированный тип данных)
6) frozenset - неизменяемое множество (хешированный тип данных)
7) в отличии от списков - операция in работает очень быстро
   ради этой операции множества и созданы (все лишние элементы удаляются)

операции множества:
sources:
       https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
       https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
Операции множества, делятся на три категории (для frozenset действительны первые две категории):

1) Действительно для set и frozenset.
   Операции, которые принимают другое множество и возвращают True или False

    x in s
    x not in s
    s.isdisjoint(other) - True если не имеют общих элементов
    s.issubset(other) or set <= other or set < other
    s.issuperset(other) or set >= other or set > other

2) Действительно для set и frozenset.
   Операции, и которые никак не изменяют объект в памяти, а создают новый объект
   Могут принимать любой итерабельный объект, не только set

    s.union(*others) or set | other | ...
    s.intersection(*others) or set & other & ...
    s.difference(*others) or set - other - ...
    s.symmetric_difference(other) or set ^ other
    s.copy() !!! - неполная копия

3)  Действительно ТОЛЬКО для set.
    Операции, которые изменяют множество непосредственно, объект в памяти остаётся тот же

    s.update(*others) or set |= other | ...
    s.intersection_update(*others) or set &= other & ...
    s.difference_update(*others) or set -= other | ...
    s.symmetric_difference_update(other) or set ^= other
    s.add(elem)
    s.remove(elem) - удаляет элемент если он есть или KeyError
    s.discard(elem) - удаляет элемент если он есть и ничего не делает если его нет (discard - отказаться)
    s.pop() KeyError если множество пустое
            pop() нужен чтобы обходить множества с
            удалением тех элементов, которые мы уже обработали
            очень полезно при реализации алгоритмов для графов
    s.clear()




Операции над множествами, которые являются методами, принимают в качестве аргуметов
любые итерабельные объекты, только если это не добавление одного элемента,
т.к. нехешированные объекты не могут являться элементом множества.
Операции над множетвами, записанные в виде бинарных операций, требуют,
чтобы второй операнд операции тоже был множеством, и возвращают множество
того типа, которым было первое множество.

Как сделать множество множеств:

     s = {1,2,3,}
     t = set(range(4,7))

     множество множеств:
     ss = {frozenset(s), frozenset(t),} # {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

     s in {frozenset({1, 2, 3}), frozenset({4, 5, 6})} # True

Ну и помни, что:

        set([1,2,1.0]) # {1,2}


*** dict

help(dict)
print(*dir(dict), sep='\n')


dict - ассоциативный массив

Отображение (mapping) - это объект-контейнер, который поддерживает произвольный доступ
к элементам по ключам. Т.е. как-бы отображают одни значения по другим.

sources:
    https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

методы не изменяющие объект
 - get(key, default=None)
 - items()
 - keys()
 - values()

методы изменяющие объект
 - setdefault(key, default=None)
 - clear()
 - pop()
 - popitem()
 - update()

Операции со словарями и другими отображениями
    len(d)
    d[key]
    d[key] = value
    key in d
    key not in d
    iter(d) - тоже самое что и iter(d.keys())
    d.clear()
    d.copy()

    @classmethod
    dict.fromkeys(sequence[, value]) -- создаёт новый словарь с ключами из последовательности sequence
                                    и заданным значением по умолчанию None
                                    обрати внимание, что это классовый метод
                                    dict.fromkeys([1,2,3],'a') # {1: 'a', 2: 'a', 3: 'a'}

    d.get(key[, default]) -- скорее всего реализован не через __getitem__(item)
    d.items() -- возвращает объект представления словаря
    d.keys() -- возвращает объект представления словаря, соответствующий ключам словаря
    d.values() -- возвращает объект представления словаря, соответствующий значениям словаря
    d.pop(key[, default]) -- если ключ key существует, удаляет элемент из словаря и возвращает значение
                             если ключ key НЕ существует, и задано значение default - возвращает default
                             иначе выбрасывается KeyError
    d.popitem() -- удаляет произвольную пару ключ-значение и возвращает её. Если словарь пустой,
                   возникает исключение KeyError
    d.setdefault(key[, default]) -- если ключ key существует, возвращает соответствующее значение
                             если ключ key НЕ существует, создаёт элемент с ключом key и значением default
                             default по умолчанию равен None
    d.update(mapping) -- принимает либо другой словарь или отображение, либо итерабельный объекь,
                         состоящий из итерабельных объектов - пар ключ-значение, либо именованные аргументы
                         Добавляет соответствующие элементы в словарь.

помни, что 1 == 1.0
поэтому лучше не использовать float в качестве ключей

Единственным встроенным отображением является тип данных dict, но
мы имеем также другие виды отображений из встроенной библиотеки collections
(все они наследуются от dict):

 collections.default
 collections.OrderedDic
 collections.Counter


*** объекты представления словаря keys() values() items()

help(dict(a=1).items()) # values() keys()
print(*dir(dict(a=1).items()), sep='\n')
print(type(dict(a=1).values())) # items() keys()

1) объекты представления вызываются методами keys(), values(), items()
2) они динамически зависимы от объекта словаря, от которого их вызвали
3) при этом это отдельный объект в памяти со своим id
   и не удаляется при удалении словаря
4) с ними можно проводить три операции - in, __len__() и __iter__()
5) изменять их нельзя
6) при итерировании объект отображения нельзя изменять словарь,
   иначе будет RuntimeError
7) реализуют интерфейс множества, т.е. можно выполнять операции с объектами представления
   такие операции с множеством
   и так:
        - реализует методы полностью из первой (где True, False)
        - реализует методы полностью из второй (кроме copy())
          но только с альтернативным вызовом с
          помощью знаков & | - ^ а не с помощью методов
        - НЕ реализует из третьей методы, где меняется сам объект

-- При итерировании объект отображения нельзя изменять словарь,
   иначе будет RuntimeError
    d = {1: 'a', 2: 'b', 3: 'c'}

    dk = d.keys()

    for k in dk:
        d[k ** 2] = str(k) # RuntimeError: dictionary changed size during iteration


-- Если мы удалим словарь, то объекты представления привязанные к нему останутся

    d = {'a':1}
    dv = d.values()
    di = d.items()
    del d # удаляем словарь
    dv
    dict_values([1]) # объекты представления остались
    di
    dict_items([('a', 1)]) # объекты представления остались

-- Мы можем выполнять те-же методы от множеств, что возвращают True или False

    d = {1: 'a', 2: 'b', 3: 'c'}
    dk = d.keys()
    dv = d.values()
    s = {1, 2, 4, 5, 6,}
    print(dk.isdisjoint(s)) # True (если нет общих элементов)
    print(s)
    dk.intersection_update(s)) # AttributeError
    s.update(dk) # {1, 2, 3, 4, 5, 6}
    print(dk & s) # {1, 2} (этот метод из второй категории)
    print(d.values() & dd.values())
    print(d.values().intersection(dd.values())) # а вот так нельзя, хоть это и таже операция  &

-- При итерации словаря python вызывает метод keys()

    d = {1:'a'}
    dv = d.values()
    dk = d.keys()
    dv_it = dv.__iter__() # <dict_valueiterator object at 0x000002B2800F5DB0>
    dk_it = dk.__iter__() # <dict_keyiterator object at 0x000002B280117AE0>
    dict_it  = d.__iter__() # <dict_keyiterator object at 0x000002B28013AC70>
-------------------------------------------------------------------------------------------------------

Множекства:
    - set
    - frozenset

Отображения:
    - dict

***** Хешируемые оьъекты

Объект называются хешируемым, если он имеет хеш-значение (целое число),
которое никогда не изменяется на протяжении его жизненного цикла и возвращается
методом __hash__(), и может сравниваться с другими объектами (реализуется метод __eq__())
Равные хешируемые объекты должны иметь равные хеш-значения.

Хешируемые объекты могут быть использованы как ключи словарей и члены множеств.

Все стандартные НЕизменяемые объекты хешируемые.

Все стандартные изменяемые объекты НЕ хешируемые.

Хешируемые объекты:
    - tuple
    - frozenset
    - str
    - int
    - range
    - bytes

Не хешируемые объекты:
    - dict
    - set

У хешируемых объектов определён метод __hash__()

Функция hash() вызывает у хешируемого объекта метод __hash__()

    print([1,2,3,].__hash__()) # TypeError
    print(frozenset([1,2,3,]).__hash__()) # -272375401224217160
    print(bytes(5).__hash__()) # 6411338102007555754


хеш значение - это какое-то целое число, которое характеризирует значение данного типа
в виде одного единственного целого числа

Хеш значение объекта не должно изменяться на протяжении жизни объекта -
от создания, до удаления из памяти

У хешируемые объектов два метода обязательные:

    __hash__() - возвращает хеш-значение обхъекта
    __eq__() - метод позволяющий сравнивать объекты

Это нужно чтобы очень сложные по структуре объекты
 очень быстро сравнивать на равенства

Если два хешированные объекта равны между собой,
то их хеш-значения обязательно равны

То что два объекта неравны между собой - мы можем это сделать моментально,
если они не являются хешированными - просто проверить их хеш-значение

Самое интересное, что нехешируемые объекты тоже имеют метод __hash__():

        print(hasattr(list, '__hash__')) # True
        print(hasattr(set, '__hash__')) # True
        print(hasattr(dict, '__hash__')) # True
        print(hasattr(tuple, '__hash__')) # True
        print(hasattr(frozenset, '__hash__')) # True
        print(hasattr(int, '__hash__')) # True
        print(hasattr(str, '__hash__')) # True
        print(hasattr(bytes, '__hash__')) # True

Экземпляры класса тоже имеют этот метод (всё по правилам ООП)

t = 1,2,3,
hasattr(t, '__hash__') # True
hash(t) # 529344067295497451

ls = [1,2,3,]
hasattr(ls, '__hash__') # True
hash(ls) # TypeError: 'NoneType' object is not callable


На основе хеш-значений, и на основе вычислений хеш-функций объектов
строятся все алгоритмы хранения значений множест - set и frozenset и словарей - dict


Почему мутабельные объекты не могут быть хешированными?

Если объект изменяемый, и его изменеие влияет на сравнение на равенство с другими объектами
то такой объект не может быть хешированным
Ведь хеш-значение не изменяется на протяжении жизни объекта:

допустим есть два словаря
    1) есть два словаря
    d = {1:'a'}
    dd = {1:'a'}

    Если бы у них было хеш-значение,
    то оно было бы одинаковым, т.к. они равны

    d == dd # True

    2) изменяем один словарь
    d[2] = 'b'

    3) они уже не равны, т.к. второй словарь не изменялся
    d == dd # False

    4) но хеш значение (если бы оно у них было) было бы одинаковым,
    ведь оно не может меняться. И тогда два этих объекта были бы равны
    ведь у хешированных объектов при сравнении сравниваются хеш-значение
    как видим это не логично, ведь объекты уже отличаются

Этот пример иллюстрирует почему мутабельные объекты не могут быть хешированными


***** множества


Множество - это неупорядоченная коллекция хешируемых объектов, которые не повторяются

Обычно используется для проверки элемента на вхождение в множество
и удаление повторений элементов и выполнение таких операций, как
    - объединение
    - пересечение
    - разница
    - симметрическая разница

В множестве нет понятия позиции элемента.
Соответственно, они не поддерживают индексауию и срезы

    hasattr(set, '__getitem__') # False
    hasattr(frozenset, '__getitem__') # False

Встроенные классы множеств:
    set - изменяемое множество (НЕхешированный тип данных)
    frozenset - неизменяемое множество (хешированный тип данных)


В отличии от списков - операция in работает очень быстро
Ради этой операции множества и созданы (все лишние элементы удаляются)

операции множества:
sources:
       https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
       https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

Операции множества, делятся на три категории (для frozenset действительны первые две категории):

1) Действительно для set и frozenset.
   Операции, которые принимают другое множество и возвращают True или False

    x in s
    x not in s
    s.isdisjoint(other)
    s.issubset(other) or set <= other or set < other
    s.issuperset(other) or set >= other or set > other

2) Действительно для set и frozenset.
   Операции, и которые никак не изменяют объект в памяти, а создают новый объект
   Могут принимать любой итерабельный объект, не только set

    s.union(*others) or set | other | ...
    s.intersection(*others) or set & other & ...
    s.difference(*others) or set - other - ...
    s.symmetric_difference(other) or set ^ other
    s.copy() !!! - неполная копия

3)  Действительно ТОЛЬКО для set.
    Операции, которые изменяют множество непосредственно, объект в памяти остаётся тот же

    s.update(*others) or set |= other | ...
    s.intersection_update(*others) or set &= other & ...
    s.difference_update(*others) or set -= other | ...
    s.symmetric_difference_update(other) or set ^= other
    s.add(elem)
    s.remove(elem) - удаляет элемент если он есть или KeyError
    s.discard(elem) - удаляет элемент если он есть и ничего не делает если его нет
    s.pop() KeyError если множество пустое
            pop() нужен чтобы обходить множества с
            удалением тех элементов, которые мы уже обработали
            очень полезно при реализации алгоритмов для графов
    s.clear()

Операции над множествами, которые являются методами, принимабт в качестве аргуметов
любые итерабельные объекты, только если это не добавление одного элемента,
т.к. нехешированные объекты не могут являться элементом множества.
Операции над множетвами, записанные в виде бинарных операций, требуют,
чтобы второй операнд операции тоже был множеством, и возвращают множество
того типа, которым было первое множество.


если в кратце, то у множества есть операции которые его изменяют,
и которые никак не изменяют объект в памяти, а проводят какое-то сравнение
и возвращают результат сравнения
операции множества:
sources:
       https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset
       https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html

У frozenset разумеется операции, которые возвращают True или False (кроме union)

с методом union у frozenset довольно интересно:

    1 - Создаём объект множества:
    s = frozenset((1,2,3,))

    print(id(s), s, hash(s), sep='\n') # 2965675843136
                                       # frozenset({1, 2, 3})
                                       # -272375401224217160

    2 - Проводим операцию union (хоть и в принте)
    Как видим id и хэш-значение другое, значит это другой объект в памяти
    print(id(s.union((4, 5))), s.union((4, 5)), hash(s.union((4, 5))), sep='\n')

                                       # 2967810110176
                                       # frozenset({1, 2, 3, 4, 5})
                                       # -3779889356588604112

    3 - Но сам объект множеста s никак не изменился
    print(id(s), s, hash(s), sep='\n') # 2965675843136
                                       # frozenset({1, 2, 3})
                                       # -272375401224217160



*** проверка на равенство множеств

Множества можно проверять на равенства друг другу

    {2,3,4} == {3,4,2,} # True
    {2,3,4, 5} == {3,4,2,} # False

При сравнении множест типы данных не проверяются, проверяются только элементы
 - что их кол-во одинаково
 - что все элементы первого множества являются элементам второго множества и наоборот

    {1,2,3,} == frozenset([1,2,3,]) # True

Операцию == изнутри использует операция in

нехешированный объект не может являться элементов множества.
Но как быть с множеством множест?
ответ очень прост

     s = {1,2,3,}
     t = set(range(4,7))

     множество множеств:
     ss = {frozenset(s), frozenset(t),} # {frozenset({1, 2, 3}), frozenset({4, 5, 6})}

     s in {frozenset({1, 2, 3}), frozenset({4, 5, 6})} # True

Таким образом мы можем избавиться от лишних множеств,
если они нам не нужны



***** dict

dict - ассоциативный массив

Отображение (mapping) - это объект-контейнер, который поддерживает произвольный доступ
к элементам по ключам. Т.е. как-бы отображают одни значения по другим.

Единственным встроенным отображением является тип данных dict, но
мы имеем также другие виды отображений из встроенной библиотеки collections
(все они наслежуются от dict):

 collections.default # его там нет
 collections.OrderedDict
 collections.Counter


Отображение реализует методы, описанные в абстрактном базовом
класса collections.Mapping:
from collections import Mapping

методы не изменяющие объект
 - get(key, default=None)
 - items()
 - keys()
 - values()

Изменяемые отображения также должны поддерживать следующие методы,
описанные в абстрактном базовом классе collections.MutableMapping
from collections import MutableMapping

методы изменяющие объект
 - setdefault(key, default=None)
 - clear()
 - pop()
 - popitem()
 - update()


class C:
    attr = 1

C.__dict__  # mappingproxy({'__module__': '__main__', 'attr': 1, '__dict__': <attribute '__dict__' of 'C' objects>, '__weakref__': <attribute '__weakref__' of 'C' objects>, '__doc__': None})
type(C.__dict__) # <class 'mappingproxy'>

Как мы видим этот атрибут реализуется с помощью класса mappingproxy



Встроенным классом отображения является dict, который реализует такую страктуру данных,
как словарь, или ассоциативный массив, т.е. неупорядоченную изеняемую коллекцию пар (ключ, значение),
которая поддерживает произвольный доступ к её элементам по их ключам.

Ключи словарей должны быть хешируемыми значениями.

int(1) и float(1.0) - являются одинаковыми ключами
но т.к. float(1.0) сохраняет приблизительно своё значение его лучше не использовать


Операции со словарями и другими оотображениями
    len(d)
    d[key]
    d[key] = value
    key in d
    key not in d
    iter(d) - тоже самое что и iter(d.keys())
    d.clear()
    d.copy()

    @classmethod
    dict.fromkeys(sequence[, value]) -- создаёт новый словарь с ключами из последовательности sequence
                                    и заданным значением по умолчанию None
                                    обрати внимание, что это классовый метод
                                    dict.fromkeys([1,2,3],'a') # {1: 'a', 2: 'a', 3: 'a'}

    d.get(key[, default]) -- скорее всего реализован не через __getitem__(item)
    d.items() -- возвращает объект представления словаря
    d.keys() -- возвращает объект представления словаря, соответствующий ключам словаря
    d.values() -- возвращает объект представления словаря, соответствующий значениям словаря
    d.pop(key[, default]) -- если ключ key существует, удаляет элемент из словаря и возвращает значение
                             если ключ key НЕ существует, и задано значение default - возвращает default
                             иначе выбрасывается KeyError
    d.popitem() -- удаляет произвольную пару ключ-значение и возвращает её. Если словарь пустой,
                   возникает исключение KeyError
    d.setdefault(key[, default]) -- если ключ key существует, возвращает соответствующее значение
                             если ключ key НЕ существует, создаёт элемент с ключом key и значением default
                             default по умолчанию равен 0
    d.update(mapping) -- принимает либо другой словарь или отображение, либо итерабельный объекь,
                         состоящий из итерабельных объектов - пар ключ-значение, либо именованные аргументы
                         Добавляет соответствующие элементы в словарь.



***** Объекты представления словаря keys() values() items()

методы keys() values() items() являются объектами представления словаря
Они предоставляют динамическое представление элементов словаря, т.е. изменения данного словаря
автоматичеси отображаются на этих объектах

Операции с представлениями словарей:

    - iter(dictview) -- представления словарей итерабельны как и сами словари
                        print(hasattr(dict(a='a').values(), '__iter__'))
                        Несмотря на то что в словаре порядка нет,
                        представление словаря соблюдает порядок (?)
                        При попытке изменить словарь во время итерирования
                        возникает RuntimeError

    - len(dictview)
    - x in dictview -- причём ключ в keys(), пары в items()

                        dict_items([(1, 'a')], ...)

                        'a' in pair # False
                        1 in pair # False
                        (1, 'a') in pair # True

Реализуют интерфейс множеств
Динамически связаны с самим словарём и постоянно отображают изменения в нём

Когда мы итерируем словарь, то у словаря вызывается метод keys()
и итерация происходит по ключам
т.е. методы keys(), values(), items() возвращают итерабельные объекты


Кароче, если в кратце об объектах представления словаря

help(dict(a=1).items()) # values() keys()
print(*dir(dict(a=1).items()), sep='\n')
print(type(dict(a=1).values())) # items() keys()

1) объекты представления вызываются методами keys(), values(), items()
2) они динамически зависимы от объекта словаря, от которого их вызвали
3) при этом это отдельный объект в памяти со своим id
   и не удаляется при удалении словаря
4) с ними можно проводить три операции - in, __len__() и __iter__()
5) изменять их нельзя
6) при итерировании объект отображения нельзя изменять словарь,
   иначе будет RuntimeError
7) реализуют интерфейс множества, т.е. можно выполнять операции с объектами представления
   такие операции с множеством
   и так:
        - реализует методы полностью из первой (где True, False)
        - реализует методы полностью из второй (кроме copy())
          но только с альтернативным вызовом с
          помощью знаков & | - ^ а не с помощью методов
        - НЕ реализует из третьей методы, где меняется сам объект

-- При итерировании объект отображения нельзя изменять словарь,
   иначе будет RuntimeError
    d = {1: 'a', 2: 'b', 3: 'c'}

    dk = d.keys()

    for k in dk:
        d[k ** 2] = str(k) # RuntimeError: dictionary changed size during iteration


-- Если мы удалим словарь, то объекты представления привязанные к нему останутся

    d = {'a':1}
    dv = d.values()
    di = d.items()
    del d # удаляем словарь
    dv
    dict_values([1]) # объекты представления остались
    di
    dict_items([('a', 1)]) # объекты представления остались

-- Мы можем выполнять те-же методы от множеств, что возвращают True или False

    d = {1: 'a', 2: 'b', 3: 'c'}
    dk = d.keys()
    dv = d.values()
    s = {1, 2, 4, 5, 6,}
    print(dk.isdisjoint(s)) # True (если нет общих элементов)
    print(s)
    dk.intersection_update(s)) # AttributeError
    s.update(dk) # {1, 2, 3, 4, 5, 6}
    print(dk & s) # {1, 2} (этот метод из второй категории)
    print(d.values() & dd.values())
    print(d.values().intersection(dd.values())) # а вот так нельзя, хоть это и таже операция  &

-- При итерации словаря python вызывает метод keys()

    d = {1:'a'}
    dv = d.values()
    dk = d.keys()
    dv_it = dv.__iter__() # <dict_valueiterator object at 0x000002B2800F5DB0>
    dk_it = dk.__iter__() # <dict_keyiterator object at 0x000002B280117AE0>
    dict_it  = d.__iter__() # <dict_keyiterator object at 0x000002B28013AC70>









































"""