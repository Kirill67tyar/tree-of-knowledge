from pprint import pprint as pp

# pp(globals())
# pp(dir(__builtins__))




"""
2.1.6
try:
    foo()
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')

2.1.7
count = int(input())
answer = []
storage = {}
errors = []

def select(error, parent_error):
    if parent_error in storage[error]:
        return True
    elif parent_error not in storage[error]:
            for ch in storage[error]:
                if ch != None:
                    return select(ch,parent_error)
                else:
                    return False


for i in range(count):
    new_errors = input()
    if ":" in new_errors:
        child_error, parent_error = new_errors.split(" : ")
        storage[child_error] = [parent_error]
    else:
        storage[new_errors] = [None]



count = int(input())
for i in range(count):
    error = input()
    if len(errors) == 0:
        errors.append(error)
    else:
        for er in errors:
            d = select(error, parent_error)
            if d == False:
                errors.append(error)
                break
            elif d == True:

                answer.append(error)
                break
print(*answer, sep='\n')

2.1.9
class NonPositiveError(BaseException):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            return super().append(x)
        
        raise NonPositiveError

В ошибках очень важная вещь, это разворачивание стека вызовов ошибок,
когда читаешь сообщение об ошибках

вот пример вызова ошибки в функции:

    ls = [1,2,3,]
    def f():
        return ls[3]

    f()
    
вот что интерпретатор выведет:

    Traceback (most recent call last):
      File "C:\Users\kiril\Desktop\Job\\tree-of-knowledge\Python\python_base_and_use_stepik\\2_\practice.py", line 8, in <module>
        f()
      File "C:\Users\kiril\Desktop\Job\\tree-of-knowledge\Python\python_base_and_use_stepik\\2_\practice.py", line 5, in f
        return ls[3]
    IndexError: list index out of range
    
на нижней строчке, выводится сообщение, что ошибка возникла в функции f
(, line 5, in f)

а строчкой выше идёт сообщение, что функция f была вызвана в функции module на 8 строчке
(, line 8, in <module>)

Ошибки нужны, чтобы сообщить нам, что в нашем коде проищошло что-то такое,
из-за чего продолжение кода становится бессмысленным,
а текущее состояние стека вызовов, тип ошибки и дополнительное сообщение
нужны для того, чтобы сказать где именно это произошло,
и что именно у нас произошло


у экземпляра ошибки есть атрибут args
tuple args содержит аргументы, с которым создаётся экземпляр класса,
или аргументы, которые мы передаём сам при поднятии ошибки (создании экземпляра класса) 

    try:
        f()
    except IndexError as err:
        print(err.args) # ('list index out of range',)
        
или так

    try:
        raise TypeError('та-ша')
    except TypeError as err:
        print(err.args) # ('та-ша',)
        


----------------------------------- Задание 2.1.7 --------------------------------------------

Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Или эквивалентно записи:
class Error1(Error2, Error3 ... ErrorK):
    pass

Антон написал код, который выглядит следующим образом.

try:
   foo()
except <имя 1>:
   print("<имя 1>")
except <имя 2>:
   print("<имя 2>")
...
Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно не ловить, 
так как ранее в коде будет пойман их предок. Но Антон не помнит какие исключения наследуются от каких. 
Помогите ему выйти из неловкого положения и напишите программу, которая будет определять обработку каких 
исключений можно удалить из кода.

Важное примечание:
В отличие от предыдущей задачи, типы исключений не созданы.
Создавать классы исключений также не требуется
Мы просим вас промоделировать этот процесс, и понять какие из исключений можно и не ловить, 
потому что мы уже ранее где-то поймали их предка.

Формат входных данных
В первой строке входных данных содержится целое число n - число классов исключений.

В следующих n строках содержится описание наследования классов. 
В i-й строке указано от каких классов наследуется i-й класс. 
Обратите внимание, что класс может ни от кого не наследоваться. 
Гарантируется, что класс не наследуется сам от себя (прямо или косвенно), 
что класс не наследуется явно от одного класса более одного раза.

В следующей строке содержится число m - количество обрабатываемых исключений.
Следующие m строк содержат имена исключений в том порядке, в каком они были написаны у Антона в коде.
Гарантируется, что никакое исключение не обрабатывается дважды.

Формат выходных данных
Выведите в отдельной строке имя каждого исключения, обработку которого можно удалить из кода, 
не изменив при этом поведение программы. Имена следует выводить в том же порядке, 
в котором они идут во входных данных.

Пример теста 1
Рассмотрим код

try:
   foo()
except ZeroDivision :
   print("ZeroDivision")
except OSError:
   print("OSError")
except ArithmeticError:
   print("ArithmeticError")
except FileNotFoundError:
   print("FileNotFoundError")


...


По условию этого теста, Костя посмотрел на этот код, и сказал Антону, 
что исключение FileNotFoundError можно не ловить, ведь мы уже ловим OSError -- предок FileNotFoundError
Sample Input:

4
ArithmeticError
ZeroDivisionError : ArithmeticError
OSError
FileNotFoundError : OSError
4
ZeroDivisionError
OSError
ArithmeticError
FileNotFoundError
Sample Output:

FileNotFoundError


"""

"""

"""
# 1я строка - кол-во вводов классов
# далее вводы классов где
# child   :   ancestor
# после итерации - строка ввода классов, в каком порядке они распологаются в конструкции try/except

import sys
# tests:
# sys.stdin = open("test.txt", "r")
# sys.stdin = open("test2.txt", "r")
# sys.stdin = open("test3.txt", "r")


hierarchy = {}
classes = []
extra_classes = []
def put_in_hierarchy(enter):
    if ':' in enter:
        child, parents = enter.split(':')
        child = child.strip()
        parents = set(map(lambda elem: elem.strip(), parents.strip().split()))
        hierarchy[child] = parents
    else:
        cls = enter.strip()
        hierarchy[cls] = set()

def dfs_paths(child, ancestor):
    # if child == ancestor:
    #     return True
    stack = [(child, [child, ])]
    while stack:
        (vertex, path) = stack.pop()
        if vertex in hierarchy.keys():
            for next_ in hierarchy[vertex] - set(path):
                if next_ == ancestor:
                    # yield path + [next_]
                    return True
                else:
                    stack.append((next_, path + [next_, ]))

count = int(input())
for i in range(count):
    enter = input()
    put_in_hierarchy(enter)

# pp(hierarchy)

# input2 - показываем, как будем распологать классы
count_part2 = int(input())
for i in range(count_part2):
    cls  = input()
    classes.append(cls.strip())


# а здесь вычисляем, используя функцию dfs_paths
# (алгоритм поиска в глубину для графов)
# dfs_paths(child, ancestor)
for i in range(len(classes)-1, 0, -1):
    built_path = any(filter(lambda cls: dfs_paths(classes[i], cls), classes[:i]))
    if built_path and classes[i] not in extra_classes:
        extra_classes.append(classes[i])
extra_classes.reverse()
print(*extra_classes, sep='\n')


















