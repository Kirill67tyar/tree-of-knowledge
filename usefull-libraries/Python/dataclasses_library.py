"""
sources:
    https://docs.python.org/3/library/dataclasses.html
    https://habr.com/ru/post/415829/



Позволяет автоматизировать создание классов,
не прописывать __init__, __repr__, __str__ и возможно что-то ещё

Пример использования:

    from dataclasses import dataclass

    @dataclass
    class Point:
        x: int = 0
        y: int = 0

    point1 = Point(5,7)
    point2 = Point(-10, 12)
    point3 = Point()

    print(point1)  # Point(x=5, y=7)
    print(point2)  # Point(x=-10, y=12)
    print(point1.x)  # 5
    print(point1.y)  # 7

    # point3
    print(point3.x)  # 0
    print(point3.y)  # 0

Т.е. как видно, __init__ мы создали здесь автоматически,
и экземпляры тоде присвоились.
Единственное - прописали аннтоацию, для заданых атрибутов (обязательно)

По умолчанию можно определять можно не определять, как хочешь
Вообще читай habr



"""



