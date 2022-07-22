# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())
#

# ---------------------------------------------------------------------

# from fibonacci import nth_fibonacci as nth
# import fibonacci
# nth = fibonacci.nth_fibonacci
# del fibonacci
#
# number = int(input('Enter number for fibonacci: '))
# print(f'Result: {nth(number)}')
# print(nth.__name__)

# ---------------------------------------------------------------------

# from math import ceil
# import random
# import requests as req
# import string
# st = string
# del string
#
# c = ceil
# del ceil
#
# x = 3.14
#
# # print(x, c(x),sep='\n')
# print(random.__name__)
# print(req.__name__)
# print(st.__name__)
# print(__name__)

# ---------------------------------------------------------------------

# import sys
#
# print(sys.argv) # ['C:/Users/kiril/Desktop/Job/tree-of-knowledge/Python/python_essential/python_essential_modules/practice.py']

# ---------------------------------------------------------------------


# ---------------------------------------------------------------------

def console(value, d=None, m=None):
    from pprint import pprint
    if d and m:
        m = None
    elif d:
        value = dir(value)
    elif m:
        if type(value) == type:
            value = value.mro()
        else:
            value = type(value).mro()
    return pprint(value)


# console(globals())
# print()
# print(locals() == globals())
from pprint import pprint as pp
a = 2
def f():
    b = 1
    pp(globals())
    print()
    pp(locals())
    print('b' in globals())
    print('b' in locals())
f()