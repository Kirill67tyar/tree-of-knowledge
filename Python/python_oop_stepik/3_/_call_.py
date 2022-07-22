"""

благодаря методу __call__(self, *args, **kwargs) мы можем использовать экземпдяр как функцию

    class C:
        def __call__(self,  *args, **kwargs):
            return 5

    C()() # 5

__call__ - делает наш экземпляр функцией

    class C:
        def __call__(self, a, *args, **kwargs):
            return a ** 2

    C()(a=14) # 196


"""

# Декоратор через класс:

from time import time, perf_counter
from functools import wraps


# так
class Timer:
    def __init__(self):
        pass

    def __call__(self, func):
        def decor(*args, **kwargs):
            start = perf_counter()
            func(*args, **kwargs)
            return perf_counter() - start

        decor.__name__ = func.__name__
        decor.__doc__ = func.__doc__
        return decor


# или так
class Timer2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.func(*args, **kwargs)
        finish = perf_counter()
        print(f'{self.func.__name__} - {finish - start}')
        return result


if __name__ == '__main__':

    @Timer2
    def f(num):
        result = 0
        for i in range(num):
            result += i ** 2
        return result


    print(f(100000))
