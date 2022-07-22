"""
sources:
    https://pypi.org/project/redis/
    https://redis.readthedocs.io/en/latest/

    использование на практике
    https://github.com/Kirill67tyar/bookmarks/blob/master/images/views.py#L32

!!! Сервер Redis должен быть включён, в PowerShell ввести redis-server



>>> import redis
>>> r = redis.Redis(host='127.0.0.1', port=6379, db=0) # создаём соединение с базой данных Redis
                                                    # собственно с этим объектом мы и работаем дальше
>>> r.set('name', 'Kirill') # True

>>> r.get('name') # b'Kirill'

>>> p_dir(r) # очень длинный список методов и атрибутов
>>> p_mro(r) # очень длинный список классов-предков
>>> p_type(r)

incr - увеличивает ключ на один, и возвращает итоговое значение.
если ключа не было - создаёт его
>>> r.incr('some_key')
1
>>> r.incr('some_key')
2
>>> r.incr('some_key')
3


Два класса для доступа к Redis:
1. StrictRedis
2. Redis - расширение класса StrictRedis переопределяет некоторые совместимости


--- Ключ
    Есть негласное соглашение использовать : как резделитель между частями ключа


Методы:

incr - увеличивает ключ на один, и возвращает итоговое значение.
если ключа не было - создаёт его
>>> r.incr('some_key')
1
>>> r.incr('some_key')
2
>>> r.incr('some_key')
3


Ранжирование с помощью redis

zincrby и zrange - работают с набором (set, не путать с питоновским set)
набор или set - это коллекция неповторяющихся строк, каждая из которых имеет свой рейтинг
это как если был бы словарь, где значением был бы рейтинг,
а мы получали только ключи отсортированные по убыванию или возврастанию

>>> r.zincrby('image_ranking2', 1, 1) # image_ranking2 = {1: 1}
1.0
>>> r.zincrby('image_ranking2', 1, 1) # image_ranking2[1] += 1
2.0
>>> r.zrange('image_ranking2', 0, -1, desc=True) # ls = list(image_ranking2.keys())) ls.sort(key=lambda x: image_ranking2[x]) ls.reverse()
[b'1']
>>> r.zincrby('image_ranking2', 2, 1) # image_ranking2[1] += 2
4.0
>>> r.zincrby('image_ranking2', 1, 2) # image_ranking2[2] = 1
1.0
>>> r.zrange('image_ranking2', 0, -1, desc=True) # предоставляет отсортированный по возврастанию список
                                                # увеличенный с помощью zincrby
[b'1', b'2'] # это значение того что мы увеличивали в третьем аргументе zincrby('image_ranking2', 1, 2)

>>> r.zincrby('image_ranking2', 1, 'some_value') # image_ranking2['some_value'] = 1
1.0
>>>
>>> r.zincrby('image_ranking2', 1, 'some_value') # image_ranking2['some_value'] += 1
2.0
>>> r.zrange('image_ranking2', 0, -1, desc=True) # ls = list(image_ranking2.keys())) ls.sort(key=lambda x: image_ranking2[x]) ls.reverse()
[b'1', b'some_value', b'2']

--- zincrby
zincrby(
    self,
    name: KeyT,
    amount: float, # на какой рейтинг увиличивать
    value: EncodableT # какое значение увеличивать
    ) -> ResponseT

по анологии с python:
    image_ranking2 = {1: 1}
    image_ranking2[1] += 1
    image_ranking2[some_value] = 1
    image_ranking2[some_value] += 1

--- zrange
zrange - выдаёт отсортированный список того, что мы сохраняли

zrange(
        self,
        name: KeyT,
        start: int,
        end: int,
        desc: bool = False,         # сортировка в убывающем порядке
        withscores: bool = False,
        score_cast_func: Union[type, Callable] = float,
        byscore: bool = False,
        bylex: bool = False,
        offset: int = None,
        num: int = None,
    ) -> ResponseT



--- zunionstore

1. принимает ключ-dest (можно придумать новый ключ)
2. принимает спиок из ключей-keys (эти ключи должны быть хранилище Redis и за ними должны быть закреплены множества)
3. присваивает ключу dest множество из агрегированных данных прошлого множества

redis_db.zunionstore(  # аггрегирует значения переданных ключей и складывает их
                dest=tmp_key,
                keys=product_redis_keys,
            )
def zunionstore(
        self,
        dest: KeyT,
        keys: Union[Sequence[KeyT], Mapping[AnyKeyT, float]],
        aggregate: Union[str, None] = None,
    ) -> ResponseT:

zunionstore на практике
https://github.com/Kirill67tyar/shop/blob/master/store/recommenders.py#L63

doc
https://redis.io/commands/zunionstore/
https://redis.readthedocs.io/en/latest/commands.html#redis.commands.core.CoreCommands.zunionstore


--- zrem

zrem - удаляет из множества Redis элементы, которые мы передали

1. name - это ключ существующего множества (some_key:<some number>)
2. *values - эдементы этого множества которые ты хочешь из него убрать
3. в итоге удаляет эти элементы, из этого множества, если они есть, если их нет - ничего не происходит

zrem(self, name: KeyT, *values: FieldT) -> ResponseT:

zrem на практике
https://github.com/Kirill67tyar/shop/blob/master/store/recommenders.py#L67

doc
https://redis.io/commands/zrem/
https://redis.readthedocs.io/en/latest/commands.html#redis.commands.core.CoreCommands.zrem



https://github.com/Kirill67tyar/shop/blob/master/store/recommenders.py

конфигурация для Django
# ------- конфигурация Redis с Django
# REDIS_HOST = 'localhost' # 127.0.0.1 | some_pro_host.ru
# REDIS_PORT = 6379
# REDIS_DB = 0



"""
from pprint import pprint as pp
