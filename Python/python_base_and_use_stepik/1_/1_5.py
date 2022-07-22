from pprint import pprint as pp

# pp(globals())
# pp(dir(__builtins__))




"""
В отличие от функций от функций тело класса исполняется в момент определения самого класса
 
        class CC: # ZeroDivisionError: division by zero
            var = 5 / 0
            
        CC # NameError: name 'CC' is not defined
        
        def f():
            var = 5 / 0
        
        f # <function f at 0x0000023B83161DC0>
        f() # ZeroDivisionError: division by zero
        
        
Идеологически, функция __init__(self) - всего лишь устанавливает атрибуты 
для нашего объекта self (экземпляра класса)
Поэтому __init__ ничего не должен возвращать, (вернее он возвращает None)
"""




























