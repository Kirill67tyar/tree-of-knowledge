from pprint import pprint as pp



"""

sources:
    https://russianblogs.com/article/6870284562/
    https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html
    https://pavel-karateev.gitbook.io/intermediate-python/sintaksis/open_function
    

open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)

работа с файлом возвращает объект file_object с классом - <class '_io.TextIOWrapper'>

открытие файла таким образом

	with open('test.txt', mode='r') as file:
    		pp(type(file)) # <class '_io.TextIOWrapper'>

эквивалетно:
	file = open('test.txt', mode='r')
	pp(type(file)) # <class '_io.TextIOWrapper'>
	file.close()

!!!
очень полезный метод str.splitlines
при чтении file_object у нас появляется объект с типом данных str
и что-бы разбить этот объект по строкам в список
можно сделать так 
    file_object.read().split('\n')
    
а можно так
    file_object.read().splitlines()

второй вариант кроссплатформенный
!!!

***** класс type_object - <class '_io.TextIOWrapper'>
------------------------------
dir:
['_CHUNK_SIZE',
 '__class__',
 '__del__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__enter__',
 '__eq__',
 '__exit__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__iter__',
 '__le__',
 '__lt__',
 '__ne__',
 '__new__',
 '__next__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '_checkClosed',
 '_checkReadable',
 '_checkSeekable',
 '_checkWritable',
 '_finalizing',
 'buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines']
------------------------------
<class '_io.TextIOWrapper'>.mro():
[<class '_io.TextIOWrapper'>,
 <class '_io._TextIOBase'>,
 <class '_io._IOBase'>,
 <class 'object'>]


методы для file_object

 'buffer',
 'close',
 'closed',
 'detach',
 'encoding',
 'errors',
 'fileno',
 'flush',
 'isatty',
 'line_buffering',
 'mode',
 'name',
 'newlines',
 'read',
 'readable',
 'readline',
 'readlines',
 'reconfigure',
 'seek',
 'seekable',
 'tell',
 'truncate',
 'writable',
 'write',
 'write_through',
 'writelines'


==================================================

После закрытия файла тип данных остаётся тот же:

<class '_io.TextIOWrapper'>
"""
# работа с file_object
# прежде чем запустить код создай файл test.txt в этой директории

# data ----------------------------
# file = open('test.txt', mode='r')
#
# pp(type(file)) # <class '_io.TextIOWrapper'>
# print('-'*30,end='\n')
# pp(dir(file))
# print('-'*30,end='\n')
# pp(type(file).mro()) # [<class '_io.TextIOWrapper'>,
#                       # <class '_io._TextIOBase'>,
#                       # <class '_io._IOBase'>,
#                       # <class 'object'>]
# print('-'*30,end='\n')
# pp(dir(type(file)))
#
# file.close()
# print('\n')
# print('='*50)
# print('\n')
# # после закрытия
# pp(type(file)) # <class '_io.TextIOWrapper'>
# with open('test.txt', mode='r') as f:
#     pp(type(f)) # <class '_io.TextIOWrapper'>
#     print('-'*30,end='\n')
#     pp(dir(f))
#     print('-'*30,end='\n')
#     pp(type(f).mro()) # [<class '_io.TextIOWrapper'>,
#                           # <class '_io._TextIOBase'>,
#                           # <class '_io._IOBase'>,
#                           # <class 'object'>]

# examples ----------------------------
# (все файлы находятся в папке dependencies, добавь её при чтении файла)

# ---------------------- чтение файла (mode='r') --------------------

# # важно помнить, что read, readline, readlines считывают object_file
# # и убирают из него то что считали (!не из самого файла, а из объекта файла в Python)
# # это очень похоже на работу с итератором
# # !! test.txt - Это файл, где в текстовом виде написаны ошибки.
# # и поэтому при считке может быть строка 'ArithmeticError\n' и т.д.
# with open(file='test.txt', mode='r') as file_obj:
#     # # for read
#     # # -------------- for read ------------------------------
#     # data = file_obj.read(5)
#     # print(repr(data)) # '4\nAri'
#     # data2 = file_obj.read()
#     # # print(repr(data2))  # 'thmeticError\nZeroDivisionError : ArithmeticError\nOSError\nFileNotFoundError : OSError\n4\nZeroDivisionError\nOSError\nArithmeticError\nFileNotFoundError'
#     # data = data + data2
#     # ls_data = data.split('\n')
#     # ls_data2 = data.splitlines()
#     # print(ls_data, ls_data2, sep='\n') # ['4', 'ArithmeticError', 'ZeroDivisionError : ArithmeticError', 'OSError', 'FileNotFoundError : OSError', '4', 'ZeroDivisionError', 'OSError', 'ArithmeticError', 'FileNotFoundError']
#
#     # -------------- for readlines --------------------------
#     # data_lines = file_obj.readlines() # ['4\n', 'ArithmeticError\n', 'ZeroDivisionError : ArithmeticError\n', ...
#     # print(data_lines)
#
#     # # -------------- for readline --------------------------
#     # data_line = file_obj.readline()
#     # print(data_line)
#     # data_line2 = file_obj.readline() # 'ArithmeticError\n'
#     # print(repr(data_line2))
#     # data_line2 = data_line2.rstrip() # 'ArithmeticError'
#     # print(repr(data_line2))
#     ## но readline здесь действует как __next__()
#     ## file_object можно спокойно итерировать, и это даже более экономно
#
#     # # -------------- итерация file_object --------------------------
#     # for line in file_obj:
#     #     print(repr(line)) # 'ArithmeticError\n'
#     #     line = line.rstrip() # убирает символ переноса строки
#     #     print(repr(line)) # 'ArithmeticError'
#     #
#     # ## когда в файле не осталось не считанной информации
#     # ## метод read() будет возвращать пустую строку
#     # print('-'*30)
#     # print(repr(file_obj.read())) # - ничего - ''
#     # print(file_obj.readline()) # - ничего - ''
#     # print(file_obj.readlines()) # - []
#     pass


# ---------------------- создание и запись файла (mode='w') --------------------
# # 1)
# file1 = open('my_test.txt', 'w')
# file1.close() # - всё. файл создан
#
# # 2)
# # или так
# with open('my_test2.txt', 'w') as file:
#     pass


# with open('my_test2.txt', 'w') as file_obj:
#     # file_obj.write('Hello')
#     # file_obj.write('world') # Helloworld
#     #
#     # # поэтому важно использовать перенос строк и специальные симоволы
#     # file_obj.write('\nHello\n')
#     # file_obj.write('blya\n')    # Hello
#     #                         # blya
#     #
#     # # очень часто может быть полезен join
#     # lines = ['raw1', 'raw2', 'raw3',]
#     # file_obj.write('\n'.join(lines))
#     # print(file_obj) # <_io.TextIOWrapper name='my_test2.txt' mode='w' encoding='cp1251'>
#     # print(type(file_obj)) # <class '_io.TextIOWrapper'>
#     pass


# ----- как дозаписать данные в конец файла
# mode='a' - создаёт файл если его небыло, а если он был
# то дозаписывает данные в конец файла

# много раз нажми ctrl-shift-f10
# with open('my_test3.txt', 'a') as file_obj:
#     file_obj.write('ТААААА - \n')
#     file_obj.write(' - ШААААА\n')



# лайфхак, в менеджере контекста with можно открывать сразу несколько файлов

# with open('my_test3.txt', 'r') as file_obj1_R, open('my_test4.txt', 'w') as file_obj2_W:
#     for line in file_obj1_R:
#         file_obj2_W.write(line)
    # здесь мы записываем данные из файла  my_test3.txt в файл my_test4.txt
    # запишется my_test4.txt - точная копия my_test3.txt