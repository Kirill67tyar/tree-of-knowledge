from pprint import pprint as pp
import sys
from . import practice


"""
# pp(sys.modules)

Интерпретатор при инпорте модуля проверяет есть ли этот модуль в словаре sys.modules

Если он там, интерпретатор его достаёт и использует

Если его там нет, то интерпретатор выполняет процедуры импорта,
и после импорта модуля создаётся объект модуля в памяти, и Python добавляет
этот модуль в словарь sys.modules

вот наглядный пример:

    >>> 'requests' in sys.modules
    False
    >>> import requests
    >>> 'requests' in sys.modules
    True
    
вот ещё

    from pprint import pprint as pp
    import sys
    
    # pp(sys.modules)
    print(sys.modules.get('practice_module')) # None
    import practice_module
    print(practice_module.s) # 1
    print(sys.modules.get('practice_module')) # <module 'practice_module' from 'C:\\Users\\kiril\\Desktop\\Job\\tree-of-knowledge\\Python\\python_base_and_use_stepik\\2_\\practice_module.py'>
    

А что делать, если мы не нашли этот модуль в sys.modules?
интерпретатор будет искать этот модуль по названиям файлов с расширением .py
в этой директории. Или там, куда при импорте провили путь

И если там не найдёт, то будет искать во внешние библиотеки

пути, где интерпретатор будет искать модуль - в списке sys.path

"""