"""
sources:
    видео
    https://stepik.org/lesson/682557/step/1?unit=681369

    текст
    https://stepik.org/lesson/682557/step/2?unit=681369


Короче в этом видео полиморфизм про то, что методы надо называть универсальными наименованиями

Допустим для класса Square, Rectangle, Circle - метод кототрый вычисляет площадь назвать - area
А не как то разному (get_circle_area, get_square_area и тд)

Чтобы мы с этим объектом работали одинаково, но при этом каждый объект вёл себя по разному.

Итого:
    Полиморфизм - возможность обработки разных объектов
    путём использования одного и того же метода по названию

Разумеется магические методы отлично обеспечивают полиморфное поведение
"""