"""


help(dict)
print(*dir(dict), sep='\n')
print(dict.__doc__)

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
                             default по умолчанию равен 0
    d.update(mapping) -- принимает либо другой словарь или отображение, либо итерабельный объекь,
                         состоящий из итерабельных объектов - пар ключ-значение, либо именованные аргументы
                         Добавляет соответствующие элементы в словарь.


помни, что 1 == 1.0
поэтому лучше не использовать float в качестве ключей


Единственным встроенным отображением является тип данных dict, но
мы имеем также другие виды отображений из встроенной библиотеки collections
(все они наслежуются от dict):

 collections.default
 collections.OrderedDic
 collections.Counter


*** Кароче, если в кратце об объектах представления словаря

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