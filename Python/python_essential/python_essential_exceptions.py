"""
-------------------------------------------------- Исключения --------------------------------------------------

sources:
    https://ru.hexlet.io/courses/advanced_python/lessons/python_exceptions/theory_unit
    https://ozlib.com/859841/informatika/apparat_isklyucheniy
    https://docs.python.org/3/tutorial/errors.html


------------------------------------------------------------------------------------------
try:                        # область действия обработчика
    ...

except Exceptions1:         # обработчик исключения Exceptions1
    ...

except MoreBaseException:   # обработчик исключения MoreBaseException
    ...

except:                     # стандартный обработчик except (отлавливает BaseExceptions)
    ...

else:                       # код который выполняется если никакое исключение не возникло
    ...

finally:                    # код который выполняется в любом случае
    ...

Главное помни:

1 - при try/except интерпретатор работает медленне, но всё равно довольно быстро
2 - количество строк в блоке try нужно свести к минимуму, только то, что может вызвать ошибку.
для остального есть else
3 - мы отлавливаем экземпляры исключений, которые возникают,
и можем присвоить их переменной с помощью оператора as
4 - нужно пытаться отловить более частные ошибки, и только потом более общие.
5 - стандартный обработчик except без указания ошибки - поймает любую. после него не могут быть другие exception
6 - исключение будет поймано ближайшим внешним блоком try/except в которм есть соответствующий обработчик
7 - else будет выполняться если не один except не сработал и ошибки не было
8 - finally будет выполняться в любом случае, даже если ошибка возникла и её не удалось словить.
(допустима форма try/finally)
------------------------------------------------------------------------------------------



оператор raise принимает как объект исключения, так и класс.
И если передать в rise класс исключения, то автомтически создастся объект соответствующего класса
причём вызывается конструктор с пустым списком аргументов
Если мы создаём объект исключения, то соответственно можно указать там свои данные

raise ValidationError('повремени мгновение, пока не схлопотал')

try:
    5 / 0
except ZeroDivisionError as err:
    print(err) # division by zero
    print(type(err)) # <class 'ZeroDivisionError'>
    print(type(err).mro()) # [<class 'ZeroDivisionError'>, <class 'ArithmeticError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
    print(isinstance(err, ArithmeticError)) # True


Шаблон try/except:

try:
    ..do something dangerous..

except ZeroDivisionError:
    ..do something..

except ArithmeticError:
    ..do something..

else:
    ..if there were not exceptions..

finally:
    ..will do it anyway..


*** try

интерпретатор ползёт медленно вниз, т.к. try/except замедляет работу интерпретатора
сначала что-то пытаемся делать в блоке команды try. Если в try было выброшено исключение,
выполнение кода в блоке try останавливается и управление переходит обработчикам except

Количество строк внутри блока try желательно свести к минимуму.
Желательно писать только то - что как ожидается может вызвать ошибку
для этого есть else в try/except

Только то, что ты ожидаешь выдаст ошибку - нужно поместить в блок try

Иначе можно случайно перехватить не то исключение, которое ты хочешь.

Иногда конструкция try/except используется не просто для отладки,
но и как неотъемлемая часть готовой программы.
Для специально потенциально заготовленных ошибок.
А если except перехватывает, то что мы не ожидали, то это уже баг в коде
а с багами нужно бороться.



*** except

нужно идти от более частных ошибок к более общим
если в операторе except не указать ошибку он будет отлавливать саму общую - BaseException

try:
    pass
except Exception1:                      # Обработчик исключения Exception1
    pass
except (Exception2, Exception3):        # Обработчик исключений Exception2 и Exception3
    pass
except Exception4 as exp:               # Обработчик исключения Exception4
    pass                                  экземпляр исключения доступен под именем exp
except:                                 # Стандарный обработчик, перехватывает все ислючения
    pass

что происходит например при
except ZeroDivisionError?
python проверяет, что объект исключения, который возник - являеятся экземпляром класса ZeroDivisionError
оно как будто применяет команду isinstance(ex, ZeroDivisionError)
Именно так и работает обработчик except
И далее, если мы запишем так:
except ZeroDivisionError as err
python сохранит экземпляр этого исклчения в переменной err

Блоки except обрабатываются сверху вниз и управление передаётся не больше, чем одному обработчику.
Поэтому, при необходимости, нужно по разному обрабатывать исключения, находящиеся в иерархии наследования,
сначала нужно указывать обработчики менее общих исключений, а затем - более общих. Также именно
поэтому стандарный блок except может быть только последним.

если except может отловить нужную ошибку - он её отловит, не важно сколько
раз был завёрнута конструкция try/except внутрь try для этого except
разумеется, если ошибка за блоком try/except то except её не отловит.
Если исключение возникло в конструкции try/except
не важно, как глубоко оно находится - except (если он для этого исключения) он его поймает
Иначе говоря исключение будет поймано ближайшим внешним блоком try/except:

try:
    try:
        5/0 # ZeroDivisionError

    except AttributeError:
        print('we catch AttributeError error')

except ZeroDivisionError:
    print('we catch ZeroDivisionError error')



print('start calculating')
try:
    a = float(input('a = '))
    b = float(input('b = '))
    print(a / b)
except (ZeroDivisionError, ValueError) as err:
    print(err)

print('stop calculating')




# def main():
#     while 1:
#         try:
#             a = float(input('a = '))
#             b = float(input('b = '))
#             print('Result: ', a / b)
#             break
#         except (ZeroDivisionError, ValueError) as err:
#             print(err)
#             print('Please try again:')
# if __name__ == '__main__':
#     main()


Если же программа не перехватывает исключение вообще, то интепретатор завершает выполнение программы
и выводит инфу об исключении в стандартный поток ошибок sys.stderr.
Из этого правила есть два исключения:

- Если исключение возникло в деструкторе объекта, выполенение программы не завершается,
  а в стандартный поток ошибок выводится предупреждение "Exception ignored"
  с информацией об исключении.
- При возникновении исключения SystemExit происходит только завершение программы без вывода информации
  об исключении на экран ( не касается предыдущего пункта, в деструкторе поведение данного исключения
  будет таким же, как и остальных)


*** else

в блок else мы завернём если никакое исключение не возникло

Предназначен по сути для внешней конструкции try/except
чтобы свести к минимуму количество строк в блоке try.

Вообще он нужен для того, чтобы свести к минимуму количество строк в блоке try

Количество строк внутри блока try желательно свести к минимуму.
Желательно писать только то - что как ожидается может вызвать ошибку
для этого есть else в try/except


*** finally

Предназначен для выполнения cleanup actions, т.е. действий по очистке:
- закрытие файлов
- удаление временных объектов

Если исключение не было перехвачено ни одним из блоков except,
то оно заново выбрасывается интерпретатором после выполнения действий в блоке finally

блок finally выполняется перед выходом из оператора try/except всегда,
даже если одна из его веток содержит оператор return (когда оператор try/except находится внутри функции),
break или continue (когда оператор try/except находится внутри цикла) или возникло другое необработанное
исключение при обработке данного исключения. Даже SystemExit не остановит finally

python гарантирует, что операторы внутри этого блока будут выполнены

хотя в принципе с этой работой также не плохо справляется менеджер контекста with
(базируется на том же механизме, что и finally)

Даже если ошибка была не отловлена finally всё равно выполнится
    try:
        3 / 0
    except ValueError:
        print('this is not Value Error')

    finally:
        a = 5 ** 2
        print('this is from finally', a)


перед вызовом SystemExit finally отработает (хотя стоит после):

    a = 5
    b = 0

    try:
        5 / 0
    except ZeroDivisionError as err:
        raise SystemExit('какая-то переменная не корректна')
    finally:
        print('finally work')

Можно сделать вывод что у finally, когда интерпретатор построчно доходит до него
очень высокий приоритет

И если он есть в python то он выполнится.

Даже SyntaxError ему не по чём:

    try:
        raise SyntaxError('какая-то переменная не корректна')
    finally:
        print('finally work')


return и break тоже не остановят finally

    def f():
        try:
            return
        finally:
            print('finally work')

    f()

И SystemExit тоже

    try:
        raise SystemExit
    finally:
        print('finally worked')
    print('after construction try/except')

*** Exceptions

ZeroDivisionError.mro()
    [<class 'ZeroDivisionError'>,
    <class 'ArithmeticError'>,
    <class 'Exception'>,
    <class 'BaseException'>,
    <class 'object'>]

В ошибках сохранены сообщения об ошибках
попробуй:
>>> 5 / 0
ZeroDivisionError: division by zero

>>> raise ZeroDivisionError('это была ошибка')
ZeroDivisionError: это была ошибка

При вызове ошибки с помощью raise мы можем перезаписывать эти сообщения


SystemExit

Это исключение вызывается, всякий раз когда работа программы завершается.
Разумеется не выводится на экран
raise SystemExit

Попробуй
print('das')
raise SystemExit('good bye')
print('asda')



Деструктор.
Вызывается, когда python будет удалять объект из памяти.

class Myobj:

    def __del__(self):
        print(self, 'is about to be deleted')

ob = Myobj()

del ob # <__main__.Myobj object at 0x000001FF5C2A3FD0> is about to be deleted

Так вот, если в этом методе произойдёт исключение, то оно будет проигнорировано

На примере ниже видно, что вызов ошибки в деструкторе
не остановил работу программы

# class Myobj:
#
#     def __del__(self):
#         print(self, 'is about to be deleted')
#         raise Exception
#         # raise SyntaxError # или эту возови
#
#
# print('Creating object...')
# ob = Myobj()
#
# print('Deleting reference...')
# del ob
#
# print('Done')


Базовые исключения:

- BaseException - базовый класс для всех исключений
- Exception - базовый класс для всех стандартных исключений, которые
не указывают на обязательное заверщение
- ArithmeticError - базовый класс для всех исключений, связанных с арифмитическими операциями
- BufferError - базовый класс для всех исключений, связанных с операциями над буфером
- LookupError - базовый класс для всех исключений, связанных с неверным ключом
или индексом коллекции


*** SyntaxError

SyntaxError возникает, когда синтакический анализатор Python сталкивается с участком кода,
который не соответствует спецификации языка и не может быть интерпретирован

В главном модуле возникает до начала выполнения программы и не может быть перехвачен

Ситуации, в которых синтаксическая ошибка в виде исключения SyntaxError
может быть перехвачена и обработана:

    ошибка синтаксиса в импортируемом модуле
    ошибка синтаксиса в коде, который представляется строкой и передаётся функцией eval и exec

Также блок finally отработает несмотря на то, что мы мыкинем SyntaxError
И при вызове в деструкторе объекта, при его удалении, она тоже не остановит
выполнение кода интерпретатором

Очень часто SyntaxError ставят особняком, но это тоже исключение
которое заимствуется в BaseException:

    print(type(SyntaxError))
    print(SyntaxError)
    print(SyntaxError.mro())
    # [<class 'SyntaxError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]
    # raise SyntaxError

Просто перехватить его нельзя, и вызывается до начала выполнения программы



*** Warning

print(Warning.mro())
[<class 'Warning'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>]

print(UserWarning)
print(UserWarning.mro())

<class 'UserWarning'>
[<class 'UserWarning'>, <class 'Warning'>,
 <class 'Exception'>, <class 'BaseException'>,
 <class 'object'>]

Есть ещё модель warnings

import warnings

__all__ = ["warn", "warn_explicit", "showwarning",
           "formatwarning", "filterwarnings", "simplefilter",
           "resetwarnings", "catch_warnings"]

Запомни:
- вызывается функцией warn из warnings
- После предупреждения, интерпретатор продолжает работу дальше

    import warnings

    warnings.warn('Ты чё, охуел')

    print('werwerwer')


*** Связывание исключений

Попробуй:

    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        raise ValueError

Несмотря на то, что ZeroDivisionError мы словили, мы видим и о нём информацию тоже:

    Traceback (most recent call last):
      File "C:\Users\kiril\Desktop\Job\tree-of-knowledge\Python\python_essential\practice.py", line 2, in <module>
        raise ZeroDivisionError
    ZeroDivisionError

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Users\kiril\Desktop\Job\tree-of-knowledge\Python\python_essential\practice.py", line 4, in <module>
        raise ValueError
    ValueError

Как реализовано то, что мы видим инфу об изначальном исключении, которое мы отловили,
а потом об исключении, которое мы сами вызвали (или оно возникло)

Это реализовано с помощью такого атрибута данных, как __context__

err = ValueError()
print(err.__context__) # None
err.__context__ = ZeroDivisionError()
print(err.__context__) # вообще ничего
print(type(err.__context__)) # <class 'ZeroDivisionError'>
raise err # вызовет ValueError, но также упомянет об ZeroDivisionError

а точнее, что при обработке ZeroDivisionError возник ValueError

Работает это так, если мы ловим в except какое-либо исключение,
то оно помещается в атрибут данных __context__ исключения,
которое возникло в блоке кода обработчика.
Если ты вышел из конструкции try/except то это связывание прерывается

    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        print('dasda')

    raise ValueError


будет просто:
    Traceback (most recent call last):
      File "C:\Users\kiril\Desktop\Job\tree-of-knowledge\Python\python_essential\practice.py", line 6, in <module>
        raise ValueError
    ValueError

Это конечно здорово, но "после" не значит "из-за"
А как быть если нужно узнать, из-за какого исключения вызвалось это исключение.
Для этого есть атрибут данных __cause__

    err = ValueError()
    print(err.__cause__)
    err.__cause__ = ZeroDivisionError()
    print(err.__cause__)

    raise err

Выдаст:

    ZeroDivisionError

    The above exception was the direct cause of the following exception:

    Traceback (most recent call last):
      File "C:\Users\kiril\Desktop\Job\tree-of-knowledge\Python\python_essential\practice.py", line 13, in <module>
        raise err
    ValueError


правильно делается это так:

    raise ValueError from ZeroDivisionError

Пример:

    a = 5
    b = 0

    try:
        5 / 0
    except ZeroDivisionError as err:
        raise ValueError('какая-то переменная не корректна') from err

Таким образом мы можем замещать одни исключения другими, которые
будут более подходить нам с логической точки зрения
Или будут соответствовать какому-то интерфейсу, который мы задаём для наших функций
Но при этом сохранять инфу об изначальных исключениях

Ну а если нужно полностью заменить старое исключение новым, без привязки,
то делается это так:

    raise ValueError('какая-то переменная не корректна') from None


*** EAFP vs LBYL

sources:
    https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/

LBYL - Look Before You Leap - "семь раз отмерь, один раз отреж"
EAFP - Easy to Ask for Forgiveness than Permission - "Проще попросить прощения, чем разрешения"


EAFP в python предпочтительнее

это значит, что try/except можно использовать почаще, как часть кода

try/except в python работает довольно быстро


Такие две проверки существуют для динамических языков,
для статических всё немного не так



Как работает память в python

class Myobj:

    def __del__(self):
        print(self, 'is about to be deleted')

ob = Myobj()

del ob # <__main__.Myobj object at 0x000001FF5C2A3FD0> is about to be deleted

В python авоматическое управление памятью
В python все объекты создаются динамически. Потому что все типы данных
являются ссылочными
Объект размещается в такой специальной области памяти, который называется heap (куча)

Любая переменная в python это ссылка на id объекта в памяти

id объекта - это адрес в памяти

Для любого объекта, который мы или python создаём - ведётся интерпретатором подсчёт ссылок

любая переменная - это ссылка на объект. Пока есть переменная - есть и объект в памяти
как только на какой-то объект не останется больше ссылок - в следующем цикле сборки мусора
python удалит этот объект

Ну алгоритм сборки мусора вообще конечно сложнее.

Пока ссылки на объект есть - он живёт. Как только ссылок не останется - python
попытается как можно скорее удалить его из оперативной памяти.

Когда python собирается удалить объект из памяти - он вызывает метод __del__,
если он в нём описан.
"""


