from pprint import pprint as pp
import sys


"""


Итератор для списка, который выводит элементы списка по два

    class DoubleIterList:
        def __init__(self, sequence):
            self.sequence = sequence
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.i += 2
            if self.i <= len(self.sequence):
                return self.sequence[self.i-2], self.sequence[self.i-1]
            elif self.i - len(self.sequence) == 1:
                return self.sequence[self.i-2]
            raise StopIteration


    class MyList(list):
        def __iter__(self):
            # так
            return DoubleIterList(self)

            # или через генератор
            count = 0
            while count + 1 <= self.__len__():
                count += 2
                if count - len(self) == 1:
                    yield self[count-2]
                    break
                yield self[count-2], self[count-1]


    ls = MyList([1,2,3,4])
    lls = MyList([1,2,3])

    for i in ls:
        print(i)

    for i in lls:
        print(i)



 ----- 2_3_3 -----

Как только при итерации генератора интерпретатор не найдёт ключевое слово yield
Но вызовет ошибку StopIteration

С помощью генераторов в языке Python реализуется концепция отложенного исполнения

У return в генераторах очень интересное поведение
если мы возвратим return до ключевого слова yield,
то вызовется ошибка StopIteration, а в аргументы этой ошибка
передастся то что мы ретёрнули:

    def gen():
        yield 'start'
        yield 1
        return 'no more elements' # StopIteration: no more elements
        
        yield 2 
        yield 'finish'   


    g = gen()
    print(g.__next__()) # start
    print(g.__next__()) # 1
    print(g.__next__()) # StopIteration: no more elements




def gen():
    yield 'start'
    yield 1
    return 'no more elements'
    
    yield 2 
    yield 'finish'   

g = gen()
print(g.__next__())
print(g.__next__())
print(g.__next__())




задача 2_3_4

# class multifilter:
#     def judge_half(pos, neg):
#         return pos >= neg
#
#     def judge_any(pos, neg):
#         return pos
#
#     def judge_all(pos, neg):
#         return neg == 0
#
#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#         # for elem in self.iterable:
#         #     array = []
#         #     for f in self.funcs:
#         #         array.append(f(elem))
#         #     pos = len(list(filter(lambda x: x, array)))
#         #     neg = len(self.funcs) - pos
#         #     if self.judge(pos, neg):
#         #         yield elem
#
#     def __next__(self):
#         for i in range(len(self.iterable)-1):
#             elem = self.iterable[i]
#             pos = len(list(filter(lambda func: func(elem), self.funcs)))
#             neg = len(self.funcs) - pos
#             if self.judge(pos, neg):
#                 return elem
#             continue
#         raise StopIteration
#
#
#         # access = False
#         # while access:
#         #     elem = self.iterable[self.index]
#         #     pos = len(list(filter(lambda func: func(elem), self.funcs)))
#         #     neg = len(self.funcs) - pos
#         #     access = self.judge(pos, neg)
#         #     self.index += 1
#         #     if self.index >= len(self.iterable):
#         #         break
#         # if access:
#         #     return self.iterable[self.index-1]
#         # else:
#         #     raise StopIteration
#
#
#
#
#
#
#
# def mul2(x):
#     return x % 2 == 0
#
#
# def mul3(x):
#     return x % 3 == 0
#
#
# def mul5(x):
#     return x % 5 == 0
#
#
# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]
#
# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]
#
# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]



задача 2_3_5

# import itertools
# def primes():
#     result = 2
#     while True:
#         dividers = [d for d in range(1, result + 1) if result % d == 0]
#         if len(dividers) == 2:
#             yield result
#         result += 1
# 
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]



2_3_6 -----------------------------------------------------

Сиснтаксис для list comprehension

ls1 = [i * i for i in range(100)]
ls2 = [i * i for i in range(100) if i % 2 == 0]
ls3 = [(i, j) for i in range(10) for j in range(10) if i >= j]
"""