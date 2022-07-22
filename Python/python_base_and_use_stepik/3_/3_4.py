from pprint import pprint as pp


"""
Текстовые форматы бывают разные, они представляют разные данные

cvs - Comma-Separated Values — значения, разделённые запятыми

пример cvs:

    first name,last name,module1,module2,module34
    student,best,100,100,100
    student,good,100,90.2,90
    
этот формат хорошо подходит, чтобы хранить табличные данные

в Python есть встроенная библиотека csv



3_4_2
from pprint import pprint as pp
import csv

crimes = {}
with open('dependecies/Crimes.csv', 'r') as file:
    reader = csv.reader(file)
    for line in reader:
        crimes[line[5]] = crimes.get(line[5], 0) + 1
# так:
crime = max(crimes, key=lambda x: crimes[x])
print(f'{crime} - {crimes[crime]}')
# или так:
# crimes = [(k,v) for k,v in crimes.items()]
# crimes.sort(key=lambda x: x[-1], reverse=True)
# pp(crimes[0])



3_4_4
import json

json_data = input()
hierarchy = json.loads(json_data)
hierarchy = {item['name']: set(item['parents']) for item in hierarchy}
ancestors_lst = set()
for cls in hierarchy.values():
    ancestors_lst.update(cls)
ancestors_lst = list(ancestors_lst)
childs_lst = list(set(hierarchy.keys()))

def dfs_paths(child, ancestor):
    stack = [(child, [child, ])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in hierarchy.keys():
            for next_ in hierarchy[vertex] - set(path):
                if next_ == ancestor:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_, ]))

counter = dict.fromkeys(childs_lst, 1)
for ancestor in ancestors_lst:
    for child in childs_lst:
        paths = list(dfs_paths(child, ancestor))
        # print(paths)
        if paths:
            counter[ancestor] += 1

# pp(hierarchy)
# pp(ancestors)
# pp(childs_lst)
# pp(counter)
childs_lst.sort()
for cls in childs_lst:
    print(f'{cls} : {counter[cls]}')





























"""

