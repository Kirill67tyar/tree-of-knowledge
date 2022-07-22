"""
sources:
    https://pythonworld.ru/moduli/modul-shutil.html
    https://docs.python.org/3/library/shutil.html
    https://digitology.tech/docs/python_3/library/shutil.html


Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок.
В частности, доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки.
Часто используется вместе с модулем os.

Модуль shutil предлагает ряд высокоуровневых операций с файлами и коллекциями файлов.
В частности, предусмотрены функции, поддерживающие копирование и удаление файлов.

методов очень много

    pp(dir(shutil))

но интересные copy() и copytree()
- copy() - позволяет скопировать файл и записать его в другом месте
- copy() - тоже самое но с целой папкой


"""
from pprint import pprint as pp
import shutil
import os
import datetime


date = datetime.date.today().strftime('%d-%m-%Y')
# ---------- copy
# # можно перезаписывать файл так:
# # открывать его, читать, сохранять в оперативной памяти инфу,
# # создавать новый и записывать инфу туда
#
# # а можно так
# # создаём переменные для работы
# source = 'experimental_file_for_os_sys/file1.txt'
# destenation = f'experimental_file_for_os_sys/file_destenation {date}.txt'
# # запускаем
# shutil.copy(src=source, dst=destenation)
#
# # можешь убедиться, мы увидим этот файл:
# # track = os.walk('.')
# # counter = 1
# # for here, dirs, file in track:
# #     print(f'{counter}) ', here, dirs, file, sep='\n', end='\n'+'-'*20 + '\n')
# #     counter += 1

# # ---------- copytree
# # позволяет скопировать папку
# # copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,
# #              ignore_dangling_symlinks=False, dirs_exist_ok=False)
# src = 'experimental_file_for_os_sys'
# dst = f'experimental_file_for_os_sys/dir-{date}'
# shutil.copytree(src=src, dst=dst)
# # здесь мы
# # 1 - копировали папку experimental_file_for_os_sys
# # 2 - создали папку dir-{date}
# # 3 - записали содержимое папки experimental_file_for_os_sys в dir-{date}


pp(dir(shutil))

