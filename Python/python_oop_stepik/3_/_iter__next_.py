"""
Бесконечный итератор
Иногда мы хотим, чтобы наш итератор продолжал работать, пока не будет выполнено определенное условие. Но если мы неправильно определим условие, то столкнемся с бесконечным итератором, который никогда не закончится. Следовательно, при работе с такими итераторами необходимо проявлять особую осторожность.

Давайте разберем такой итератор, и поможет нам вновь встроенная функция iter.

help(iter)
Help on built-in function iter in module builtins:
iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    In the second form, the callable is called until it returns the sentinel.
Документация говорит, что функция iter может быть вызвана от двух аргументов:

callable - вызываемый объект
sentinel - значение, обозначающее конец последовательности
Функция iter будет каждый раз вызывать объект callable и сравнивает его со вторым аргумент sentinel. Как только они совпадут, будет исключение StopIteration

В качестве вызываемого объекта мы можем выбрать выражение int()

int() # возвращает 0
Используем это выражение в итераторе

>>> int()
0
>>> inf_iter = iter(int, 999)
>>> next(inf_iter)
0
>>> next(inf_iter)
0
При каждом вызове next будет вызываться int(), который постоянно возвращает 0, а 0 никогда не равен значению 999. Отсюда получаем бесконечный итератор.

Но если в качестве второго аргумента передадим 0, то сразу получим StopIteration, так как значения совпадут

>>> not_inf = iter(int, 0)
>>> next(not_inf)
Traceback (most recent call last):
  File "C:\Python3.9\lib\site-packages\IPython\core\interactiveshell.py", line 3457, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-17-3ca409f2299a>", line 1, in <module>
    next(not_inf)
StopIteration

"""