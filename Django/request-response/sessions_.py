"""
sourses:
    https://developer.mozilla.org/ru/docs/Web/HTTP/Session
    https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%81%D1%81%D0%B8%D1%8F_(%D0%B2%D0%B5%D0%B1-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0)
    https://codenamecrud.ru/ruby-on-rails/sessions-cookies-and-authentication


from django.contrib.sessions.middleware import SessionMiddleware
HTTP сессия
Так как HTTP — это клиент-серверный протокол, HTTP сессия состоит из трёх фаз:
Клиент устанавливает TCP соединения (или другое соединение, если не используется TCP транспорт).
Клиент отправляет запрос и ждёт ответа.
Сервер обрабатывает запрос и посылает ответ, в котором содержится код статуса и соответствующие данные.
Начиная с версии HTTP/1.1, после третьей фазы соединение не закрывается,
так как клиенту позволяется инициировать другой запрос. То есть, вторая и третья фазы могут повторяться.
Понятие "Сессий" основано на том, что состояние пользователя каким-то образом сохраняется,
когда он переходит с одной страницы на другую. Вспомните, что HTTP не сохраняет состояний,
поэтому только браузер или ваше приложение может "запомнить" то, что нужно запомнить.


---------------------------------------------------------------------------------------------------
Немного теории:

    заголвок запроса - Cookie
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie
        https://www.ietf.org/rfc/rfc2109.txt
        Браузер имеет встроенный механизм управления куками
        поэтому он автоматически определяет для каждого запроса
        те куки, которые должны быть отправлены (установлены были до этого при ответе сервра в заголовке Set-Cookie)
        вот как выглядит заголовок Cookie при запросе авторизованного пользователя на сервер Django

        'Cookie': 'csrftoken=UHXhP5CDb2ml7UsBI5SuZvSf2XRWS0TQLu3XsjWAQHHQqjMEcTJuiRCrChXCvhZW; '
               'sessionid=cxxakvlafv7eh2yehb3h908hc74uh599',

        Именно там передаётся сессионный ключ авторизованного пользователя
        Cookie также доступны в атрибуте request.COOKIES


    заголовок ответа - Set-Cookie
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie
        https://www.ietf.org/rfc/rfc2109.txt
        https://www.ietf.org/rfc/rfc2965.txt
        позволяет web-серверу установить сессию на клиенте
        Схема работы с куками:
            1) клиент отправляет логин - пароль (вход на сайт) (другие виды авторизации)
            2) web сервер проверяет авторизацию
            3) с помощью Set-Cookie при HTTP ответе сервер клиенту передаёт очень длинную строчку
               эта строчка и есть ключ сессии (устанавливаем её в Django с помощью login(request, user_instance))
            4) браузер запоминает эту строчку у себя в куках
            5) и возвращает эту строчку при каждом последующем запросе на этот сервер
               в заголовке Cookie, (сессионный ключ может протухнуть, и тогда всё по новой)
        по этому сессионному ключу web сервер может понять какой из пользователей к нему пришёл


                                    Django сессии

    !!!                                                                                         !!!
        Основное:
        1) сесси Django доступны в переменной request.session
        2) являются экземпляром класса <class 'django.contrib.sessions.backends.db.SessionStore'>
        3) доступны куча методов для работы с ними - p_dir(request.session) (смотри ниже)
        4) при этом ведёт себя как обчный словарь - request.session['key'] = 'value'; pprint(dict(request.session))
        5) почти как словарь. его измения сохранятся если выставить django.session.modified = True
        6) за сессии в django отвечает промежуточный слой в MIDDLEWARE - django.contrib.sessions.middleware.SessionMiddleware
        7) настройки сессий - https://docs.djangoproject.com/en/4.0/ref/settings/#sessions
           или читай ниже
        8) документация - https://docs.djangoproject.com/en/4.0/topics/http/sessions/
        9) request.session - представляет текущий сеанс. вот как выглядит словарь request.session
             {'_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
                 '_auth_user_hash': 'f79daa3fe9e21caed1e12961bd15f67748985bfc4f35512f30fdd89be74b3a13',
                 '_auth_user_id': '1'}
            А вот как request.COOKIES:
                {'csrftoken': 'UHXhP5CDb2ml7UsBI5SuZvSf2XRWS0TQLu3XsjWAQHHQqjMEcTJuiRCrChXCvhZW',
                 'sessionid': 'cxxakvlafv7eh2yehb3h908hc74uh599'}
        10) cookie же будут доступны в атрибуте request.COOKIES
        Вывод: request.session - несколько отдельная вещь от request.COOKIE
               Cookie - это то что передаётся в заголовке ответа Set-Cookie и запроса Cookie
               request.session это скорее какой-то внутренний механизм Django для сессий,
               где указан user_id, доступные бэкенды для аутентификации и ещё _auth_user_hash
               причём т.к. мы узнаём какой юзер к нам пришёл через Cookie
               то скорее всего этот словарь request.session создаётся динамически
               вспомни, что в бэкэнде аутентификации получаем юзера по id
               ! но это только предположения

            не всё понятно с django session. А именно:
            1 - где будет храниться эта корзина, если СКОРЕЕ ВСЕГО в куках при HTTP ответе её нет
            2 - что в итоге такое request.session, ведь это не тоже самое что и request.COOKIE
            3 - когда пользователь отвечает, в request.COOKIE нигде нет корзины, зато они есть в django.session
                каким образом поддерживается передача этой информации между клиентом и сервером
                по идеи должна быть в заголовках, но нигде в заголовке её не видно
            4 - по идеи вся инфа о работе с клиентом должна храниться где то в бд
                но я не нашёл, где в бд хранится вот эта вот инфа
                '_auth_user_hash': 'f79daa3fe9e21caed1e12961bd15f67748985bfc4f35512f30fdd89be74b3a13',
                ещё какая-то там была свзанная с CSRF токенами

         UPD: кстати, вспомнил, что ключи приработе с request.session обязательно должны быть str
              это потому что django работает с request.session как то через JSON
                  (Django использует формат JSON для сериализации данных сессии.
                  Поэтому важно, чтобы ключи были string)
              Что косвенно говорит о том, что это всё таки какой-то внутренний мезанизм
              в Django, не связанный, (во всяком случае напрямую) с HTTP запросами, ответами
              и вообще куками.

         UPD: пришло в голову - да скорее всего request.session - это отдельный механизм
              от куков. Скорее всего действительно это механизм, реализованный исключительно,
              на стороне django и не взаимодействует с клиентской частью (может только косвенно взаимодействует).
              отвечает за request.session приложение django.contrib.sessions
              Скорее всего эта сессия полностью сохраняется на стороне django
              а определяет django всю эту информацию с помощью _auth_user_id (ключ в request.session)
              т.е. какой юзер аутентифицирован. Скорее всего за юзером закрепляется информация
              А какой юзер django определяет уже с помощью обычных cookies
              Правда вопрос остаётся открытым, где Django хранит инфу об request.session
    !!!                                                                                         !!!
---------------------------------------------------------------------------------------------------


Все взаимодействия между браузерами и серверами осуществляются при помощи протокола HTTP,
который не сохраняет своё состояние (stateless). Данный факт означает, что сообщения между клиентом
и сервером являются полностью независимыми один от другого — то есть не существует какого-либо
представления "последовательности", или поведения в зависимости от предыдущих сообщений.
В результате, если вы хотите создать сайт который будет отслеживать взаимодействие с клиентом (браузером),
вам нужно реализовать это самостоятельно.
Сессии являются механизмом, который использует Django (да и весь остальной "Интернет")
для отслеживания "состояния" между сайтом и каким-либо браузером. Сессии позволяют вам хранить
произвольные данные браузера и получать их в тот момент, когда между данным браузером и сайтом
устанавливается соединение. Данные получаются и сохраняются в сессии при помощи соответствующего "ключа".
(Вспоминай сессионный ключ, который формируется функцией login(request, user)
В данном случае сессионный ключ формируется на стороне сервера, но хранится
я так понимаю на стороне браузера, и на сервере он тоже хранится - таблица django_session
Django использует куки (cookie), которые содержат специальный идентификатор сессии,
который выделяет среди остальных, каждый браузер и соответствующую сессию. Реальные данные сессии,
по умолчанию, хранятся в базе данных сайта (это более безопасно, чем сохранять данные в куки, где
они могут быть уязвимы для злоумышленников). Однако, у вас есть возможность настроить Django так,
чтобы сохранять данные сессий в других местах (кеше, файлах, "безопасных" куки). Но всё же хранение
по умолчанию (в бд) является хорошей и безопасной возможностью.

--- В базе данных django есть таблица django_session где три столбца:
    1) session_key
    2) session_data
    3) expire_date (истекает дата)
Именно в них сохраняется сессионный ключ
upd: но опять же это про Cookie а не про request.session
На стороне браузера сессионная инфа сохраняется в куках
В django за обработку и установку куков для каждого запроса отвечает
промежутоный слой в MIDDLEWARE - django.contrib.sessions.middleware.SessionMiddleware
это проежуточный слой для управления сессиями
каждый HTTP request и response проходит через middleware
Благодаря middleware на доступны сессии в экземпляре запроса request - request.session
(управляет обработкой и установкой куков для каждого запроса)

request.session.keys():
dict_keys(['_auth_user_id', '_auth_user_backend', '_auth_user_hash'])
request.session.values():
dict_values(['1', 'django.contrib.auth.backends.ModelBackend',
'1e7b45ed1cfb2632e3221aab4b00d5b2b1a500215e556786cebb801f19b53e9d'])
request.session.items():
dict_items([('_auth_user_id', '1'), ('_auth_user_backend', 'django.contrib.auth.backends.ModelBackend'),
('_auth_user_hash', '1e7b45ed1cfb2632e3221aab4b00d5b2b1a500215e556786cebb801f19b53e9d')])
request.session.get('_auth_user_hash'):
1e7b45ed1cfb2632e3221aab4b00d5b2b1a500215e556786cebb801f19b53e9d
По умоланию подсистема сессий сохраняет их в бд, но это можно переопределить
если выбрать другой механизм хранения сессий
Работа с сессиями аналогина работе со словарями
Единтвенное клюи и знаения должны быть сериализуемы в JSON
request.session['foo'] = 'bar'
request.session.get('foo') - 'bar'

Вот как выглядят сессии, если их распечатать в виде словаря - print(dict(request.session))
{'_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
 '_auth_user_hash': 'f79daa3fe9e21caed1e12961bd15f67748985bfc4f35512f30fdd89be74b3a13',
 '_auth_user_id': '1'}

    !!!                                                                     !!!
        Когда пользователь авторизуется на сайте, его анонимная сессия теряется,
        и создается новая, ассоциированная с конкретным пользователем. Если ты хранишь
        в анонимной сессии данные, которые не должны быть утеряна после авторизации,
        необходимо копировать их в новую сессию при входе пользователя
    !!!                                                                     !!!

Как уже было сказано сессии сохраняются в бд в таблицу django_session
upd: сессии из Cookie,
В django же они являются экземплярами класса Session
приложения django.contrib.sessions
    !!! Следующие способы хранения данных в сессии:                         !!!
        -- На основе базы данных - инфа сессии хранится в бд (по умолчанию) (upd уже не уверен что по умолчанию)
        -- На основе файлов - данные сохраняются в файловой системе
        -- На основе кеша - данные хранятся в бэкэнде кеширования
            можно настроить с помощью конфигурации CACHES в settings.py
            Сессии на основе кеша - самый быстрый способ
            https://docs.djangoproject.com/en/4.0/topics/http/sessions/#using-cached-sessions
            Отличные варианты кеширования - Memcached и Redis
        -- На основе кеша и базы данных - инфа записывается в бд, но для доступа
            к ней обращение идет сначала в кеш, и только в том случае, если там этой
            информации уже нет, выполняется запрос в базу данных
        -- На основе куков - данные сессий сохраняются в куках, отправляемых в браузер
            пользователю.
    !!!                                                                     !!!
        Django использует формат JSON для сериализации данных сессии. Поэтому важно,
        чтобы ключи были string
    !!!                                                                     !!!

                            Session settings
doc:
https://docs.djangoproject.com/en/3.2/topics/http/sessions/
https://docs.djangoproject.com/en/3.2/topics/http/sessions/#settings
https://docs.djangoproject.com/en/3.2/ref/settings/
https://docs.djangoproject.com/en/3.2/ref/settings/#sessions

SESSION_COOKIE_AGE - время жизни сессии на основе куков. измеряется в секундах
(по умолчанию 1209600 - 2 недели)

SESSION_COOKIE_DOMAIN - домен для сессий на основе куков. Установить константу
равной домену сайта, или None, чтобы избежать угрозы подмены куков

SESSION_COOKIE_HTTPONLY - булево значение, говорящее о том, может ли сессия на
основе куков быть задана через HTTP и HTTPS или только HTTPS

SESSION_EXPIRE_AT_BROWSER_CLOSE - время жизни сессии на основе куков после
закрытия браузера (проще - время жизни сессии в браузере) по умоланию False
Если установить True - сессия будет заканчиваться при закрытии пользователем браузера

SESSION_SAVE_EVERY_REQUEST - булево значение. Если оно равно True, сессия будет
сохраняться в бд при каждом запросе. При этом время оконания ее действия булет
автоматиески обновляться

    !!!
        Настройка сессий, чтобы сессии хранились в кеше -
        https://docs.djangoproject.com/en/4.0/topics/http/sessions/#using-cached-sessions
    !!!

    !!! Самая важная настройка сессии - SESSION_ENGINE - позволяет указать каким образом
    хранить данные сессии (по умолчанию сохраняются в бд, таблицу django_session)
    По умоланию SESSION_ENGINE = 'django.contrib.sessions.backends.db'
    метод set_expiry() объекта request.session - тоже может изменить время жизни сессии

методы и аттрибуты request.session:
accessed
clear
clear_expired
create
create_model_instance
cycle_key
decode
delete
delete_test_cookie
encode
exists
flush
get
get_expire_at_browser_close
get_expiry_age
get_expiry_date
get_model_class
get_session_cookie_age
has_key
is_empty
items
key_salt
keys
load
model
modified - атрибут, отвечает за сохранение изменений request.session,
            как минимум в нашем коде (присвоить request.session.modified = True), по умолчанию равен False
pop
save
serializer
session_key
set_expiry - можно установить время жизни сессий (callable)
set_test_cookie
setdefault
test_cookie_worked
update
values


здесь мы работаем с сессиями:
https://github.com/Kirill67tyar/myshop/blob/master/src/cart/cart.py
https://github.com/Kirill67tyar/myshop/blob/master/src/cart/views.py

При работе с сессиями вот как выглядит request.session:
    {'_auth_user_backend': 'django.contrib.auth.backends.ModelBackend',
     '_auth_user_hash': 'f79daa3fe9e21caed1e12961bd15f67748985bfc4f35512f30fdd89be74b3a13',
     '_auth_user_id': '1',
     'cart': {'1': {'price': '50.00', 'quantity': 1},
              '2': {'price': '20.00', 'quantity': 4}}}

А вот как request.COOKIES:
    {'csrftoken': 'UHXhP5CDb2ml7UsBI5SuZvSf2XRWS0TQLu3XsjWAQHHQqjMEcTJuiRCrChXCvhZW',
     'sessionid': 'cxxakvlafv7eh2yehb3h908hc74uh599'}


Вывод - не всё понятно с django session. А именно:
1 - где будет храниться эта корзина, если СКОРЕЕ ВСЕГО в куках при HTTP ответе её нет
2 - что в итоге такое request.session, ведь это не тоже самое что и request.COOKIE
3 - когда пользователь отвечает, в request.COOKIE нигде нет корзины, зато они есть в django.session
    каким образом поддерживается передача этой информации между клиентом и сервером
    по идеи должна быть в заголовках, но нигде в заголовке её не видно


# ----------------------------- непонятно -------------------------------
Если послать HTTP запрос с POSTman  добавлением товара в корзину
чтобы можно было видеть заголовки HTTP ответа, то вот как они будут выглядить

    csrftoken=VN3u82a9UdwqOFGR79uK4VxX6QiToGglzczu5HXnJUjVSjuzzLUZcHgAcvGG8GE1;
    expires=Fri, 23 Jun 2023 06:48:12 GMT;
    Max-Age=31449600;
    Path=/;
    SameSite=Lax

Более того, дополнительно указано, что есть две cookie:

    sessionid и csrftoken

хотя в заголовках cookie при ответе на postman никакого sessionid не видно
# ----------------------------- непонятно -------------------------------
"""
