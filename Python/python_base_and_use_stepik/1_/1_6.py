from pprint import pprint as pp

# pp(globals())
# pp(dir(__builtins__))




"""
1.6.7
# count = int(input())
# answers = []
# storage = {}
# 
# def select(parent, child):
#     if parent in storage[child]:# or parent == child:
#         return answers.append("Yes")
#     elif parent not in storage[child]:
#             for ch in storage[child]:
#                 if ch in storage:
#                     return select(parent,ch)
#     return answers.append("No")
# 
# for i in range(count):
#     new_class = input()
#     if ":" in new_class:
#         child_class, parent_class = new_class.split(" : ")
#         if len(parent_class) > 1:
#               parent_class = parent_class.split()
#               storage[child_class] = parent_class
#         else:
#               storage[child_class] = [parent_class]
# 
# count = int(input())
# for i in range(count):
#     d = input()
#     if len(d) > 1:
#         parent, child = d.split()
#         if child == parent:
#             answers.append("Yes")
#         elif child in storage:
#             select(parent, child)
#         else:
#             answers.append("No")
#     else:
#         answers.append("Yes")
# 
# print(*answers,sep="\n")


Классы от которых класс наследуется напрямую - являются ролдительскими классами
классы от которых наследуются родительские классы - являются предками первоначального класса

MRO предоставляет список классов в том порядке, в каком бы мы их перебирали
когда бы искали метод у самого младшего класса
и где впервые этот метод встретится (в каком класса), на этом месте поиск и прекратится
и будет использоваться именно первый выстретившийся метод

наглядный пример, что такое миксины:

    class EvenOddListMixin:
        def even(self):
            return len(self) % 2 == 0
            
        def odd(self):
            return len(self) % 2 == 1
            
    class MyList(list, EvenOddListMixin):
        pass
        

"""

from datetime import date, timedelta


year, month, day = map(int, input().split())
d = date(year=year, month=month, day=day)
days = timedelta(days=int(input()))

d += days
print(d.year, d.month, d.day)


















