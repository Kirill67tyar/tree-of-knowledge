# help(dict(a=1).items())
# print(*dir(dict(a=1).items()), sep='\n')
# print(type())
#
from pprint import pprint as pp
import sys

class IteratorInt:

    def __init__(self, integer):
        self._next = 0
        self._tail = integer

    def __iter__(self):
        return self

    def __next__(self):
        if self._next < self._tail and 0 < self._tail:
            result = self._next
            self._next += 1
            return result
        elif self._next > self._tail and 0 > self._tail:
            result = self._next
            self._next -= 1
            return result
        else:
            raise StopIteration

class Int(int):

    def __iter__(self):
        # return IteratorInt(self)
        # # or
        for _ in range(self):
            yield _



    def __getitem__(self, item):
        return range(self)[item]

    def print_int(self):
        print(self)
        return self

#
# i = Int(5)
# print(i)
# print(type(i))
# print(i + 5)
# i = Int(i ** 2)
# print(i)
# print(type(i))
# # print(i.print_int())
# print(list(i))
# for _ in i:
#     print(_)
# print(i[2])

def show_builtins():
    key_builtins = globals().get('__builtins__')
    if key_builtins:
        if isinstance(key_builtins, dict):
            return pp(key_builtins)
        return pp(dir(key_builtins))
    else:
        return pp("Can't show builtins")

show_builtins()

pp(sys.builtin_module_names)