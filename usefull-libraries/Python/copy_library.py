"""
sources:
    https://docs.python.org/3/library/copy.html
    https://pythonworld.ru/moduli/modul-copy.html


Данный модуль позволяет выполнять полные и не полные копии любых произвольных объектов
Полная копия - копия как структуры, так и всех объектов, которые в неё входят
Неполная копия - копия самой структуры данных, с сохранением всех ссылок
на отдельные элементы, которые там были

Две функции в этом модуле:

copy.copy(x) - возвращает поверхностную копию x.

copy.deepcopy(x) - возвращает полную копию x.

help(copy)
"""
from pprint import pprint as pp
import copy

class Container:
    def __init__(self, ls=[1,2,3,]):
        self.list = ls
        self.int = 123

obj = Container([1,2,3,4,])

obj_copy = copy.copy(obj) # неглубокая копия
obj_copy.list.extend(range(10))

# как видим просто копия создаёт shallow copy (неглубокую копию)
# print(obj.list) # [1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

obj_deepcopy = copy.deepcopy(obj_copy)
obj_deepcopy.list.insert(0, True)

# как видим deepcopy создаёт полную, глубокую копию
# print(obj.list) # [1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(obj_deepcopy.list) # [True, 1, 2, 3, 4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Ну и мякотка
ls = [1,2,3,]
lss = ls
lls = ls.copy()

llss = [ls,lss,lls,]

ls_copy = llss.copy()
ls_deepcopy = copy.deepcopy(llss)

llss[0].append(4)

# Здесь мы выдим глубокую копию на деле.
# Очень полезный метод. Один список мы копировали с помощью shallow copy,
# а другой с помощью deepcopy.
# и в случае с deep copy даже элементы этого списка (тоже списки),
# заново создались в памяти
print(ls_copy) # [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3]]
print(ls_deepcopy) # [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


result = list(zip(list(map(id, llss)),list(map(id, ls_copy)), list(map(id, ls_deepcopy))))

# здесь видно, что id списков в списке копированном deepcopy
# отличаются от таковых спика, копированного с помощью
# встроенного метода copy() (shallow copy)
for i,j,k in result:
    print(i,j,k, sep='\n',end='\n'*2)
