# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())

from pprint import pprint as pp
import sys
import builtins

"""

Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2, и "No", если не является.

Sample Input:

4
A
B наследуется от A
C : A
D : B C
4
A предок B?
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No



child           parents
B       :       [A, ]
C: [A]
D: [B, C]


classK classD
classH classG
"""
# import sys
# sys.stdin = open("test.txt", "r")

# здесь три решения, каждое в своей функции :
# dfs_paths
# show_relation
# show_relation2
# работает только решение dfs_paths
hierarchy = {}
answers = []
relations = {('parent', 'index'): None}
counter = 0
# в этой функции ошибок нет
def put_in_hierarchy(enter):
    if ':' in enter:
        child, parents = enter.split(':')
        child = child.strip()
        parents = set(map(lambda elem: elem.strip(), parents.strip().split()))
        hierarchy[child] = parents
    else:
        cls = enter.strip()
        hierarchy[cls] = set()

def put_in_relations(enter):
    if ':' in enter:
        child, parents = enter.split(':')
        child = child.strip()
        parents = list(map(lambda elem: elem.strip(), parents.strip().split()))
        check_key = lambda item, elem: elem == item[0]
        global counter
        for cls in parents:
            relations[(cls, counter)] = child
            counter += 1

def show_relations2(child, ancestor):
    for i in range(counter + 1):
        if relations.get((ancestor, i)) == child:
            return True
    return False



def dfs_paths(graph, child, ancestor):
    stack = [(child, [child, ])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in graph.keys():
            for next_ in graph[vertex] - set(path):
                if next_ == ancestor:
                    yield path + [next_]
                else:
                    stack.append((next_, path + [next_, ]))




def show_relation(ancestor, child):
    if child in hierarchy:
        if ancestor in hierarchy[child]:
            return True
        for cls in hierarchy[child]:
            show_relation(child, cls)
    return False





count_enters = int(input())
for i in range(count_enters):
    enter = input()
    put_in_hierarchy(enter)

counter_outputs = int(input())
for i in range(counter_outputs):
    enter = input()

    ancestor, child = enter.split()
    # answers.append(show_relation(ancestor, child))
    if ancestor == child:
        answers.append('Yes')
    else:
        data = list(dfs_paths(hierarchy, child, ancestor))
        # data = show_relations2(child, ancestor)
        if data:
            answers.append('Yes')
        else:
            answers.append('No')


print(*answers, sep='\n')







# првоверка put_in_hierarchy. Она работает правильно.
# data_for_check = {'classE': ['classD', 'classF', 'classK', 'classL'], 'classH': ['classL'], 'classK': ['classH', 'classL'], 'classG': ['classF'], 'classC': ['classE', 'classD', 'classH', 'classK', 'classL'], 'classB': ['classC', 'classE', 'classG', 'classH', 'classK', 'classL'], 'classA': ['classB', 'classC', 'classD', 'classG', 'classH'], 'classF': ['classK'], 'classD': ['classG', 'classH'], 'classL': []}
#
pp(hierarchy)
# print()
# pp(data_for_check)
#
# pp(hierarchy == data_for_check)






# проверка dfs_path
yes_no = """
Yes
Yes
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
Yes
No
Yes
Yes
Yes
No
Yes
No
No
Yes
Yes
No
No
No
Yes
Yes
No
Yes
No
No
No
Yes
Yes
Yes
No
"""
yes_no = set(enumerate(yes_no.split('\n')[1:-1], start=1))
length1 = len(yes_no)
answers = set(enumerate(answers, start=1))

output = list(answers.difference(yes_no))
output.sort(key=lambda x: x[0])
# yes_no = list(yes_no)
# yes_no.sort(key=lambda x: x[0])
counter = 0
for i, elem in enumerate(output, start=1):
    counter += 1
    print(f'{elem[0]} - {elem[-1]}')
print()
print(counter)