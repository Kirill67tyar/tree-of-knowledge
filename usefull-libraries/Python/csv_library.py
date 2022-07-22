"""
sources:
    https://docs.python.org/3/library/csv.html
    https://pythonworld.ru/moduli/modul-csv.html

cvs - Comma-Separated Values — значения, разделённые запятыми

для работы с csv документами

Пример csv файла

    first name,last name,module1,module2,module34
    student,best,100,100,100
    student,good,100,90.2,90
    student,good,100,"90,2",90

в нижней строке, обрати внимание, используется запятая
значение изолированно двойными ковычками


вот ещё пример csv файла

    first name,last name,module1,module2,module3,description
    student,best,100,100,100,excellent score
    student,good,100,90.2,90,good score
    student,middle,70,"80,2",90,"middle score,
     can better"

"""
from pprint import pprint as pp
import csv
from csv import QUOTE_ALL, QUOTE_NONE, QUOTE_NONNUMERIC, QUOTE_MINIMAL
# ---------------------------------- analizetools
from analizetools.analize import *

#     'p_dir', 'p_mro',
#     'p_glob', 'p_loc', 'p_type',
#     'p_content', 'show_doc',
#     'delimiter', 'show_builtins',
# ---------------------------------- analizetools
#
# # --------------------------------------------------------------- ЧТЕНИЕ
# # csv
# with open('files_for_example/example_csv.csv', 'r') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)
#         # p_type(line)
#         pass
# delimiter()
#
# # tub-Separated Values
# with open('files_for_example/example_tsv.tsv', 'r') as file:
#     reader = csv.reader(file, delimiter='\t')
#     for line in reader:
#         # print(line)
#         # p_type(line)
#         pass
#
# # как видим мы просто передали явно аргумент delimiter
# # ввиде знака \t - табуляция
#
#
# # --------------------------------------------------------------- ЗАПИСЬ
#
#
# students = [
#     ["Tom", 'Cat', 70, 80, 90, 'good cat',],
#     ['Jerry', 'Mouse', 100, 100, 100, 'good mouse',]
# ]
# with open('files_for_example/example_csv.csv', mode='a') as file: # mode='a' - дозаписать
#     writer = csv.writer(file) # , quoting=csv.QUOTE_ALL - поместит все значения в ковычки
#     # for st in students:
#     #     writer.writerow(st)
#     # или
#     writer.writerows(students)
# # QUOTE_NONNUMERIC - все нечисловые значенния поместить в ковычки
#
# # QUOTE_NONE, QUOTE_NONNUMERIC, QUOTE_MINIMAL
#
# delimiter()
# with open('files_for_example/example_csv.csv', mode='r') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         print(line)
#         pass


# # 3_4_2 (Python: оснвы и применение)
# crimes = {}
# with open('files_for_example/Crimes.csv', 'r') as file:
#     reader = csv.reader(file)
#     for line in reader:
#         crimes[line[5]] = crimes.get(line[5], 0) + 1
# crimes = [(k, v) for k, v in crimes.items()]
# crimes.sort(key=lambda x: x[-1], reverse=True)
# pp(crimes[0])
