from pprint import pprint as pp

# pp(globals())
# pp(dir(__builtins__))




"""
count = int(input())
answer = []
storage = {'global': {'parent': None, 'items': []}}
def get(namespace, item):
    if item in storage[namespace]['items']:
        return answer.append(namespace)
    elif item not in storage[namespace]['items'] and namespace != 'global':
        return get(storage[namespace]['parent'], item)
    else:
        return answer.append(None)
for i in range(count):
    act, namespace, item = input().split()
    if act == 'add':
        storage[namespace]['items'].append(item)
    elif act == 'create':
        storage[namespace] = {'parent': item, 'items': []}
    elif act == 'get':
        get(namespace, item)
print(*answer, sep='\n')
"""
"""
1.4.3



У нас 4 пространства имён (области видимости scope (scope - объём [сфера, рамки]) то же самое)
1) builtins   pp(dir(__builtins__))
2) global     pp(dir(globals()))
2) local      pp(dir(locals()))
2) enclosing     pp(dir(locals()))

Пространство имён очень взаимосвязано со стеком вызовов 
Глобальное пространство имён соответствует функции main на стеке вызовов
Пространство имён built-in лежит ниже main на стеке вызовов

Сначала интерпретатор переменную в пщетпространство имён в той функции
в которой эта переменная была вызваана, на стеке вызовов
Если в функции main, (самая базовая функция на стеке вызовов), 
то в глобальном прострастве имён
И если не найдёт её в глобальном пространстве имён, то спустится в пространство имён builtins

Именно поэтому мы можем перезатирать встроенные функции
и классы в Python

    list = 4
    print(list(range(5))) # TypeError: 'int' object is not callable
    
то же самое касается и функции. 

Во время поиска интерпретатор спускается вниз от самого верхнего,
пространства имён, до пространства имён builtins

    !!!                                                     !!!
        интерпретатор ищет переменную в пространстве имён
        самой верхней, на стеке вызовов, функции, и не найдя её там 
        спускается вниз, до пространства имён builtins, включительно
    !!!                                                     !!!    
Что было неправильно:  порядок поиска имени переменной не связан со стеком вызовов. 
Порядок поиска имени переменной связан лишь с порядком вложенности друг в друга областей видимости.        

Пространство имен - это словарь с именами и значениями.
Область видимости - это цепочка пространств имен, которая начинается от локального и длится до глобального или встроенного уровня.

***** scope (область видимости)
scope - объём [сфера, рамки]
область видимости - это просто кусок кода, блок, если быть точнее

Порядок областей видимости: local, non-local, global, built-in.
и для поиска переменной в функции действует правило LEGB - (local, enclosing, global, builtins)
        
Подумай, почему NameError 

def a():
    print(x)

def b():
    x = 5
    a()
        
b() # NameError
        
подсказка, функция a не определена в функции b
а значит её пространство имён не завёрнуто в пространство имён функции b,
хотя на стек вызовов она ложится

В этом собственно разница в простнастве имён и области видимости



    global variable     nonlocal variable

global - изменяет или создаёт переменную только в глобальном прострнастве имён
         остальные не трогает

nonlocal - ищет ближайшее к текущему пространство имён (в своём не ищет), с нужной переменной
           по пути от текущего пространства имён, до namespace global


        
        
        
        
        
        
        
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
Sample Output:

global
None
bar
foo    
        
        
        
        
        
        
        
        
        
"""
count = int(input())
output = []
# storage = {'global': {'parent': None, 'items': []}}
# def get(namespace, item):
#     if item in storage[namespace]['items']:
#         return output.append(namespace)
#     elif item not in storage[namespace]['items'] and namespace != 'global':
#         return get(storage[namespace]['parent'], item)
#     else:
#         return output.append(None)
# for i in range(count):
#     act, namespace, item = input().split()
#     if act == 'add':
#         storage[namespace]['items'].append(item)
#     elif act == 'create':
#         storage[namespace] = {'parent': item, 'items': []}
#     elif act == 'get':
#         get(namespace, item)
# print(*output, sep='\n')




























