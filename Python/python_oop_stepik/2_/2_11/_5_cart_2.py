"""

С предыдущего урока у вас должен быть создан класс  File, у которого имеется:

метод __init__
метод  restore_from_trash
метод  remove
метод read
метод write


Далее создайте класс  Trash у которого есть:

атрибут класса  content изначально равный пустому списку

статик-метод  add, который принимает файл и сохраняет его в корзину:
для этого нужно добавить его в атрибут content и проставить файлу атрибут in_trash значение True.
Если в метод add передается не экземпляр класса File, необходимо вывести сообщение «В корзину добавлять можно только файл»

статик-метод  clear, который запускает процесс очистки файлов в корзине. Необходимо для всех файлов,
хранящийся в атрибуте content , в порядке их добавления в корзину вызвать метод файла remove.
Атрибут content  после очистки должен стать пустым списком.
Сама процедура очистки должна начинаться фразой «Очищаем корзину» и заканчиваться фразой «Корзина пуста»

статик-метод  restore, который запускает процесс восстановления файлов из корзины.
Необходимо для всех файлов, хранящийся в атрибуте content ,
в порядке их добавления в корзину вызвать метод файла restore_from_trash.
Атрибут content  после очистки должен стать пустым списком.
Сама процедура восстановления должна начинаться фразой «Восстанавливаем файлы из корзины» и заканчиваться фразой «Корзина пуста»
Пример работы с классом Trash

f1 = File('puppies.jpg')
f2 = File('cat.jpg')
passwords = File('pass.txt')

f1.read() # Прочитали все содержимое файла puppies.jpg
Trash.add(f1)
f1.read() # ErrorReadFileTrashed(puppies.jpg)

Trash.add(f2)
Trash.add(passwords)
Trash.clear() # после этой команды вывод должен быть таким
'''
Очищаем корзину
Файл puppies.jpg был удален
Файл cat.jpg был удален
Файл pass.txt был удален
Корзина пуста
'''

f1.read() # ErrorReadFileTrashed(puppies.jpg)
Определение класса File  тоже нужно вставить в редактор кода
"""


class File:

    def __init__(self, name):
        self.name = name
        self.is_deleted = False
        self.in_trash = False

    def restore_from_trash(self):
        print(f"Файл {self.name} восстановлен из корзины")
        self.in_trash = False

    def remove(self):
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def read(self):
        if self.is_deleted:
            return print(f'ErrorReadFileDeleted({self.name})')
        elif self.in_trash:
            return print(f'ErrorReadFileTrashed({self.name})')
        print(f'Прочитали все содержимое файла {self.name}')

    def write(self, content):
        if self.is_deleted:
            return print(f'ErrorWriteFileDeleted({self.name})')
        elif self.in_trash:
            return print(f'ErrorWriteFileTrashed({self.name})')
        print(f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file):
        if isinstance(file, File):
            file.in_trash = True
            Trash.content.append(file)
        else:
            print('В корзину добавлять можно только файл')

    @staticmethod
    def clear():
        print('Очищаем корзину')
        for file in Trash.content:
            file.remove()
        Trash.content.clear()
        print('Корзина пуста')

    @staticmethod
    def restore():
        print('Восстанавливаем файлы из корзины')
        for file in Trash.content:
            file.restore_from_trash()
        Trash.content.clear()
        print('Корзина пуста')


if __name__ == '__main__':
    f1 = File('puppies.jpg')
    f2 = File('cat.jpg')
    passwords = File('pass.txt')

    f1.read()  # Прочитали все содержимое файла puppies.jpg
    Trash.add(f1)
    f1.read()  # ErrorReadFileTrashed(puppies.jpg)

    Trash.add(f2)
    Trash.add(passwords)
    Trash.clear()  # после этой команды вывод должен быть таким
    '''
    Очищаем корзину
    Файл puppies.jpg был удален
    Файл cat.jpg был удален
    Файл pass.txt был удален
    Корзина пуста
    '''

    f1.read()  # ErrorReadFileTrashed(puppies.jpg)
