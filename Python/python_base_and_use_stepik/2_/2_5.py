from pprint import pprint as pp

# pp(globals())
# pp(dir(__builtins__))




"""
map, filter, zip - и другие итераторы, являются по сути ленивой функцией

    ls = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = map(lambda x: x / 0, ls)  # (ошибка не вызывается)
    m # <map object at 0x000002300B4B7B20> (ошибка не вызывается)
    next(m) # ZeroDivisionError: division by zero
    
в примере выше ошибка вызывается когда мы начинаем итерировать наш итератор\

map и filter можно с лёгкостью записать и в виде генераторов

    # map
    m = (int(i) for i in ['1', '2',])
    # filter
    f = (int(i) for i in ['1', '2',] if i.isdigit())
    f.__next__() # 1
    f.__next__() # 2
    
разумеется метод __next__() реализован в map, filter, zip

    hasattr(zip, '__next__') # True
    
    

------- lambda

при определении аргументов lambda всё что верно для обычной функции, 
всё то же верно и для lambda
т.е. аргументы в lambda функции мы можем также опредеять и передавать как и в 
обчной функции (позиционные, именованные, *args и т.д.)

более того:

    def my_func(): return 1
    my_func.__name__ # 'my_func'
    lf = lambda : 5+5
    lf.__name__ # '<lambda>'
    
    # но, приэтом
    type(my_func) # <class 'function'>
    type(lf) # <class 'function'>
    
У lambda функции и у обычной функции одинаковый тип данных - <class 'function'>


--------------------------Задание 2_5_6

def mod_checker(x, mod=0):
    lf = lambda y : y % x == mod
    return lf

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True














"""



















