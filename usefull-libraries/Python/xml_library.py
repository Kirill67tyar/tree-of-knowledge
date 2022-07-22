"""
sources:
    https://docs.python.org/3/library/xml.etree.elementtree.html
    https://python-scripts.com/xml-python

В целом - похоже на работу с библиотекой Beautiful Soup

 -- ElementTree.parse - парсить xml джокумент
 -- ElementTree.fromstring - парсить xml данные в виде строки

методы
ElementTree.parse('files_for_example/students.xml')

     find
     findall
     findtext
     getroot
     iter
     iterfind
     parse
     write
     write_c14

"""

from pprint import pprint as pp


from xml.etree import ElementTree
# ---------------------------------- analizetools
from analizetools.analize import *

#     'p_dir', 'p_mro',
#     'p_glob', 'p_loc', 'p_type',
#     'p_content', 'show_doc',
#     'delimiter', 'show_builtins',
# ---------------------------------- analizetools


# # -------------------------------------------------- Считывание файла--------------------------------------------------
#
#
#
# # # # ------------------------------------------- ElementTree объект
# # p_dir(ElementTree)
# # delimiter('*')
# # p_type(ElementTree) # <class 'module'>
# # delimiter('*')
# # p_mro(ElementTree) # [<class 'module'>, <class 'object'>]
#
#
# # # -------------------------------------------  Объект дерева
tree = ElementTree.parse('files_for_example/students.xml')

# p_dir(tree)
# delimiter()
# p_type(tree) # <class 'xml.etree.ElementTree.ElementTree'>
# delimiter()
# p_content(tree)
# delimiter()
# p_mro(tree) # [<class 'xml.etree.ElementTree.ElementTree'>, <class 'object'>]
#
#
# # # -------------------------------------------  Объект root (tree.root())
# # pp(tree.getroot()) # <Element 'studentsList' at 0x0000022DCAC62A40>
root = tree.getroot()
# # +++++++++++++++++++
p_dir(root)
delimiter()
p_type(root) # <class 'xml.etree.ElementTree.Element'>
delimiter()
p_content(root)
delimiter()
p_mro(root) # [<class 'xml.etree.ElementTree.Element'>, <class 'object'>]



# # обход всего дерева +++++++++++++++++++
# def rec_tree(elem):
#     for e in elem:
#         print(e.text)
#         if e:
#             rec_tree(e)
# print(rec_tree(root))
# # +++++++++++++++++++


# # +++++++++++++++++++
# # pp(root.tag) # - показывает сам тег 'studentsList'
# # pp(root.attrib) # - показывает атрибуты тега
# # pp(root.text) # '\n    '
# # pp(root.text) # '\n    '
#
# # ------------ итерация root
# # Все объекты которые мы итерируем будут принадлежать классу Element
# # и у Element можно достать (есть атрибуты и методы):
# # tag - тег
# # attrib - атрибут тега
# # text - текст внутри тега
# # и т.д., смотри p_dir(root)
# # можно опуститься ниже используя атрибут tail
#
# p_type(root) # <class 'xml.etree.ElementTree.Element'>
# print(root.tag, root.attrib) # studentsList {}
# for child in root:
#     # такой же класс как  и root хоть мы его же и итерируем
#     # какой-то рекурсивный итератор получается (метода __next__ нету)
#     p_type(child) # <class 'xml.etree.ElementTree.Element'>
#     print(child.tag, child.attrib) # student {'id': '1'}
#                                     # student {'id': '2'}
#
#
# pp(root[0][0].text) # 'Greg'
#
#
# delimiter() #  -+-+-+-+-+--+-+-+-+-+-+-+-+-+-+
# # есть метод iter
# # передаёшь туда имя тега, который находится внутри
# scopes = root.iter('scope') # а ничего
# for elem in scopes:
#     print(elem) # ничего нет :)
# # у нас нет тега scope, а есть тег scores
# scores = root.iter('scores')
# # for elem in scores:
# #     print(elem)# <Element 'scores' at 0x00000282B0D70EF0>
# #     p_type(elem)# <class 'xml.etree.ElementTree.Element'>
#
#
# # суммируем баллы:
#
# for elem in scores:
#     score_sum = 0
#     for sc in elem:
#         score_sum += float(sc.text)
#     pp(score_sum)



# -------------------------------------------------- Записывание файла--------------------------------------------------
#
# # Записываем данные в файл в формате xml
#
# tree = ElementTree.parse('files_for_example/students.xml')
# root = tree.getroot()
#
# # записываем точную копию файла, который мы прочитали
# # tree.write('files_for_example/students_copy.xml')
#
#
# # увеличим оценку Grega с 70 до 90
# greg = root[0]
# score = next(greg.iter('module1'))
# print(score.text) # '70.0'
# score.text = str(float(score.text) + 21)
# print(score.text) # '91.0'
#
# # добавить или изменить атрибут с помощью метода set
# sertificate = greg[2]
# print(sertificate.attrib) # {}
# sertificate.set('type', 'with disctinction')
# print(sertificate.attrib) # {'type': 'with disctinction'}
#
# # записываем в копию
# tree.write('files_for_example/students_copy.xml')
#
#
#
# # ---------------------------------- Создание нового тега
# # создаём новый тег
# new_tag = ElementTree.Element('description')
# new_tag.text = 'Showed excellent skills during this course'
#
# # присоединяем его
# greg.append(new_tag)
#
# # записываем в копию
# tree.write('files_for_example/students_copy.xml')
#
# # ---------------------------------- Убрать тег
# # по быстрому записываем тег
# else_new_tag = ElementTree.Element('some_new_tag')
# else_new_tag.text = 'some_text'
# greg.append(else_new_tag)
# tree.write('files_for_example/students_copy.xml')
#
# # убираем some_new_tag
# tag = greg.find('some_new_tag') # находим
# greg.remove(tag) # убираем
# tree.write('files_for_example/students_copy.xml')
#
#
# # ---------------------------------- Записать полностью новый тег (старая инфа удалится)
#
# root = ElementTree.Element('student')
#
# # тег firstName
# firstName = ElementTree.SubElement(root, 'firstName')
# firstName.text = 'Tom'
#
# # тег lastName
# lastName = ElementTree.SubElement(root, 'lastName')
# lastName.text = 'Cat'
#
# # тег scores
# scores = ElementTree.SubElement(root, 'scores')
# # оценки scores
# module1 = ElementTree.SubElement(scores, 'module1')
# module1.text = '100'
# module2 = ElementTree.SubElement(scores, 'module2')
# module2.text = '80'
# module3 = ElementTree.SubElement(scores, 'module3')
# module3.text = '90'
#
#
# tree = ElementTree.ElementTree(root)
# tree.write('files_for_example/students_copy.xml')



















