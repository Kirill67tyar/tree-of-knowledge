"""
sources:
    https://docs.python.org/3/library/json.html
    https://pythonworld.ru/moduli/modul-json.html

    неплохие статьи
    https://pyneng.readthedocs.io/ru/latest/book/17_serialization/index.html#csv-json-yaml
    https://python-scripts.com/json

    мой декодер и инкодер
    https://github.com/Kirill67tyar/datetime-encoder/blob/master/custom_json_hook.py

    генерация большого объёма JSON данных
    https://python-scripts.com/elizabeth

    отлично подходит для тестового API:
    https://jsonplaceholder.typicode.com/


модуль json - для работы с json документами

следующие функции:
-- dump - для превращения из словаря в json
-- dumps - для записи в файл .json
-- load - для превращения из json в словарь
-- loads - для чтения файла .json
-- JSONDecoder
-- JSONDecodeError
-- JSONEncoder






    data = {
            'first_name': 'Eugene',
            'last_name': 'Petrov',
            'birthday': date(year=1986, month=9, day=29),
            'hired_at': datetime(2006, 9, 29, 12, 30, 5),
            'hobbies': [
                'guitar',
                'cars',
                'mountains',
                'adventures'
            ]
        }

    # -------------------------------------------------------
    # пример использования dumps
    json_data = json.dumps(data, cls=DatetimeJSONEncoder, indent=3)
    # pprint(json_data)

    # # пример использования dump
    # with open('../files/record_data.json', 'w', encoding='utf-8') as f:
        # json.dump(data, f, cls=DatetimeJSONEncoder, indent=3)
    # -------------------------------------------------------



    # -------------------------------------------------------
    # # пример использования loads
    py_date = json.loads(json_data, object_hook=from_str_to_datetime_hook)
    pprint(py_date)

    # # пример использования load
    # with open('../files/record_data.json', 'r', encoding='utf-8') as f:
    #     file_py_date = json.load(f, object_hook=from_str_to_datetime_hook)
    #     pprint(file_py_date)
    # # -------------------------------------------------------


Немного теории:

Как правило, процесс кодирования JSON называется сериализация.
Этот термин обозначает трансформацию данных в серию байтов
(следовательно, серийных) для хранения или передачи по сети.

Естественно, десериализация — является противоположным процессом декодирования данных,
которые хранятся или направлены в стандарт JSON.

Таблица конвертации данных Python в JSON:

    Python	        JSON
    dict	        object
    list, tuple	    array
    str	            string
    int, float	    number
    True	        true
    False	        false
    None	        null

Таблица конвертации JSON в данные Python:

    JSON	        Python
    object	        dict
    array	        list
    string	        str
    number          (int)	int
    number          (real)	float
    true	        True
    false	        False
    null	        None


"""
import json
from pprint import pprint as pp
# ---------------------------------- analizetools
from analizetools.analize import *

#     'p_dir', 'p_mro',
#     'p_glob', 'p_loc', 'p_type',
#     'p_content', 'show_doc',
#     'delimiter', 'show_builtins',
# ---------------------------------- analizetools


student1 = {'first_name': 'Tom',
        'last_name': 'Cat',
        'hobbies': [
            'guitar',
            'cars',
            'mountains',
            'adventures'
        ]
        }

student2 = {'first_name': 'Jerry',
        'last_name': 'Mouse',
        'hobbies': [
            'guitar',
            'cars',
            'mountains',
            'adventures'
        ]
        }
students = [
    student1,
    student2,
]

# # -------- dumps (в json) и loads (из json) --------
# # dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True,
# #         allow_nan=True, cls=None, indent=None, separators=None,
# #         default=None, sort_keys=False, **kw)
#
# # loads(s, *, cls=None, object_hook=None, parse_float=None,
# #         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
#
#
# # загружаем в формат .json (объект str в Python)
# json_object = json.dumps(students, indent=3)
# pp(json_object)
#
# # загружаем из .json (объект dict в Python)
# python_object = json.loads(json_object)
# pp(python_object)



# Запись в файл
# -------- dump (в файл json) и load (из файла json) --------

# dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True,
#         allow_nan=True, cls=None, indent=None, separators=None,
#         default=None, sort_keys=False, **kw)

# load(fp, *, cls=None, object_hook=None, parse_float=None,
#         parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)


# dump(какой объект, fp=в какой файл)
with open('files_for_example/students.json', 'w') as file:
    json.dump(obj=students, fp=file, indent=3, sort_keys=True)
    # obj=students - объект Python (обязательный аргумент)
    # fp=file - файл куда записывать (обязательный аргумент)


with open('files_for_example/students.json', 'r') as file_json:
    python_obj = json.load(file_json)


pp(python_obj)















