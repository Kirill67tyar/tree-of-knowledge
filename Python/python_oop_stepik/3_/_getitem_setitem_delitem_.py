"""

__getitem__(self, item) - добавляет обращение по индексу или ключу
__setitem__(self, key, value) - добавляет присваивание по индексу или ключу новое значение - ls[1] = 'some_object'
__delitem__(self, key) - добавляет удаление по индексу или ключу

все принимают аргументы - (self, item)


"""


class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __str__(self):
        return str(self.values)

    def __repr__(self):
        return str(self.values)

    def get_obj(self, item):
        if 0 <= item < len(self.values):
            return True
        else:
            item = len(self.values) + item
            if 0 <= item < len(self.values):
                return True

    def __getitem__(self, item):
        if self.get_obj(item):
            return self.values[item]
        else:
            raise IndexError('Index out of range, таа-шаа')

    def __setitem__(self, key, value):
        if self.get_obj(key):
            self.values[key] = value

        # # --- для разряженного массива ---
        # elif key > len(self.values) - 1:
        #     difference = key - (len(self.values) - 1)
        #     if difference == 1:
        #         self.values.append(0)
        #         self.values[key] = value
        #     else:
        #         self.values.extend([0] * difference)
        #         self.values[key] = value
        # # --- для разряженного массива ---

        else:
            raise IndexError('Index out of range, таа-шаа')

    def __delitem__(self, key):
        if self.get_obj(key):
            del self.values[key]
        else:
            raise IndexError('Index out of range, таа-шаа')


if __name__ == '__main__':
    v = Vector(3, 21, 4, 6, 4)
    v[5] = 'qwe'
    v[15] = 'qwe12123123'
    print(v)

"""
v = Vector(3,21,4,6,4)
"""
