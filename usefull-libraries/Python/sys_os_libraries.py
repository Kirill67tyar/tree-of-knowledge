"""
sources:
        sys:
            https://pythonworld.ru/moduli/modul-sys.html
            https://docs.python.org/3/library/sys.html
        os:
            https://docs.python.org/3/library/os.html
            https://pythonworld.ru/moduli/modul-os.html

Эти модули отлично работают в связке

os и os.path - связаны с операционной системой ПК, и с путями операционной системы ПК
можно узнать, является ли путь указанной директорией или папкой,
существует ли он вообще, а таке как обходить папки рекурсивно
------------------------------------- sys ----------------------------------------------------------

Модуль sys обеспечивает доступ к некоторым переменным и функциям, взаимодействующим с интерпретатором python.

Короче это такой модуль, который позволяет работать с python по полной
с объектами в памяти, с модулями. Вообще с операционной системой


При помощи sys можно:
 -- узнать версию интерпретатора
 -- sys.implementation полная информация об интерпретаторе
 -- sys.prefix - папка установки интерпретатора python.
 -- узнать путь к интерпретатору Python sys.executable
 -- возвращает количество ссылок на объект. Аргумент функции getrefcount - еще одна ссылка на объект
    sys.getrefcount(object)
 -- узнать размер объекта в байтах
    sys.getsizeof(object[, default])
 -- изменить максимальную глубину рекурсии с помощью sys.getrecursionlimit() и sys.setrecursionlimit()
 -- есть переменная argv - список аргументов всей командной строки
    в качестве первого элемента этого списка - имя скрипта,
    все остальные элементы - аргументы скрипта


   Если из консоли:

   sys.argv # [
            #   'C:\\\\Program Files\\\\JetBrains\\\\PyCharm Community Edition 2021.2.2\\\\plugins\\\\python-ce\\\\helpers\\\\pydev\\\\pydevconsole.py',
            #   '--mode=client',
            #   '--port=49569'
            # ]

   обычно используется для написания консольных утилит
   попробуй набрать в консоли

 -- sys.builtin_module_names - все встроенные модули

    import sys
    print(*sys.builtin_module_names, sep='\\n')

 -- sys.modules словарь имен загруженных модулей (скорее всего вообзе все файлы на компьютере с .py)

    import sys
    from pprint import pprint
    pprint(sys.modules)

 -- sys.stderr - стандартный поток ошибок

    pp(dir(sys.stderr))
    pp(type(sys.stderr))
    pp(sys.stderr.__class__.mro())
    help(sys.stderr)


 -- sys.path - список путей, каталогов, в которых Python будет искать модули, при импорте
    По умолчанию sys.path состоит из директории с запускаемым скриптом, содержимного
    переменной окружения PYTHONPATH и стандартного расположения модулей,
    специфического для конкретной платформы и интерпретатора.

      import sys
      print(*sys.path, sep='\\n')


*** sys.path
При импортировании модулей интерпретатор Python ищет их в директориях и архивах,
список которых доступен для чтения, так и для модификации в виде переменной path
встроенного модуля sys

По умолчанию sys.path состоит из директории с запускаемым скриптом, содержимного
переменной окружения PYTHONPATH и стандартного расположения модулей,
специфического для конкретной платформы и интерпретатора.

Для ускорения загрузки модулей Python куширует байт-код и производит компиляцию
модуля в таком случае, если исходный код был изменён.
Python сохраняет файлы байт-кода .pyc  в каталоге __pycache__


интерпретатор python ищет по порялку, сначала в первом каталоге
затем во втором и т.д., пока не закончатся все пути в данном списке

Например при виртуальном окружении scraping-service sys.path выдаёт такой результат:

    C:\\Users\\kiril\\Desktop\\Job\\django_repeat_07\\scraping-service\\src
    C:\\Users\\kiril\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip
    C:\\Users\\kiril\\AppData\\Local\\Programs\\Python\\Python39\\DLLs
    C:\\Users\\kiril\\AppData\\Local\\Programs\\Python\\Python39\\lib
    C:\\Users\\kiril\\AppData\\Local\\Programs\\Python\\Python39
    C:\\Users\\kiril\\Desktop\\Job\\django_repeat_07\\scraping-service\\src\\venv
    C:\\Users\\kiril\\Desktop\\Job\\django_repeat_07\\scraping-service\\src\\venv\\lib\\site-packages

По умолчанию там находится:
 - каталог, который был текущим на момент запуска интерпретатора
 - содержимое соответствующей системной переменной окружения
 - а также разных стандартных путей расположения модулей, которые являются платформо-специфичными

os.path.join('a', 'b') # 'a\\\\b'

Соединяет два объекта обратными слэшами
функция join - соединяет две части пути, разделителем частей пути,
который принят на текущей платформе (если используется | то будет соединять им)

------------------------------------- os ----------------------------------------------------------

Вообще, модуль os предоставляет множество функций для работы с операционной системой,
причём их поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.

*** os.path (это модуль)
os.path - модуль, который содержит различные функции по манипулированию с путями в файловой системе
os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.

os.path - кросплатформенная, как и модуль os.
Команды универсальны и на каждой платформе будут работать правильно

 -- os.path.join('a', 'b') # 'a\\\\b'

    Соединяет два объекта обратными слэшами
    функция join - соединяет две части пути, разделителем частей пути,
    который принят на текущей платформе (если используется | то будет соединять им)


 -- os.path.abspath(path) - узнаёт абсолютный путь файла
   можно конечно узнать абсолютный путь файла с помощью атрибута модуля __file__
   но иногда он даёт неверный путь (по каким-то причинам)
   os.path.abspath(path) всегда даст абсолютный путь
   help(os.path.abspath)

        print(os.path.abspath('qwerty')) # C:\\Users\\kiril\\Desktop\\...\\python_essential_modules\\another_directory\\qwerty
        print(os.path.abspath(__file__)) # C:\\Users\\kiril\\Desktop\\...\\python_essential_modules\\another_directory\\practice_from_another_directory.py

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
   может быть передан в аргумент только файл
   help(os.path.dirname)

        print(os.path.dirname(__file__))

   причём работает интересно, он просто КАК БУДТО делает split('\\')
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

универсальный способ сделать так, чтобы модуль был дотпен

"""


from pprint import pprint as pp
import sys, os


# # # ----------------------------------------
# # работа в связке path.dirname, path.join, sys.path, path.abspath:
# current_path = os.path.dirname(os.path.abspath(__file__))
# # поднимаемся на папку выше
# parent_path = os.path.dirname(current_path)
# fibonacci_module = os.path.join(parent_path, 'fibonacci_package')
# sys.path.append(fibonacci_module)
#
# # ----------------------------------------
# # формула, по построению абсолбтного пути файла, где запущен скрипт
# os.path.dirname(os.path.abspath(__file__))
#
# # ----------------------------------------
# # универсальный способ сделать так, чтобы модуль был доступен
# SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append(SCRIPTS_DIR)
#
#
# # пример из файла run_scraping.py
# proj = os.path.dirname(os.path.abspath('manage.py'))    # устанавливаем абсолютный путь для manage.py
#
# sys.path.append(proj)# тут мы добавляем путь в системные переменные путей
# # как мы видим мы устанавливаем абсолютный путь для файла manage.py,
# # находясь в этот момент в файле run_scraping.py
# # ----------------------------------------


# --------------------- os, os.path----------------------------------------------------------

# ---------------- os.listdir()
# pp(os.listdir())
# # возвращает список файлов и папок в директории
# # без аргументов - файлы и папки внутри текущей директории
#
# # можно передать аргумент который является отноительным путём для текущей директории
# pp(os.listdir('files_for_example')) # ['file1.txt', 'file2.txt', 'file3.txt']
# # такая папка была в нашей директории
# # а этой нет
# pp(os.listdir('path1')) # FileNotFoundError: [WinError 3] Системе не удается найти указанный путь: 'Django'
# # эта папка находится на директорию ниже


# # ---------------- os.path.exist()
# # есть ли папка или файл в этой директории
# pp(os.path.exists('files_for_example')) # True
# pp(os.path.exists('path1')) # False (но такой файл существует в директории ниже)
# pp(os.path.exists('random_library.py')) # True

# # ---------------- os.path.isdir() os.path.isfile()
# # os.path.isdir() - является ли путь папкой
# # os.path.isfile() - является ли путь файлом
# pp(os.path.isdir('random_library.py')) # False - не папка
# pp(os.path.isfile('random_library.py')) # True - файл
# pp(os.path.isdir('files_for_example')) # True - папка
# pp(os.path.isfile('files_for_example')) # False - не файл

# # ---------------- os.chdir()
# # os.chdir() - сменить директорию (опуститься ниже)
# pp(os.getcwd()) # 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\usefull-libraries\\Python'
# os.chdir('files_for_example')
# pp(os.getcwd()) # 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\usefull-libraries\\Python\\files_for_example'
# pp(os.listdir()) # ['file1.txt', 'file2.txt', 'file3.txt', 'path1']

# ---------------- os.getcwd()
# pp(os.getcwd()) # 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\usefull-libraries\\Python'
# # определяет текущую директорию

# pp(os.path.dirname(os.getcwd())) # 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\usefull-libraries'
# # абсолютный путь к текущей директории


# # ---------------- os.walk()
# # os.walk(top, topdown=True, onerror=None, followlinks=False) - генерация имён файлов в дереве каталогов,
# # сверху вниз (если topdown равен True), либо снизу вверх (если False).
# # Для каждого каталога функция walk возвращает кортеж (путь к каталогу, список каталогов, список файлов).
#
# # Позволяет рекурсивно пройтись по всем папка подпапкам и т.д.
# # он только вниз я так понимаю
# # возвращает нам генератор
# # и каждый раз спрашивая значение генератора он будет возвращать
# # кортеж из 3х элементов:
# # 1 - строковое представление текущей директории, которое он осматривает
# # 2 - список из всех подпапок, который есть в данной директории
# # 3 - список все файлов, который есть в данной директории
#
# # walk(top, topdown=True, onerror=None, followlinks=False)
#
# track = os.walk('.')
# pp(track.__next__()) # ('.', - текущая директория
#                      #  ['files_for_example'], - список из папок
#                      #  ['copy_library.py',               - список из файлов
#                      #   'datetime_library.py',
# pp(track.__next__())
# pp(track.__next__())
# pp(track.__next__()) # StopIteration
#
# track = os.walk('.')
# counter = 1
# for here, dirs, file in track:
#     print(f'{counter}) ', here, dirs, file, sep='\n', end='\n'+'-'*20 + '\n')
#     counter += 1































