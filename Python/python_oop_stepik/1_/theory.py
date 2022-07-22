"""

sources:
    getattr hasattr setattr delattr
    https://russianblogs.com/article/45011841864/
    https://medium.com/@pranaygore/using-getattr-setattr-delattr-hasattr-in-python-6d79c6f9fda3


-------- черепашки ниндзя - getattr, setattr, hasattr, delattr -----------------
# getattr(Cls, 'attr'[, default]) # value of attr | default | AttributeError
# setattr(Cls, 'attr', value) # None
# hasattr(Cls, 'attr') # True or False
# delattr(Cls, 'attr') # None or AttributeError if attr not being


1) при добавлении/изменении/удалении атрибута класса
   атрибут в его экземплярах также изменится динамически
   в обратную сторону это не работает

    class C:
        pass

    c = C()
    cc = C()
    C.attr = 'qwerty'
    c.attr # 'qwerty'
    cc.attr # 'qwerty'


1.4-----------------------------------------------------------------------------------------------------------------1.3



























1.4-----------------------------------------------------------------------------------------------------------------1.4















































"""


