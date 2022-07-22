import sys

print(sys.argv)

# попробуй в консоли запустить этот скрипт
# kiril@LAPTOP-1D1S7LOO C:\Users\kiril\Desktop\...\python_essential\python_essential_modules\some_module$ python args_list.py 12, 3,5,2
"""
мы увидим имя модуля, (путь относительный командной строки)
и аргументы, которые мы туда передали  12, 3,5,2
"""
print(__name__)
print(__file__)