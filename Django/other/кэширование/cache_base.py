"""
---------------------------------------------------------------------------------------------

sources:
    https://docs.djangoproject.com/en/4.0/topics/cache/

    у меня
    https://github.com/Kirill67tyar/education-service/blob/master/src/courses/draft.py#L323

    что такое кэш на сервере
    https://docsvision.com/ecm-bpm/functional/server-components/cash/

    django-book (Меле Антонио) - 363 стр.

    memcached habr
    https://habr.com/ru/post/42607/

    также установка на windows
    https://russianblogs.com/article/14531620805/

                                Кеширование в django

Кэш - Специальная область на диске или в операционной памяти компьютера,
предназначенная для временного хранения информации и для часто используемых данных и команд.

https://docs.djangoproject.com/en/3.2/topics/cache/

Работа подсистемы кеширования при обработке HTTP-запроса:
1) пытается найти запрошиваемые данных в кеше;
2) если это удалось - возвращает ответ;
3) если данные не нашлись - выполняет такие шаги:
    -- делает запрос в бд и/или вычисления, в соответствии с логикой обработчика,
    -- сохраняет результат в кеш,
    -- возвращает данные в HTTP-ответе.

Доступные бэкэнды кеширования:

1) -- backends.memcached.MemcachedCache, или backends.memcached.PyLibMCCache
    import:
    from django.core.cache.backends.memcached import MemcachedCache, PyLibMCCache
    https://memcached.org/
    https://github.com/memcached/memcached/wiki/ReleaseNotes169
    https://ru.wikipedia.org/wiki/Memcached
    а также гугли Memcached в google
    MemcachedCache и PyLibMCCache - бэкэнды для Memcached. Это быстрая и эффективная система кеширования
    работающая с оперативной памятью. Какой именно из классов использовать - зависит от того,
    как настроить взаимодействие Memcached с python кодом.
    Предоставляет хорошую производительность. Используется чаще всего
2) -- backends.db.DatabaseCache
    import:
    from django.core.cache.backends.db import DatabaseCache
    использует в качестве хранилища кешей - базу данных
3) -- backends.filebased.FileBasedCache
    import:
    from django.core.cache.backends.filebased import FileBasedCache
    Сохраняет результаты в файловую систему, сериализует, и хранит каждое кешируемое значение
    в отдельном файле.
    Настройка в settings.py выглядит так:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
        }
    }
4) -- backends.locmem.LocMemCache
    import:
    from django.core.cache.backends.locmem import LocMemCache
    Бэкэнд для кеширования в памяти. Используется по умолчанию
5) -- backends.dummy.DummyCache
    import:
    from django.core.cache.backends.dummy import DummyCache
    Фиктивный бэкэнд кеширования, применяемый только при разработке.
    Он реализует бэкэнд кеширования, но не сохраняет никакие результаты.


************** Memcached
    https://habr.com/ru/post/42607/
    Это приложение при запуске полуает от операционной системы заданный в настройках
    объем оперативной памяти для кеширования. Как только место в памяти заканчивается
    memcached перезаписывает старые записи.

    Порт для Memcached - 11211
    Но можно задать любой другой порт.
    Раз есть порт, то скорее представляет из себя какой-то сервер.
    (но не совсем, вообще-то программы взаимодействуют с сервером через порты,
    и не обязательно эти программы - серверы)

    Требует установки Memcached,
    а также библиотеку python-memcached для взаимодействия с Memcached из python кода

    Установка Memcached на Windows 10:
    https://stackoverflow.com/questions/59476616/install-memcached-on-windows
    https://static.runoob.com/download/memcached-win64-1.4.4-14.zip   - адрес ссылки
    Steps to install Memcached on Windows:
    1 - Download a stable version, in either 32-bit or 64-bit I have tested the 64-bit version.
    2 - Unzip it in some hard drive folder. For example C:\memcached
    3 - There will be memcached.exe file in the unzipped folder.
    4 - Open a command prompt (need to be opened as administrator).
    5 - Run c:\memcached\memcached.exe -d install   (не забывай, что нужно подставить путь, куда ты зазархивировал
                                                                скачанный файл)
    For start and stop run following command line
    c:\memcached\memcached.exe -d start
    c:\memcached\memcached.exe -d stop

    python-memcached:
    pip install python-memcached
    https://pypi.org/project/python-memcached/
    https://github.com/linsomniac/python-memcached
    https://launchpad.net/python-memcached
    Так как Memcached уже установлен, то запуск его следующий:
    1 - открываешь коноль как администратор.
    2 - заходишь по этому адресу C:\Program Files\memcached>
    3 - вводишь memcached.exe -d start (memcached.exe -d install если memcached не установлен)

    Для Memcached есть отличный инструмент для анализа ее работы через админку.
    django-memcache-status
    https://pypi.org/project/django-memcache-status/
    Это приложение собирает стату по каждомум рабочему приложению Memcached
    и отображает ее на сайте администрирования

    Минимальная установка:
    1) pip install django-memcache-status
    2) добавить в INSTALLED_APPS 'memcache_status',
    3) В любой admin.py файл добавить:
    admin.site.index_template = 'memcache_status/admin_index.html'

    какие поля предоставляет ?
    Curr Items	- количество объектов, которые находятся в кеше
    Get Hits	- показывает какое кол-во в кеш было произведено успешно
    Get Misses	- кол-во неудачных обращений к кешу
    Miss Ratio  - выводит результирующую оценку по параметрам Get Hits и Get Misses в процентах.


    mecached в settings.py:

    # -------------------------------------------------------- CACHES settings (for Memcached)
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',  # 11211 - port для Memcached по умолчанию.
        }
    }

    # # для кеширования всего сайта (отключить если надо)
    # CACHE_MIDDLEWARE_ALIAS = 'default'  # - псевдоним кеша
    # CACHE_MIDDLEWARE_SECONDS = 60 * 5  # 5 minutes
    # CACHE_MIDDLEWARE_KEY_PREFIX = 'educa'  # - префикс для всех ключей чтобы избежать пересечения
    # # при использовании одного рабочего процесса Memcached с несколькими проектами
    # -------------------------------------------------------- CACHES settings



************** Настройки кеширования в settings.py
    https://docs.djangoproject.com/en/3.2/ref/settings/#caches
    https://docs.djangoproject.com/en/4.0/ref/settings/#caches
    https://docs.djangoproject.com/en/4.0/topics/cache/#setting-up-the-cache
    CACHES - словарь используемый в проекте систем кеширования.
    Основная настройка для определения системы кеширования
    CACHE_MIDDLEWARE_ALIAS - псевдонимы кешей
    CACHE_MIDDLEWARE_KEY_PREFIX - префиксы для ключей кешей.
    Когда проект работает с несколькими сайтами, префиксы
    позволяют избежать коллизий имен ключей
    CACHE_MIDDLEWARE_SECONDS - продолжительность хранения кеширования страниц в секундах


************** CACHES
    По сути самая важная настройка для кеширования
    Подсистему кеширования проекта конфигурируют с помощью насройки CACHES
    Это словарь, который задает параметры конфигурации (ключи python) для каждого бэкэнда.
    Параметры для CACHES:
        BACKEND - используемый класс для бэкэнда
        LOCATION - расположение !результата кеширования. В зависимости от используемой системы кеширования
                    настройка может принимать значения в виде пути в файловой системе, хоста и порта или имени
                    для бэкэндов на основе оперативной памяти
        KEY_FUNCTION - функция для получения ключа кеша. Она принимает в качестве аргументов префикс,
                    версию и некоторый начальный ключ в виде строки. Затем преобразует их в ключ, используемый
                    для кеширования
        KEY_PREFIX - префикс для всех ключей бэкэнда
        OPTIONS - любые дополнительные параметры, которые может принимать конкретный класс бэкэнда
        TIMEOUT - время хранения результата кеширования в секундах. По умолчанию равна 300 с (5 минут)
                    Если установить None - срок хранения данных не будет ограничен
        VERSION - номер версии кеширования данных. Нужно для добавления версии для кеширования
                    так CACHES выглядит для FileBasedCache
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
            'LOCATION': os.path.join(BASE_DIR, 'django_cache'),
        }
    }
    а так для MemcachedCache (Memcached)
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
    Если используется несколько рабочих процессов Memcached,
    в настройке LOCATION нужно указать список их адресов.


************** Уровни кеширования

    Django поддерживает кеширование представленное на нескольких уровнях:
    -- низкоуровневое API - предоставляет возможноть кешировать наименьшую единицу вычислений
        (запросы или выисления)
    -- уровень обработчиков - кешируются резудбтаты обработки одного HTTP запроса
    -- уровень шаблонов - применяется для добавления в кеш результата генерации HTML шаблона
        и его фрагмента
    -- уровень сайта - кеширует весь сайт

    Кеширование на самом деле не такая простая тема, там есть что изучать.
    Нужно хорошо разбираться в механизмах кеширования, чтобы
    хорошо обдумать стратегию кеширования.
    Да, кеширование предполагает хорошо обдуманную стратегию.

    ++++++++++++++ Очень важные моменты:

    !!! Для начала необходимо оптимизировать наиболее дорогие с точки зрения вычислений
    запросы и операции. !!!

    !!! Следует избегать установления неограниченного срока хранения данных в кеше,
    так можно обезопасить себя от получения неактуальной информации !!!

    !!! Работа подсистемы кеширования при обработке HTTP-запроса:
    1) пытается найти запрошиваемые данных в кеше;
    2) если это удалось - возвращает ответ;
    3) если данные не нашлись - выполняет такие шаги:
        -- делает запрос в бд и/или вычисления, в соответствии с логикой обработчика,
        -- сохраняет результат в кеш,
        -- возвращает данные в HTTP-ответе.!!!
    +++++++++++++


************** низкоуровневое API кеширования
    from django.core.cache import cache
    cache.set(<key>, <value>, <timeout>)
    cache.get(<key>)
    > cache.set('music_band', 'Король и шут', 20)
    > cache.get('music_band')
    > 'Король и шут'
     # 20 секунд проходит
    > cache.get('music_band') # пусто
    > print(cache.get('music_band') # None
    Хороший пример низкоуровневого кеширования смотри в обработчике CourseListView (courses.views)
    !!!                                                                              !!!
        С низкоуровневым кэшированием связана одна очень неприятная вещь, а именно,
        если ты туда сохранил queryset с каким-то select_related,
        select_related туда не сохранится, и когда ты будешь делать итерировать
        этот queryset для каждой записи django будет делать запрос в базу данных
        Короче, запомни правило, если ты сохраняешь qs в кэш, то
        через этот qs ни в коем случае нельзя обращаться к другим, связанным таблицам
    !!!                                                                              !!!


************** кеширование шаблонов
    {% load cache %}
    {% cache 600 some_name some_value_from_context %}
    ...some tags and calculates...
    {% endcache %}
    Не очень понял кеширование шаблонов.
    У меня закешировались данные от одного курса к другому из-за этого
    cache - название тега
    600 - кол-во секунд
    some_name - непонятно что, и для чего
    some_value_from_context - какая-то переменная из контекста, но непонятно для чего.
    прочти 370 страницу


************** кеширование результата работы обработчиков (HTTP запросов)
    from django.views.decorators.cache import cache_page
    для добавления в кеш результатов HTTP запросов в django есть декоратор cache_page
    его можно наклеить как и на обработчик (если он функция конечно), так и на шаблон url и установить только время
    в качестве ключа будет использоваться url этого http запроса (который может меняться динамиески).
    смотри пример использования в students.urls/views.py
    вот эт кста удобно.
    и в этой библиотеке есть также функция never_cache


************** использование кеширования для сайта
    кеширование всего сайта - самый высокоуровневый способ кеширования.
    1) нужно добавить два промежуточных слоя:
    'django.middleware.cache.UpdateCacheMiddleware', и 'django.middleware.cache.FetchFromCacheMiddleware',
    между промежутоным слоем
    'django.middleware.common.CommonMiddleware',
    MIDDLEWARE = [
        ...
        'django.middleware.cache.UpdateCacheMiddleware',
        'django.middleware.common.CommonMiddleware', - уже есть в MIDDLEWARE
        'django.middleware.cache.FetchFromCacheMiddleware',
        ...
    ]

!!! Важно помнить:
промежуточные слои при запросе (HTTP request) выполняются в том порядке,
в котором расположены, а при ответе (HTTP response) - в обратном!
Поэтому порядок расположения имеет значение.
Далее для кеширования всего сайта нужно добавить три константы:
CACHE_MIDDLEWARE_ALIAS = 'default'# - псевдоним кеша
CACHE_MIDDLEWARE_SECONDS = 60 * 5  # 5 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'educa'# - префикс для всех ключей чтобы избежать пересечения
# при использовании одного рабочего процесса Memcached с несколькими проектами
Для платформы обучения такой вид кеша не очень подходит, т.к. инфа меняется динамически.
Такой вид кеша подходит для сайтов, где инфа меняется очень редко - в идеале
одностраничных статических сайтов.

И так, следующие моменты:
 1. нужно кешировать сначало дорогостоящие операции
 2. нужно грамотно выбирать время кеша. Если у нас какая-то ин-фа меняется
    очень редко, её надо закешировать надолго (к примеру категории товаров в магазине, header сайта и т.д.)
    если ин-фа меняется очень часто, то нужно грамотно продумать время.
 3. в идеале - если что-то можно кешировать - то это надо кешировать.
"""
