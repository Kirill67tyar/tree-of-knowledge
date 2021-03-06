"""
-------------------------------------------------- 5 Sequences - Последовательности --------------------------------------------------


-----------------------------------------------------------------------------------------------
Attention please:
    есть отличный package для работы с последовательностями в python - collections.abc
    https://docs.python.org/3/library/collections.abc.html
    https://digitology.tech/docs/python_3/library/collections.abc.html

*** Коллекции в python делсятся на три группы:

1) последовательности
2) множества (set)
3) отображения (dict)


*** Последовтельности в python обязана иметь __getitem__(item) и __len__()
Не обязательно, но желательно чтобы имели метод __iter__()

все встроенные последовательности в python имеют метод __iter__():

    ls = [list, tuple, str, range, bytes,]

    for seq in ls:
        print(hasattr(seq, '__iter__')) # True x 5

*** К встроенным типам последовательнсти относятся
- list
- tuple
- range
- str
- bytes

*** Ощие операции для последовательностей:
Где:
s - sequence
x - element
i - index

 - x in s, x not in s - отвечает за эту операцию метод __contains__()
 - s + t - отвечает за эту операцию метод __add__()
 - s * n, n * s - конкатенация n неполных копий последовательности s
 - s[i]              -- в обоих случая работает __getitem__(item)
 - s[i:j], s[i:j:k]  _/
 - len(s)
 - min(s)
 - max(s)
 - sum(s)   -- если последовательность содержит не числа, то выкинет TypeError
 - s.index(x, i,j) -- если передать туда элемент, которого нет в последости то выкинет ValueError
 - s.count(x)


*** Операции с изменяемыми (мутабельными) последовательностями
Где:
s - sequence
x - element
i - index
k - step

 - s[i] = x -- элемент с индексом i заменяется на x. Отвечает метод __setitem__(key, value)
 - s[i: j: k] = t -- элемент с индексом от i до j с шагом k заменяются на t
 - del s[i: j] -- удаление соответствующих элементов из последовательности
 - s.append(x)
 - s.clear() -- удаление всех элементов последовательности
 - s.copy() -- получает неоплную копию последовательности
 - s.count(x)
 - s.extend(another_sequence)
 - s.index(x)
 - s.insert(i, x) -- не заменяет элемент, а вклинивает его, все остальные элементы двигаются в право
 - s.pop(), s.pop(i) -- не просто удаляет элемент из списка как del, но ещё и возвращает его
 - s.remove(x) -- удаляет первое вхождение данного элемента x. Выкидывает ValueError если элемента нет
 - s.reverse()
 - s.sort()

*** list
help(list)
print(*dir(list), sep='\n')

Список в Python хранит не сами значения а ссылки на них,
список адресов в памяти этих объектов

Любой список - это список чисел (id), на нижнем уровне, с точки зрения самого интепретатора,
где числа - это адреса в памяти

Единственная изменяемая встроенная последовательность (не встроенных - полно)

source for list comprehension:
    https://habr.com/ru/post/320288/

*** tuple
Кортежи - это неизменяемые последовательности, обычно используемые, чтобы хранить разнотипные данные.
Представлены классом tuple


*** range
Не хранит значения (кроме аргументов), а вычисляет его по формуле:

    r[i] = start + step * i, где i >= 0 и r[i]< stop для step > 0 или r[i] > stop для step < 0

Поддерживают все общие последовательности операции, кроме конкатенации и повторения

НЕ является итератором. Но итерируемым объектом.

    hasattr(filter, '__next__') # True

    hasattr(range, '__next__') # False

    hasattr(range, '__iter__') # True


Используются чаще всего с блоком цикла for, для итерирования


*** сравнение последовательностей

две последовательности равны, если они имеют одинаковый тип, равную длину
и соответствующие элементы обоих последовательностей равны

Сравнение последовательностей происходит по строго определённым правилам:
Важно! это не сравнение < или >, а сравнение == будет True или False

Но тут такой момент немаловажный. Такое алгоритм сравнения происходит,
только если сравниваются два списка, или список с чем либо
если сравниваются хешированные объекты, то будет сравниваться их хеш-значение

Что проверяется поэтапно. Каждый пункт проверяется, если предыдущий True (кроме первого):

    1) то что их типы данных должны быть одинаковыми.

        (1,2,3,) == [1,2,3,] # False
        [1,2,3,] == [1,2,3,] # True

    2) далее проверка на длину

        list(range(10)) == list(range(5)) # False
        tuple(range(5)) == tuple(range(5)) # True

    3) проверяется каждый элемент этой последовательности попарно (1й с 1м, 2й с 2м)

        (True, True, None) == (True, True, False) # False
        ['a', 'c', 'b',] == ['a', 'b', 'c',] # False
        ['a', 'b', 'c',] == ['a', 'b', 'c',] # True


*** распаковка

Про распаковку запомни:

    Правильно:
    a, *b = range(10)
    a, *b, c = range(10)
    *a, b = range(10)

    Неправильно:
    *a = range(10)
-----------------------------------------------------------------------------------------------

Attention please:
    есть отличный package для работы с последовательностями в python - collections.abc
    https://docs.python.org/3/library/collections.abc.html
    https://digitology.tech/docs/python_3/library/collections.abc.html


контейнер (коллекция) - объекты, которые в себе инкапсулируют множество других объектов

Коллекции в python делсятся на три группы:

1) последовательности
1) множества (set)
1) отображения


Последовательность в Python - итерабельный объект,
который поддерживает эффективный доступ к элементам с использованием
целочисленных индексов через специальный метод __getitem__()
и поддерживает метод __len__(), который возвращает длину последовательности

К встроенным типам последовательнсти относятся
- list
- tuple
- range
- str
- bytes

Последовательности также опционально могут реализовывать метода
count(), index(), __contains__() и __reversed__() и другие


***** __getitem__() и __len__()

__getitem__() и __len__() - два обязательных метода для последовательности

__getitem__(item) - реализован для индекса (возвращает индекс)

    ls = [4,23,2,1,2]
    ls.__getitem__(-1) # 2

__len__() - возвращает длину последовательности
есть функция len(), которая вызывает метод __len__()

    ls.__len__() # 5

для __getitem__(self, item) если этод метод реализован в последовательности
значние item должно быть целочисленным и называться индексом
а так __getitem__() реализован и для ключей тоже

В случае получения срезов тоже используется метод __getitem__(item)
Есть такая built-in функция как slice()

    slice(3) # slice(None, 3, None)
    slice(1, 13) # slice(1, 13, None)
    print(*dir(slice), sep='\n')

То получение среза получается так:

    ls.__getitem__(slice(2, 4)) # [2, 1]
    ls[2:4] # [2, 1]



__iter__() - очень желательный, но не обязательный метод для последовательности
дело в том, что для итерации достаточно и __getitem__ но он проводит итерацию не эффективно

И тем не мене все встроенные последовательности в python имеют метод __iter__:

    ls = [list, tuple, str, range, bytes,]

    for seq in ls:
        print(hasattr(seq, '__iter__')) # True x 5


***** Операции которые являются общими для последовательностей:
Где:
s - sequence
x - element
i - index

 - x in s, x not in s - отвечает за эту операцию метод __contains__()

    [1,3,5,2].__contains__(3) # True
    [1,3,5,2].__contains__(23) # False

 - s + t - отвечает за эту операцию метод __add__()

    print((1,2,3,).__add__((4,5,6,)))

 - s * n, n * s - конкатенация n неполных копий последовательности s

    (1,2,) * 5
    12 * '-'

 - s[i]              -- в обоих случая работает __getitem__(item)
 - s[i:j], s[i:j:k]  _/
 - len(s)
 - min(s)
 - max(s)
 - sum(s)   -- если последовательность содержит не числа, то выкинет TypeError
 - s.index(x, i,j) -- если передать туда элемент, которого нет в последости то выкинет ValueError
 - s.count(x)


***** Операции с изменяемыми (мутабельными) последовательностями

Где:
s - sequence
x - element
i - index
k - step

 - s[i] = x -- элемент с индексом i заменяется на x. Отвечает метод __setitem__(key, value)

    ls[i] = 'elem'
    ls.__setitem__(i, 'elem')

 - s[i: j: k] = t -- элемент с индексом от i до j с шагом k заменяются на t

    ls = [5]
    ls[:4] = range(4)
    ls # [0, 1, 2, 3, 5,]

 - del s[i: j] -- удаление соответствующих элементов из последовательности
 - s.append()
 - s.clear() -- удаление всех элементов последовательности
 - s.copy() -- получает неоплную копию последовательности

    ls # [4, 23, 2, 1, 2]
    lss = ls
    print(id(ls)) # 2309983085824
    print(id(lss)) # 2309983085824
    lss is ls # True

    lls = ls.copy()
    print(id(lls)) # 2309983390208
    lss is lls # False


 - s.count(x)
 - s.extend(another_sequence)
 - s.index(x)
 - s.insert(i, x) -- не заменяет элемент, а вклинивает его, все остальные элементы двигаются в право

    интересный момент:
    ls = [1, 2, 3, 4,]
    ls.insert(99999, 5)
    ls # [1, 2, 3, 4, 5,]
    ls.insert(-99999, 6)
    ls # [6, 1, 2, 3, 4, 5,]

 - s.pop(), s.pop(i) -- не просто удаляет элемент из списка как del, но ещё и возвращает его
 - s.remove(x) -- удаляет первое вхождение данного элемента x. Выкидывает ValueError если элемента нет
 - s.reverse()
 - s.sort()

***** списки list

Списки - это изменяемые последовательности, обычно используемые для хранения однотипных данных.
хотя Python не запрещает хранить в них данные разных типов.
То что списки в Python могут хранить объекты разных типов -
побочный продукт динамической типизации

Предствлены классом list

Список в python, в памяти хранит числа (id), которые являются адресами
объектов в памяти
Иначе говоря список в Python хранит не сами значения а ссылки на них,
список адресов в памяти этих объектов

Любой список - это список чисел (id), на нижнем уровне, с точки зрения самого интепретатора,
где числа - это адреса в памяти

создаются или так:

    ls = [1,2,3,]

или так:

    ls = list([1,2,3,])
    ls = list((1,2,3,))
    ls = list('abc')

или даже так:

    ls = list({'a': 1, 'b': 2,}) # ['a', 'b',]

list comprehension:

    ls = [x % 2 for x in range(10)]

source for list comprehension:
    https://habr.com/ru/post/320288/

***** полная копия (deep copy) и непоная копия (shallow copy) (shallow - мелкий)

Что есть не полная копия?

полная копия может часто называется рекурсивной копией

Любой список - это список чисел (id), на нижнем уровне, с точки зрения самого интепретатора,
где числа - это адреса в памяти

Смотри:

    1) создаём копию списка
    ls = [[1,2,],3]
    lss = ls.copy()

    2) id этих списков разные
    print(id(ls)) # 1698968267200
    print(id(lss)) # 1698968266816
    print('\n', '*' * 50, '\n')

    3) но адреса в памяти тех объектов, что там хранятся - одинаковые
    for i in ls: print(id(i)) # 1698968267200
    print('\n', '*' * 50, '\n') # 1698968266816
    for i in lss: print(id(i))


А здесь пример как мы изменили не сам тапл,
а один элемент тапла:

    ls = [1,2,]
    t = (ls, 3)
    ls.extend(range(3, 10))
    print(tt[0]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(t) # ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

Пример неполной копии (shallow copy):

    1) функция которая принтит матрицу
    def print_matrix(matrix):
        for row in matrix:
            print(' '.join(str(x) for x in row))
        return '\n'

    2) создаём матрицу с помощью неполной копии
    matrix = [[0,] * 5] * 5 # [[0,0,0,0,0,], [0,0,0,0,0,], ...]

    print(print_matrix(matrix)) # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
    3) и изменяя один объект изменяем все
    matrix[1][-1] = 1

    print(print_matrix(matrix)) # 0 0 0 0 1
                                # 0 0 0 0 1
                                # 0 0 0 0 1
                                # 0 0 0 0 1
                                # 0 0 0 0 1

    4) как видим с помощью неглубокой копии создаются одни и те же объекты
    это всё один список в памяти
    for i in matrix:
        print(id(i))

    # 1933963847808
    # 1933963847808
    # 1933963847808
    # 1933963847808
    # 1933963847808

Таким умножением

    matrix = [[0,] * 5] * 5

мы получиди список, который пять раз ссылается на один и тот же список
Как же создать матрицу тогда?
с помощью спискового включения:

    matrix = [[0,] * 5 for i in range(5)]

    print(print_matrix(matrix)) # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0

    matrix[1][-1] = 1

    print(print_matrix(matrix)) # 0 0 0 0 0
                                # 0 0 0 0 1
                                # 0 0 0 0 0
                                # 0 0 0 0 0
                                # 0 0 0 0 0
    for i in matrix:
        print(id(i))

    # 2195144215232
    # 2195144206272
    # 2195144206656
    # 2195147427584
    # 2195143870848


Теперь всё работает нормально.
Это скорее так, лайфхак

а можно использовать функцию deepcopy из модуля copy

***** кортежи tuple

Кортежи - это неизменяемые последовательности, обычно используемые, чтобы хранить разнотипные данные.
Представлены классом tuple

Поддерживают вcе общие для последовательностей операции.

такого синтакиса как включение кортежей в python нет
синтаксис включения кортежей забит за генераторами

и выражения comprehension тоже нет, это генераторы



***** распаковка

Про распаковку запомни:

    Правильно:
    a, *b = range(10)
    a, *b, c = range(10)
    *a, b = range(10)

    Неправильно:
    *a = range(10)


Прикольная функция:

    def mean(first, *args):
        return (first + sum(args)) / (len(args) + 1)

    print(mean(5,5,5))
    print(mean(5,5,11))


***** диапазоны range

Диапазоны - неизменяемые последовательности чисел, которые задаются началом, концом и шагом
Представлены классом range

Начало по умолчанию равно 0, шаг единице. Если задать нулевой шаг, будет выброшено
исключение ValueError.

Не хранит значения (кроме аргументов), а вычисляет его по формуле:

    r[i] = start + step * i, где i >= 0 и r[i]< stop для step > 0 или r[i] > stop для step < 0

Поддерживают все общие последовательности операции, кроме конкатенации и повторения

НЕ является итератором. Но итерируемым объектом.

    hasattr(filter, '__next__') # True

    hasattr(range, '__next__') # False

    hasattr(range, '__iter__') # True


Используются чаще всего с блоком цикла for, для итерирования


***** строки str

sources:
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

Строки - неизменяемые последовательности кодов симоволов (в Python 3 кодировка Unicode)
Представлены классом str

Если перед начальной ковычкой стоит префикс r то большинство escape последовательностей игнорируются
Поддерживают все общие для последовательностей операции, а также реализует огромное
кол-во собственных методов

Функции, которые позволяют работать с символами на более низком уровне:

 - ord(char) -- возвращает код символа char
 - chr(code) -- возвращает символ с кодом code

Строки - неизменяемый тип данных,
все строки которые мы модифицируем создают новый объект в памяти

***** Обратные/Экранизированные последовательности


Последовательность	Назначение
\newline	Если после символа "\" сразу нажать клавишу Enter то это позволит продолжать запись с новой строки.
\\	        Позволяет записать символ обратного слеша.
\'	        Позволяет записать один символ апострофа.
\"	        Позволяет записать один символ кавычки.
\a	        Гудок встроенного в систему динамика.
\b	        Backspace, он же возврат, он же "пробел назад" – удаляет один символ перед курсором.
\f	        Разрыв страницы.
\n	        Перенос строки (новая строка).
\r	        Возврат курсора в начало строки.
\t	        Горизонтальный отступ слева от начала строки (горизонтальная табуляция).
\v	        Вертикальный отступ сверху (вертикальная табуляция).
\xhh	    Шестнадцатеричный код символа (две шестнадцатеричные цифры hh).
\ooo	    Восьмеричный код символа (три восьмеричные цифры ooo).
\0	        Символ Null.
\N{id}	    ID (идентификатор) символа в базе данных Юникода, или, проще говоря, его название в таблице Юникода.
\uhhhh	    Шестнадцатеричный код 16-битного символа Юникода (символ кодируемый двумя байтами).
\Uhhhhhhhh	Шестнадцатеричный код 32-битного символа Юникода (символ кодируемый четырьмя байтами).
\other	    Под other понимается любая другая последовательность символов. Не является экранированной
            последовательностью (остается без изменений с сохранением в строке символа "\").




***** Сравнение последовательностей

две последовательности равны, если они имеют одинаковый тип, равную длину
и соответствующие элементы обоих последовательностей равны

Последовательности одинаковых типов можно сравнивать. Сравнения происходят в
лексиграфическом порядке: последовательность меньшей длины меньше, чем
последовательность большей длины, если же их длины равны, то результат сравнения равен
результату сравнения первых отличающихся элементов.

Сравнение последовательностей происходит по строго определённым правилам:
Важно! это не сравнение < или >, а сравнение == будет True или False

Что проверяется поэтапно. Каждый пункт проверяется, если предыдущий True (кроме первого):

    1) то что их типы данных должны быть одинаковыми.

        (1,2,3,) == [1,2,3,] # False
        [1,2,3,] == [1,2,3,] # True

    2) далее проверка на длину

        list(range(10)) == list(range(5)) # False
        tuple(range(5)) == tuple(range(5)) # True

    3) проверяется каждый элемент этой последовательности попарно (1й с 1м, 2й с 2м)

        (True, True, None) == (True, True, False) # False
        ['a', 'c', 'b',] == ['a', 'b', 'c',] # False
        ['a', 'b', 'c',] == ['a', 'b', 'c',] # True



Сравнение последовательностей на < или >:

    Видео прерывается

Sources:
    https://docs-python.ru/tutorial/podrobno-uslovijah-sravnenijah-python/sravnenie-posledovatelnostej-drugih-tipov/
    https://pythonist.ru/sravnenie-strok-v-python/#:~:text=%D0%A1%D1%82%D1%80%D0%BE%D0%BA%D0%B8%20%D0%B2%20Python%20%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%20%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D0%B2%D0%B0%D1%82%D1%8C,%D1%81%D1%80%D0%B0%D0%B2%D0%BD%D0%B8%D0%B2%D0%B0%D1%8E%D1%82%D1%81%D1%8F%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8B%20%D0%BD%D0%B0%20%D1%81%D0%BB%D0%B5%D0%B4%D1%83%D1%8E%D1%89%D0%B5%D0%B9%20%D0%BF%D0%BE%D0%B7%D0%B8%D1%86%D0%B8%D0%B8.










"""
