# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())
from pprint import pprint as pp
from pathlib import Path
import os, sys, math

# ---------------------------------------------------------------------


#
# try:
#     import args_list
#     print('Exceptions not found')
# except ModuleNotFoundError:
#     module_path = os.path.join('..', 'some_module') # '..\\some_module'
#     sys.path.append(module_path) # список доступных путей (каталогов) для импорта модулей
#     import args_list
#
# try:
#     import fibonacci
#     print('Exceptions not found')
# except ModuleNotFoundError:
#     module_path = os.path.join('..', 'fibonacci_package') # '..\\some_module'
#     sys.path.append(module_path) # список доступных путей (каталогов) для импорта модулей
#     import fibonacci
#
# # import fibonacci
# #
# print(fibonacci.nth_fibonacci(10))

# ---------------------------------------------------------------------

"""
секция выше была посвящена склейке оносительных путей. но как работать с абсолютными?

У модулей есть атрибут __name__

Но также у них есть очень важный атрибут __file__

__file__ - показывает абсолютный путь модуля, в котором он вызывается + его имя
Но на самом деле это далеко не всегда абсолютный путь. 
Иногда он может быть не абсолютным. 
В общем при каких-то абстоятельствах __file__ выдаёт не абсолютный путь,
а при каких не понял
"""
#
# pp(globals())
# print('='*50)
# pp(locals())

# from pathlib import Path
# p = Path(__file__)
# print(p.parent)

# import os
# import sys
#
# try:
#     import fibonacci
#
#     print('Exceptions not found')
# except ModuleNotFoundError:
#     module_path = os.path.join('..', 'fibonacci_package')  # '..\\some_module'
#     sys.path.append(module_path)  # список доступных путей (каталогов) для импорта модулей
#     import fibonacci
# (
# # import fibonacci
# #
# ls = enumerate([
#     fibonacci.nth_fibonacci(10),  # 1
#     __file__,                     # 2
#     fibonacci.__file__,           # 3
#     fibonacci.pkg,                # 4
# ], start=1)

# print(fibonacci.nth_fibonacci(10))
# for i, elem in ls:
#     print(str(i) + ') ', elem)
# print(fibonacci.nth_fibonacci(100))
# ---------------------------------------------------------------------

#
# # print(os.path.abspath('qwerty'))
# # print(os.path.abspath(__file__)) # C:\Users\kiril\Desktop\...\python_essential_modules\another_directory\practice_from_another_directory.py
# # # print(__file__) # C:\Users\kiril\Desktop\...\python_essential_modules\another_directory\practice_from_another_directory.py
# ls = enumerate([
#     os.path.dirname(__file__),
#     os.path.basename(__file__),
#     os.path.dirname('asd'),
#     os.path.basename('asdasdasd'),
#
# ], start=1)
# for i, elem in ls:
#     print(str(i) + ') ', elem)
#     pass
#
# # print(os.path.dirname('asd'))
#
# help(os.path.basename)
# help(os.path.basename)
# ---------------------------------------------------------------------

# сначала мы узнаём абсолютный путь + файл, а затем только абсолютный путь
# os.path.dirname(__file__) здеь не сработал бы, т.к. он мог бы дать относительный путь
current_path = os.path.dirname(os.path.abspath(__file__))

parent_path = os.path.dirname(current_path)

fibonacci_module = os.path.join(parent_path, 'fibonacci_package')

sys.path.append(fibonacci_module)

import fibonacci

print(fibonacci.nth_fibonacci(100),'!'*20)


env = os.environ

for k in env:
    print(k, ' - ', env[k])
# pp(env['ALLUSERSPROFILE'])


import package.module
import package.subpackage.module
from package import module
from package import item
from package.subpackage import module, item
from module import *