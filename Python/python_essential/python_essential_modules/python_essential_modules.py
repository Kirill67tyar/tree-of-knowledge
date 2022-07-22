"""
-------------------------------------------------- Модули --------------------------------------------------

-------------------------------------------------------------------------------------------------------

sources:
    https://docs.python.org/3/library/importlib.html
    https://python-scripts.com/importlib

библиотеки для работы с испортом модулей:
    https://docs.python.org/3/library/modules.html
    https://docs.python.org/3/library/test.html#module-test.support.import_helper

----- Алгоритм импорта модулей
1) любой файл с кодом Python и расширением .py является модулем
2) папка с файлом __init__.py является пакетом
3) пакет - это разновидность модуля
   любой пакет является модулем, но не каждый модуль является пакетом
4) т.к. пакет это модуль, то пакеты могут содержать не только модули (файлы с .py)
   но и другие пакеты
5) у модуля, запущенного как скрипт глобальная переменная __name__ равна "__main__"
6) при импорте модуля глобальная переменная __name__ инициализируется в имя модуля
7) при импортирвании модуля выполняется весь код, который там есть.
   для этого и нужна конструкция if __name__ == '__main__'
8) В случае импорта через * импортируются все имена, кроме тех, что начинаются с _
   если правда эти переменные (с _) не определены в файле __init__.py пакета
   тогда они тоже импортируются
9) любой модуль за сессию работы интепретатора импортируется только один раз
   если не перезагрузим в функции reload() который есть в importlib
10) sys.path - список путей, каталогов, в которых Python будет искать модули, при импорте
    По умолчанию sys.path состоит из директории с запускаемым скриптом, содержимного
    переменной окружения PYTHONPATH и стандартного расположения модулей,
    специфического для конкретной платформы и интерпретатора.
    Смотри дополнительно про sys.path в файле про библиотеку
11) чтобы загрузить модуль Python сначало ищет бинарный файл с байт-кодом этого модуля в
    папке __pycache__ рядом с модулем. смотри алгоритм ниже, в несписка в *** __pycache__
12) после того как модуль загружен, в памяти интерпретатора появляется объект, который
    и представляет этот модуль, а его атрибуты - это любые глобальные имена, которые были в этом модуле
13) этот объект имеет точно такое же имя, как и сам модуль
14) from math import ceil as c
    тоже самое что
    from math import ceil
    c = ceil
    del ceil
14) но при это m.__name__ == 'math' # True
    потому что имя модуля, и имя переменной, по которой этот модуль доступен - разные вещи





*** __pycache__
Если модуля нет в оперативной памяти, то Python находит его, и смотрит рядом с ним файл __pycache__
в __pycache__ хранятся файлы байт-кода модулей (есть и в django, просто в PyCharm не виден)
с расширунием .pyc и версией интерпретатора.
Далее:
    - Python сверяет дату измениния модуля и соответствуюего ему файла байт-кода
    - если модуль был изменён раньше файла байт-кода, то будет загружен
        готовый байт-код, который описывает импортируемый модуль на гораздо более низком уровне
        (является бинарным файлом)
    - если модуль был изменён позже, или файла байт-кода вообще нет, то:
        1) будет прочитан файл исходного кода
        2) произведён его синтаксический анализ
        3) будет для него сгенерирован байт-код для виртуальной машины python
        4) записан в этот файл
        5) и потом уже загружен


!!!                                                                             !!!
    Low Coupling and High Cohesion - слабой связанностью и сильной связанностью
    Сильная связанность кода внутри модуля, и слабая между модулями
!!!                                                                             !!!

Low Coupling and High Cohesion - слабой связанностью и сильной связанностью
    Код который находится внутри модулей, (функций, классов) должен быть как можно более тесно связан
    а связи между самими модулями должны быть как можно менее тесными

sources:
    https://medium.com/german-gorelkin/low-coupling-high-cohesion-d36369fb1be9#:~:text=Low%20Coupling%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%2C%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9,%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%D0%BC%D0%B8%20%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B0%D0%BB%D0%B0%D1%81%D1%8C%20%D0%BD%D0%B8%D0%B7%D0%BA%D0%BE%D0%B9.

----- Пакеты

1) модули могут объединяться в пакеты. Пакеты служат как пространство имён
   для модулей и способ их структурирования.
2) любой пакет является модулем, но не каждый модуль является пакетом.
3) для того, чтобы каталог был пакетом, в нём должен находиться файл __init__.py
4) файл __init__.py автоматически выполняется при импортировании соответствующего модуля
   и может содержать определённые действия для инициализации или быть пустым.
   Точно также, как при импортировании модуля как файл, выполняется весь его код
   точно также при импортировании пакета выполняется весь код в файле __init__.py
   код в __init__.py выполняется в первую очередь при импорте
5) для того, чтобы можно было импортировать все имена пакета
   (from package.subpackage import *), пакет должен описывать
   список __all__ в файле __init__.py, который содержит имена подпакетов и модулей.
6) при использовании оператора from package import item, item
   может быть пакетом, модулем или любым именем, описанным в пакете
7) при использовании оператора import package.item, item должен быть модулем или пакетом.
8) ключевая разница между  import ...  и   from ... import ...
   в том, что в случае просто import можно импортировать только модули и пакеты
   а в случае связки слов from ... import ... можно импортировать
   и модели и пакеты и любые переменные в модуле
   гдавное правильно выстроить иерархию модулей

Варинаты импорта пакетов:

    import package.module
    import package.subpackage.module
    from package import module
    from package import item
    from package.subpackage import module, item
    from module import *


*** относительное импортирования

Кроме абсолютных, существуют также относительные импорты:
точка указывет на текущтй пакет, две точки на родительский

    from . import name # импортировать из текущего пакета
    from .. import name # импортировать из родительского пакета

Эти же символы могут быть использованы сразу перед именем пакета
или модуля и влиять на то, где интерпретатор будет его искать.

    from .package import name # импортировать из текущего пакета который лежит в текущем пакете
    from ..package import name # импортировать пакет из родительского пакета


-------------------------------------------------------------------------------------------------------



Модуль - функционально законченный фрагмент программы, оформленный в виде отдельного файла
с исходным кодом или поименованной непрерывной её части. Модули позволяют разбивать сложные задачи
на более мелкие в сооветствии с принциплм модульности.

Обычно проектируются таким образом, чтобы предоставлять удобную для многократного использования
функциональность (интерфейс) в виде набора функций, классов, констант

Файл, который содержит исходный код на языке Python, является модулем

Чисто с технической точки зрения - ООП это продолжение модульного программирования
И классы это как модули, которые мы может инстацировать несколько раз

Модули можно рассматривать как классы singleton (класс, у которого может быть только один экземпляр)

Функции фрагменты программы, которые можно несколько раз использовать
Классы тоже описывают какой-то код для многократного использования,
И модули также - отдельный фрагмент кода, который можно переиспользовать

В жизни:
    Функции позволяют разбить на отдельные сущности процесс решения задач

    Классы помогают определить и выделить в отдельные категории, и сущности
    объекты из реального мира. Таксаномия так сказать. В Python создать тип данных
    со своим поведением.

    А модули помогают выделить в одно целое (системы) целые подсистемы
    целый набор функций и классов, которые мы можем определять по каким-то признакам
    которые все вместе будут выполнять отдельную функционально законченную задачу
    нужную для приложения, проекта и т.д.

и классы и функции иногда тоже называют модулями. ну так, в переносном смысле
Есть даже модульное тестирование - unittest.
Потому что и модуль и класс и функция это многозначные слова
очень часто модуль означает любые функционально законченные элементы программы
любые фрагменты кода, которые можно использовать

Потому что всё является системой, которая состоит из систем, и является сама часть какой-либо системы
Но любое деление на системы, арбитрарно. Любая таксаномия арбитрарна

И для классов и для функций и для модулей можно вывести общий принцип:

!!!                                                                             !!!
    Low Coupling and High Cohesion - слабой связанностью и сильной связанностью
    Сильная связанность кода внутри модуля, и слабая между модулями
!!!                                                                             !!!

Low Coupling and High Cohesion - слабой связанностью и сильной связанностью
    Код который находится внутри них должен быть как можно более тесно связан
    а связи между самими модулями должны быть как можно менее тесными

sources:
    https://medium.com/german-gorelkin/low-coupling-high-cohesion-d36369fb1be9#:~:text=Low%20Coupling%20%E2%80%94%20%D1%8D%D1%82%D0%BE%20%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%2C%20%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B9,%D1%81%D0%B2%D1%8F%D0%B7%D0%B0%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%BC%D0%B5%D0%B6%D0%B4%D1%83%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0%D0%BC%D0%B8%20%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%B0%D0%BB%D0%B0%D1%81%D1%8C%20%D0%BD%D0%B8%D0%B7%D0%BA%D0%BE%D0%B9.
Т.е. отдельные модули должны быть максимально независимы друг от друга

Такой код легко тестировать и использовать.

***** __pycache__

Любой модуль за сессию работы интепретатора импортируется только один раз
если не перезагрузим в функции reload() который есть в importlib

Если модуль, который мы запрашиваем был уже импортирован,
то python возьмёт из памяти соответствующий ему объект загруженного модуля
который уже находится в памяти интерпретатора

Если его нет в памяти (модуль не был загружен, или импортирован)
Python найдёт его, посмотрит есть ли рядом с этим модулем папка __pycache__
и там файл с таким же названием но разрешением .pyc и укзанаием версии интерпретатора
(в PyCharm этот файл даже не виден)
Если есть соответствующий ему файл байт-кода, то проверяется дата последнего изменения
Если байткод был создан позже чем изменён файл исходного кода,
то файл исходного кода даже не будет трогаться
Сразу же Python загрузит в память байт-код из этого скомпилированного файла

Если файла байт-кода (__pycache__) нет вообще, или файл исходного кода
(файл где этот модуль описывался )был изменён позже чем он
в таком случае:
- будет прочитан файл исходного кода
- произведён его синтаксический анализ
- будет для него сгенерирован байт-код для виртуальной машины python
- записан в этот файл
- и потом уже загружен

Если исходник не был изменён - загрузка будет происходить намного быстрее,
не будет выполняться синтаксический анализ кода, не будет выполняться его компиляция в байт-код
сразу будет загружен готовый байт-код, который описывает импортируемый модуль на гораздо более низком уровне

При импорте python сначала ищет модуль в built-in (встроенных в язык)


__pycache__ - Файл скомпилированного байт кода


***** после загрузки модуля

Далее в памяти интерпретатора создаётся структура, объект, который представляет модуль в памяти
Это обычный объект, но его атрибуты - это любые глобальные имена, которые были в этом модуле




Когда мы импортируем модуль Python

1) ищет модуль в built-in (встроенных в язык)




***** импортирование имён из модуля

При импорте отдельных переменных из модуля сам модуль импортируется
но вместо какой-то переменной привязать сам объект модуля,
к отдельным перенменным привязываются функции, классы и т.д.

Но в то же время:

    from fibonacci import nth_fibonacci as nth

    print(nth.__name__) # nth_fibonacci


В случае импорта через * импортируются все имена, кроме тех, что начинаются с _
(это касается функций, классов и т.д.)

импорт и переименование по именам имеет такую логику:

    import fibonacci
    nth = fibonacci.nth_fibonacci
    del fibonacci

    number = int(input('Enter number for fibonacci: '))
    print(f'Result: {nth(number)}')
    print(nth.__name__)


***** sys и os

Есть такие модули, которые являются встроенными в сам интерпретатор

Модуль sys относится к таким, модулям.
sys содержит разные системные переменные

Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.

Короче это такой модуль, который позволяет работать с python по полной
с объектами в памяти, с модулями. Вообще с операционной системой

sources:
    https://pythonworld.ru/moduli/modul-sys.html

При помощи sys можно:
 - узнать версию интерпретатора
 - узнать путь к интерпретатору Python - sys.executable
 - возвращает количество ссылок на объект. Аргумент функции getrefcount - еще одна ссылка на объект
   sys.getrefcount(object)
 - узнать размер объекта в байтах
   sys.getsizeof(object[, default])

    import sys
    t = 1,2,3,
    ls = [1,2,3,]
    sys.getsizeof(ls) # 120
    sys.getsizeof(t) # 64

 - изменить максимальную глубину рекурсии с помощью sys.getrecursionlimit() и sys.setrecursionlimit()

    import sys
    sys.getrecursionlimit() # 1000

 - есть переменная argv - список аргументов всей командной строки
   в качестве первого элемента этого списка - имя скрипта,
   все остальные элементы - аргументы скрипта


   Если из консоли:

   sys.argv # [
            #   'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2.2\\plugins\\python-ce\\helpers\\pydev\\pydevconsole.py',
            #   '--mode=client',
            #   '--port=49569'
            # ]

   обычно используется для написания консольных утилит
   попробуй набрать в консоли
   # kiril@LAPTOP-1D1S7LOO C:\....python_essential\python_essential_modules\some_module$ python args_list.py 12, 3,5,2

   выдаст такое - ['args_list.py', '12,', '3,5,2']

   или
   python args_list.py and True # ['args_list.py', 'and', 'True']


 - узнать все встроенные модули

    import sys
    print(*sys.builtin_module_names, sep='\n')

 - словарь имён загруженных модулей (скорее всего вообще все файлы на компьютере с .py) - sys.modules

    import sys
    from pprint import pprint
    pprint(sys.modules)

 - список sys.path - список директорий и архивов,
   где python ищет модули при импортировани. Можно читатать и изменять
   По умолчанию sys.path состоит из директории с запускаемым скриптом, содержимного
   переменной окружения PYTHONPATH и стандартного расположения модулей,
   специфического для конкретной платформы и интерпретатора.

      print(*sys.path, sep='\n')

   sys.path - список путей, каталогов, в которых Python будет искать модули, при импорте

***** пути поиска модулей или sys.path

При импортировании модулей интерпретатор Python ищет их в директориях и архивах,
список которых доступен для чтения, так и для модификации в виде переменной path
встроенного модуля sys

По умолчанию sys.path состоит из директории с запускаемым скриптом, содержимного
переменной окружения PYTHONPATH и стандартного расположения модулей,
специфического для конкретной платформы и интерпретатора.

Для ускорения загрузки модулей Python кеширует байт-код и производит компиляцию
модуля в таком случае, если исходный код был изменён.
Python сохраняет файлы байт-кода .pyc  в каталоге __pycache__


интерпретатор python ищет по порядку, сначала в первом каталоге
затем во втором и т.д., пока не закончатся все пути в данном списке

Например при виртуальном окружении scraping-service sys.path выдаёт такой результат:

    C:\Users\kiril\Desktop\Job\django_repeat_07\scraping-service\src
    C:\Users\kiril\AppData\Local\Programs\Python\Python39\python39.zip
    C:\Users\kiril\AppData\Local\Programs\Python\Python39\DLLs
    C:\Users\kiril\AppData\Local\Programs\Python\Python39\lib
    C:\Users\kiril\AppData\Local\Programs\Python\Python39
    C:\Users\kiril\Desktop\Job\django_repeat_07\scraping-service\src\venv
    C:\Users\kiril\Desktop\Job\django_repeat_07\scraping-service\src\venv\lib\site-packages

Из чего он будет состоять по умолчанию зависит от операционной системы, конкретной версии интерпретатора
конкретной платформы и т.д.
По умолчанию там находится:
 - каталог, который был текущим на момент запуска интерпретатора
 - содержимое соответствующей системной переменной окружения
 - а также разных стандартных путей расположения модулей, которые являются платформо-специфичными

Кроме того, этот список является изменяемым.
Поэтому его можн использовать, чтобы оптимизировать загрузку модулей в приложение


***** os

Вообще, модуль os предоставляет множество функций для работы с операционной системой,
причём их поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
кроссплатформенный модуль

sources:
    https://docs.python.org/3/library/os.html
    https://pythonworld.ru/moduli/modul-os.html


*** os.path


Ок, если sys.path - список директорий и архивов, где python ищет модули при импортировани,
который можно читать и изменять, то
os.path - модуль, который содержит различные функции по манипулированию с путями в файловой системе
os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.


os.path - кросплатформенная, как и модуль os.
Команды универсальны и на каждой платформе будут работать правильно

os.path.join('a', 'b') # 'a\\b'

Соединяет два объекта обратными слэшами
функция join - соединяет две части пути, разделителем частей пути,
который принят на текущей платформе (если используется | то будет соединять им)


У нас есть папка another_directory в которую мы хотим импортировать
модуль из папки, которая лежит на уровень ниже


    !!!                                                     !!!
        Непонятная ситуация. Загляни в папку exp_with_import
        там я создал в каждой папке по файлу __init__.py и
        всё равно ничего не импортируется.
    !!!                                                     !!!

А так склейка засчёт os.path.join и sys.path - работает отлично
смотри файл practice_from_another_directory.py

 -- os.path.abspath(path) - узнаёт абсолютный путь файла
   можно конечно узнать абсолютный путь файла с помощью атрибута модуля __file__
   но иногда он даёт неверный путь (по каким-то причинам)
   os.path.abspath(path) всегда даст абсолютный путь
   help(os.path.abspath)

        print(os.path.abspath('qwerty')) # C:\Users\kiril\Desktop\...\python_essential_modules\another_directory\qwerty
        print(os.path.abspath(__file__)) # C:\Users\kiril\Desktop\...\python_essential_modules\another_directory\practice_from_another_directory.py

   как мы видим, в аргумент abspath можно не только передавать __file__
   но и строчной аргумент, иначе будет

        TypeError: _getfullpathname: path should be string, bytes or os.PathLike, not dict

 -- os.path.basename(path) обрезает путь,
   и возвращает только имя файла.
   может быть передана в аргумент строка
   (эквивалентно os.path.split(path)[1])
   help(os.path.basename)

        print(os.path.basename(__file__)) # name_of_file_where_you_call_it.py

 -- os.path.dirname(path)
   возвращает путь и обрезает имя файла
   может быть передан в аргумент только файл (или имя файла в формате str)
   help(os.path.dirname)

        print(os.path.dirname(__file__))

   причём работает интересно, он просто КАК БУДТО делает split('\')
   и отсекает последний элемент.
   Поэтому если мы сделаем так

        print(os.path.dirname(os.path.dirname(__file__)))

   мы получим имя родительской директории
   это эквивалентно Path(__file__).parent.parent
   только тип данных у Path будет <class 'pathlib.WindowsPath'>

работа в связке path.dirname, path.join, sys.path, path.abspath:

    current_path = os.path.dirname(os.path.abspath(__file__))
    # поднимаемся на папку выше
    parent_path = os.path.dirname(current_path)
    fibonacci_module = os.path.join(parent_path, 'fibonacci_package')
    sys.path.append(fibonacci_module)

вообще запомни, что

    os.path.dirname(os.path.abspath(__file__))

это такая формула, по построению абсолбтного пути

, а

    SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(SCRIPTS_DIR)

универсальный способ сделать так, чтобы модуль был доступен


 -- os.environ - словарь переменных окружения (изменяемый)

    env = os.environ

    for k in env:
        print(k, ' - ', env[k])

***** Пакеты

Модули могут объединяться в пакеты. Пакеты служат как пространство имён
для модулей и способ их структурирования.

Любой пакет является модулем, но не каждый модуль является пакетом.

Как правило, модули представляются в виде файлов, а пакеты -
каталогов в файловой системе (но не всегда)

Для того, чтобы каталог был пакетом, в нём должен находиться файл __init__.py
Он автоматически выполняется при импортировании соответствующего модуля
и может содержать определённые действия для инициализации или быть пустым.

Точно также, как при импортировании модуля как файл, выполняется весь его код
точно также при импортировании пакета выполняется весь код в файле __init__.py


Варинаты импортов пакетов:

    import package.module
    import package.subpackage.module
    from package import module
    from package import item
    from package.subpackage import module, item
    from module import *


Для того, чтобы можно было импортировать все имна пакета
(from package,subpackage import *), пакет должен описывать
список __all__ в файле __init__.py, который содержит имена подпакетов и модулей.

При использовании оператора from package import item, item
может быть пакетом, модулем или любым именем, описанным в
пакете. При использовании оператора import package.item, item
должен быть модулем или пакетом.

Ключевая разница между  import ...  и   from ... import ...
в том, что в случае просто import можно импортировать только модули и пакеты
а в случае связки слов from ... import ... можно импортировать
и модели и пакеты и любые переменные в модуле
главное правильно выстроить иерархию модулей

*** относительное импортирования

Кроме абсолютных, существуют также относительные импорты:
точка указывет на текущтй пакет, две точки на родительский

    from . import name # импортировать из текущего пакета
    from .. import name # импортировать из родительского пакета

Эти же символы могут быть использованы сразу перед именем пакета
или модуля и влиять на то, где интерпретатор будет его искать.

    from .package import name # импортировать из текущего пакета который лежит в текущем пакете
    from ..package import name # импортировать пакет из родительского пакета


















"""