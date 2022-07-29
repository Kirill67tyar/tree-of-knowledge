"""
---------------------------------------------------------------------------------------------
                                RESTful API

from book:
Иногда в проектах появляется необходимость взаимодейтсвия с другими системами для отображения
данных вашего веб-приложения. Для этих целей реализуется специальный интерфейс,
API (application programming interface), которвый определяет точки взаимодействия двух систем.
Наиболее часто для таких целей используется REST (чтобы организовать API)
REST (Representational State Transfer) - передача состояния управления.
Такой способ взаимодействия основан на ресурсах.

Модель приложения (база данных) - представляет из себя ресурсы,
а HTTP заголовки запросов - действия.

Действия в REST должны быть следующие - Create, Read, Update, Delete

за Create отвечает метод POST
за Read отвечает метод GET
за Update отвечает методы (PUT, PATCH)
за Delete - DELETE

общепринятые форматы взаимодействия RESTful API - JSON и XML
При реализации интерфейса для REST API важно продумать, какие точки доступа будут.
Наиболее часто для построения логики REST APi используется фреймворк Django REST Framework

Если в кратце то RESTful API представляет следующее:
возможность Читать, Создавать, Изменять, Удалять определенные данные из базы данных,
которые мы предоставляем (точка достпа), посредством HTTP методов, через
форматы взаимодействия JSON или XML.

Позволяет другим системам (в основном front-end) взаимодействовать с нашим приложением
(по сути с базой данных напрямую через JSON)
REST API в web это легализованный способ доступа информации, который прописывает обладатель информации
доступ в db

это специальное приложение, которое позволяет распарсить инфу с сайта официально и через формат json
а не с помощью библиотеки BeautifulSoup, где мы вычленяем информацию из тегов.
и кстати даже добавлять, изменять, удалять эту инфу.

Общение клиента с REST API происходит через http методы, и http заголовки
    !!!                                                                             !!!
        REST описывает принципы взаимодействия клиента и сервера,
        основанные на понятиях «ресурса» и «глагола» (можно понимать их как подлежащее и сказуемое).
        В случае HTTP ресурс определяется своим URI, а глагол — это HTTP-метод.
    !!!
                                                !!!
а API - это application programming interface (интерфейс программы для разработика)

    Ну и про HTTP:
    https://datatracker.ietf.org/doc/html/rfc2616
    Очень неплохая статья:
    https://habr.com/ru/post/50147/
    Отличный пример документации API:
    https://ghost.org/docs/content-api/
    Потенциальный пример для будущего api
    https://developers.themoviedb.org/3/getting-started/introduction
    библиотека google translate
    https://pypi.org/project/googletrans/

************** Django REST Framework
https://www.django-rest-framework.org/
-- settings --
https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

REST_FRAMEWORK - основная константа для настроек django rest framework.
поддерживает множество различных параметров для поведения по умолчанию.
параметр (ключ) DEFAULT_PERMISSION_CLASSES за разрешение по умолчанию для доступа к:
Чтению, Созданию, Изменению, Удалению объектов.
DjangoModelPermissionsOrAnonReadOnly - анонимные пользователи могут только просматривать,
а авторизованные имеют полный CRUD функционал по умолчанию.

************** Serializers (Model, all)
отлиная статья о принципах работы Serilalizer и ModelSerializer и Serilalizer
https://www.django-rest-framework.org/api-guide/serializers/
Сериализаторы, которые мы определяем - могут заимствоваться от 3 классов:
1) Serializer - сериализует обычные python классы (объекты python)
2) ModelSerializer - преобразует объекты моделей Django (превращает в OrderedDict или ReturnList)
3) HyperlinkedModelSerializer - аналогичен классу ModelSerializer, но для связанных объектов
формирует http ссылки а не внешние ключи.
(есть еще поле HyperlinkedIdentityField которое позволяет это сделать в ModelSerializer)
Система проста:
- для функционала Read (list, retrieve), Delete
1) принимает на вход объект модели или Queryset
2) если принимает QuerySet, то нужно указать дополнительный аргумент many=True
- для функционала Create, Update
1) если Create - принимает request.data (по сути словарь, то что приходит с POST/PUT/PATCH запросами)
2) если Update - то принимает сначала экземпляр модели или Queryset в аргумент instance
    а в аргумент data принимает request.data
3) Важный момент, когда у тебя обработчик - класс, унаследованный от GenericAPIView и миксина
в методе perform_create ты не можещь вызывать serializer.data при создании.
ты можешь вызывать validated_data и вызовется OrderedDict при создании новой записи
Далее у serializer (экземпляр класса заимствованного от Serializer или ModelSerializer)
будет доступен аргумент data, где можно посмотреть, что в нем содержится.

************** парсеры и рендеры в django rest framework
https://www.django-rest-framework.org/api-guide/renderers/
https://www.django-rest-framework.org/api-guide/parsers/
DRF работает с форматом взаимодействия JSON.
Нужно как то вычленять из HTTP запроса JSON данные, чтобы можно было с ними работать в python коде
И наоборот, из python кода загружать данные в HTTP запрос, чтобы они были, в формате JSON.
Для этого и нужны рендеры и парсеры

----- парсер позволяет преобразовывать тип данных JSON в dict python:
from io import BytesIO
from rest_framework.parsers import JSONParse
datab = b'{"pk": 1, "title": "programming", "slug": "programming"}'
JSONParser().parse(stream=BytesIO(datab))
{'pk': 1, 'title': 'programming', 'slug': 'programming',}
По сути эта команда делает тоже что и json.loads(), но только не совсем понятна история с байтами
В DRF для получения python объекта из JSON используется класс JSONParses.
Т.е. JSONParses - это парсер DRF. Скорее всего атрибут data в request (request.data)
появляется благодаря парсеру JSONParses
Вот так парсер класс определяется (хотя по умоланию и так стоит JSONParses)
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

----- рендер позволяет формировать ответы на запросы к API.
Грубо говоря преобразует объекты python (dict, OrderedDict, ReturnList) в JSON данные
from rest_framework.renderers import JSONRenderer
Для определенния конкретного класса рендерера DRF смотрит на тип объекта, который
нужно преобразовать (dict или QuerySet или экземпляр модели).
тип ответа зависит от заголовка Accept, HTTP запроса
для формирования json ответа будет задействован JSONRenderer
from rest_framework.renderers import JSONRenderer
serializer_data = {'pk': 1, 'title': 'programming', 'slug': 'programming',}
JSONRenderer().render(serializer_data)
b'{"pk":1,"title":"programming","slug":"programming"}'
По умоланию DRF ипользует два рендерера:
JSONRenderer
BrowsableAPIRenderer - предоставляет веб-интерфейс для просмотра API
Воэ эта страница с документацией и формами, которое мы полуаем при обращение к API
приложения с JSON данными из базы данных генерируется благодаря рендереру BrowsableAPIRenderer
Можно указать необходимый класс в настройках:
DEFAULT_RENDERER_CLASSES в константе REST_FRAMEWORK

************** Базовый набор классов и примесей в DRF
https://www.django-rest-framework.org/api-guide/generic-views/
Базовый набор классов и примесей могут использоваться для точек доступа к функциями:
полуения, создания, изменения, удаления объектов.
APIView
from rest_framework.views import APIView
Заимствуется от View.
Отличия от View и особенности:
-- APIView использует собственные классы для объекта запроса и ответа (Request и Response)
-- может обрабатывать исключения APIException (from rest_framework.exceptions import APIException)
возвращая необходимые коды ошибок
-- Реализует методы авторизации и аутентификации, чтобы была возможность ограниить доступ
к обработчику API-запросов

А вообще система довольна проста:
    1) Есть базовый APIView.
    - Методы get, post, put, patch, delete там придется полностью писать вручную,
    вернее начинку этих методов, сам эти методы там есть, т.к. APIView заимствован от View из Django
    - Атрибуты queryset, serializer_class, permission_classes, authentication_classes и т.д
    там есть
    2) Есть:
    - GenericAPIView (from rest_framework.generics)
    и миксины:
    - CreateModelMixin (Create)(from rest_framework import mixins):
    - ListModelMixin (Read)
    - RetrieveModelMixin (Read)
    - UpdateModelMixin (Update)
    - DestroyModelMixin (Delete)
    Так вот, у этих миксинов есть методы list, retrieve, create, update, partial_update, destroy
    (а также perform_create и perform_update)
    Эти миксины с этими методами работают только в связке с GenericAPIView
    Так что можно создавать классы вручную и наследоваться от миксина и GenericAPIView
    А можно использовать из rest_framework.generics типо ListAPIView или RetrieveUpdateDestroyAPIView
    Они уже унаследованы от миксинов и GenericAPIView, причем во всех возможных вариантах.
    3) Есть ViewSet (from rest_framework.viewsets)
    Ситуация схожа с генериками которые уже от всего унаследованы, но добавляется еще класс GenericViewSet
    И есть итоговый базовый класс:
    - ModelViewSet
    С полным CRUD функционалом.
Из преимществ появляется self.action (list, retrieve и т.д.)
И возможность настроить роутер в urls.py
Вот что написано в ModelViewSet  в viewsets.py:
ViewSets are essentially just a type of class based view, that doesn't provide
any method handlers, such as `get()`, `post()`, etc... but instead has actions,
such as `list()`, `retrieve()`, `create()`, etc...
Actions are only bound to methods at the point of instantiating the views.
    user_list = UserViewSet.as_view({'get': 'list'})
    user_detail = UserViewSet.as_view({'get': 'retrieve'})
Typically, rather than instantiate views from viewsets directly, you'll
register the viewset with a router and let the URL conf be determined
automatically.
    router = DefaultRouter()
    router.register(r'users', UserViewSet, 'user')
    urlpatterns = router.urls

************** Обработка аутентификации пользователей в DRF
sources:
    отличная статья по аутентификации в DRF
    https://starkovden.github.io/authentication-and-authorization.html

https://www.django-rest-framework.org/api-guide/authentication/
Прописывается в настройках аутентификация так:
REST_FRAMEWORK = {# REST_FRAMEWORK - базовая константа для настроек DRF
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
from rest_framework.authentication import BasicAuthentication
В DRF есть классы для управления аутентификацией

-- BasicAuthentication - базовая аутентификация в DRF. Пользователь и пароль отправляются в
    зашифрованном виде в заголовке HTTP Authorization
    https://en.wikipedia.org/wiki/Basic_access_authentication

-- TokenAuthentication - бэкэнд для авторизации по токену.
    Используется модель токен для сохранения токенов, для сохранения токенов пользователей
    которые добавляются к запросам в HTTP заголовке Authorization
    гугли token authentication и т.д. (скорее всего это и есть JWT аутентификация)

-- SessionAuthentication - бэкэнд на основе сессий Django. Полезен, когда браузерный код
    отправляет AJAX или другие асинхронные запросы

-- RemoteUserAuthentication - делегирует процесс авторизации пользователя веб-серверу,
    который устанавливает переменную окружения REMOTE_USER
    Можно создать собственный бэкэнд. Нужно унаследоваться от BasicAuthentication
    и описать для него метод authenticate()

    !!! Аутентификация только определяет конкретного пользователя, выполняющего запрос. !!!
        Она не ограничивает доступ к обработчикам по ролям.
    !!! Для ограничения доступа к обработчикам используются permissions (я так понимаю от DRF)!!!

как добавить аутентификацию в наш обработчик?
Ну если это класс, то через атрибут authentication_classes = (,)
DRF определяет пользователя по HTTP заголовку Authorization
https://developer.mozilla.org/ru/docs/Web/HTTP/Headers/Authorization
заголовок Authorization использует кодировку base64
что не безопасно. Ее можно с лугкостью расшифровать.
В чем недостаток basic authentication в DRF
в headers запроса появляется загловок со значением:
Authorization: Basic a2lyaWxsYm9nb21vbG92LnJpY0B5YW5kZXgucnU6YWxza2RqZmhn
это можно декодировать в utf-8 - https://www.base64decode.org/
Это обычная кодировка base64 и передается в headers каждый раз при GET запросе
Главных недостатка 2:
1 - каждый раз мы светим email и паролем в headers в небезопасной кодировке - очень не безопасно.
2 - лишняя нагрузка на базу данных, ведь каждый раз при таком запросе приходится
сверять email и пароль в базе данных.
Это не как обычная авторизация, когда мы проверяем валидность логина и пароля,
и если всне норм, то запоминаем что это нужный пользователь с помощью сессионого ключа
который создается с помощью функции login().
Здесь мы каждый раз проверяем логин и пароль, что очень не эффективно.
Поэтому лучше использовать систему JWT токен
************** JSON Web Token (JWT)
https://jwt.io/
https://pyjwt.readthedocs.io/en/stable/
https://github.com/Kirill67tyar/pyjwt
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
https://pypi.org/project/djangorestframework-simplejwt/
Гугли дополнительно про JWT.
Много картинок и схем как это работает.
Вот неплохая статься https://habr.com/ru/post/340146/
она же на английском:
https://morioh.com/p/63009714b79a
И of course wikipedia: https://en.wikipedia.org/wiki/JSON_Web_Token
Картинка JWT:
C:\Users\User\Desktop\Job\learning_tree\tree-of-knowledge\web\JWT\JWT
Там можно выбирать разные алгоритмы формирования этого токена (по умолчанию HS256)
Данный токен представляет из себя короткое время жизни, и предстовляет из себя структуру,
которую можно однозначно идентифицировать
Пример токена:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
Состоит из трех частей:
HEADER:ALGORITHM & TOKEN TYPE
1 часть - голова, где передается алгоритм шифрования и какой это тип токена
{
  "alg": "HS256",
  "typ": "JWT"
}
PAYLOAD:DATA
2 часть - это данные по пользователю (нечувствительные данные имя или id юзера,
или администратор ли он, метаданные в общем) данные чтобы пользователя можно было однозначно идентифицировать
iat - это время жизни этого токена
Как формируются ключи JWT, какие обязательны, какие нет:
https://en.wikipedia.org/wiki/JSON_Web_Token#Standard_fields
{
  "sub": "1234567890",
  "name": "John Doe",
  "iat": 1516239022
}
VERIFY SIGNATURE
3 часть - это пара первых двух частей (headers и payload), которые зашифрованы с помощью секретного
ключа, который знает только сервер
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
your-256-bit-secret
)
Важно - все эти три данные в токене декодированы base64
* Как это все работает?
1) Когда сервер получает данный токен, он его разбивает на три части по точке
2) При это у сервера есть свой секретный ключ
3) И сервер их шифрует с помощью секретного ключа
4) И если эти данные совпали с тем, что пришло от клиента
точнее совпадает 3 часть токена и то как зашифровал сервер с помощью секретного ключа
значит тому пользователю, что указан во второй части (payload) можно доверять
Дальше как это работает на уровне сервера смотри видео с 8:09 (django API, bot flask)
* Зачем нужно маленькое время жизни данного ключа?
Для того чтобы уменьшить вероятность использования данного токена другими людьми
Если кто-то в HTTP трафике перехватит этот токен, этот токен через 5 мимнут протухнет,
и он уже им воспользоваться не сможет
* Как получить новый токен?
Для этих целей придумана другая структура. Не просто один токен, а пара токенов
"access token" - многоразового использования, но с коротким временем жизни
"refresh token" - одноразовый, но с большим временем жизни
Похоже refresh token это приватный ключ, а access token - публичный ключ
Того токен, что мы разобрази выше это access token который быстро протухает
Его можно много раз использвать, до того, как он протухнет
Как только он протух нужно получить новый access token
Для этого как раз и новый refresh
refresh token позволяет обратиться по определенному адресу, полуить новую пару
access token и refresh token и опять использовать уже новый access token
до времени жизни access token и тд.
Эти токены получаются один раз, когда происходит логирование на сайте.
нормальная авторизация через метод post. Сервер сам выдает эти токены при валидной авторизации
* А как быть, если хакер перехватил и access и refresh token?
Ну походит он по серверу, что-то поделает. Но потом эта пара будет невалидна той,
которую настоящий пользователь получит заново при авторизации.
Система будет видеть что не у пользователя не у хакера не валидный refresh
и таким образом анулируются все токены, нужно будет пройти снова процесс авторизации
и после этого нормальный пользователь получит новые access и refresh, которые будут отличаться
от того, то есть у хакера.
Это в целом безопасная система, которая минимизирует взлом и возможность долго
пользоваться чужим аккаунтом.
Уходит от того, что очень увствительные данные будут использоваться в теле запроса
Будут использоваться только токены. Максимум инфы это возможный id пользователя.
************** djangorestframework-simplejwt
Как работать с библиотекой djangorestframework-simplejwt
для системы токенов
важно - при использовании такой системы authenticated_classes нужно отключать в обработчиках
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
https://pypi.org/project/djangorestframework-simplejwt/
* Как установить:
1) pip install djangorestframework-simplejwt
2) добавить 'rest_framework_simplejwt.authentication.JWTAuthentication',
в базовую настройку REST_FRAMEWORK, поднастройку DEFAULT_AUTHENTICATION_CLASSES
REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        )
    ...}
3) в корневом urls.py импортировать TokenObtainPairView и TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
4) добавть в корневой urlpatterns:
path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
5) все, минимальная настройка готова
* Механиз авторизации с token:
1) Для первого раза делаешь post запрос на http://127.0.0.1:8000/api/token/
при этом вставляешь в тело запроса JSON данные
{"email": "kirillbogomolov.ric@yandex.ru",
"password": "alskdjfhg"}
или те, с помощью которых происходит аутентификация на сервере
2) получаешь два токена (в body HTTP-response):
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDMwNTkyNiwianRpIjoiYzlmMjA5Y2NmODRlNDdjOGExZDdjMjZlZjI5Y2FkZjciLCJ1c2VyX2lkIjoxfQ.bVv5YYN8ucakAlTk2pIs-Cx_79_uYzZ-OQLZlaZ1FkE",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MjE5ODI2LCJqdGkiOiI1NTZmMmQ1ZmQxZWE0NzQ2ODNiMDRhYmMzZWJmOTY5YSIsInVzZXJfaWQiOjF9.ZCVkefJofX-OqsNZdtEdN9YDYczLml8glQSlxLBb2ls"
}
refresh token - публичный токен который быстро протухает
access token - приватный токен, который нужно сохранить, и менять, когда публичный протухнет
по тому адресу http://127.0.0.1:8000/api/token/refresh/
или можно получть новые refresh и access токены
3) для доступа к контенту
выбираешь способ аутентификации Bearer Token и вставляешь access token в нужное место
4) чтобы обновить access token посылаешь post запрос по адресу (без аутентификации)
http://127.0.0.1:8000/api/token/refresh/
с телом запроса:
{"refresh":
"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.
eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNDMwNTkyNiwianRpIjoiYzlmMjA5Y2NmODRlNDdjOGExZDdjMjZlZjI5Y2FkZjciLCJ1c2VyX2lkIjoxfQ.
bVv5YYN8ucakAlTk2pIs-Cx_79_uYzZ-OQLZlaZ1FkE"}
(любой другой refresh token)
и получаешь access token, который можешь дальше использовать
*
refresh token по умолчанию один день
access token по умолчанию 5 минут
в настройках можно менять
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
from datetime import timedelta
...
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),# - отвечает за срок годности access token
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),# - отвечает за срок годности refresh token
    ...
Когда ты автризиуешься через Bearer Token то в заголовках HTTP появится такой заголовок:
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI0MjIxNDY5LCJqdGkiOiIzZDNlYjFhZmJmNGY0YjZhOTYyZTM0Y2NkM2EyMTExZSIsInVzZXJfaWQiOjF9.QYDh52m4ixIPo0aqQ0cCjiO_AvMQ1uLP04Wa53FvAwc
(понятно что вместо eyJ0eXAiOiJKV... будет access token)
************** permissions
https://docs.djangoproject.com/en/3.2/topics/auth/default/#permissions-and-authorization
https://www.django-rest-framework.org/api-guide/permissions/
В DRF реализована система доступа пользователей к данным, по анологии с тем, как это
сделано в Django.
Разрешения определенные в DRF:
-- AllowAny - позволено любому
-- IsAuthenticated - доступ имеют только авторизированные пользователи
-- IsAdminUser - только админы имеют доступ
-- IsAuthenticatedOrReadOnly - авторизированные имеют доступ к полному функционалу,
 анонимные только к чтению
-- DjangoModelPermissions - разрешение на основе django.contrib.auth
У обработчиков с таким уровнем должен быть задан QuerySet.
Будут иметь доступ те, кто умеют разрешение на обращение к указанной модели
-- DjangoObjectPermissions - разрешение Django по отношению к конкретным объектам.
Доступ к обработчику в классе прописывается permission_classes = (,)
Если доступ запрещен, то формируется HTTP Ответ с статус кодом:
401 - пользователь не авторизован
403 - доступ запрещен
Да, ну и можно самим определять свои классы доступа (разрешения):
from rest_framework.permissions import BasePermission, SAFE_METHODS
from notes.models import Note
class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
Т.е. надо определить has_permission и has_object_permission
BasePermission - базовый класс, от которого должен наследоваться наш permission
has_permission - выполняет проверку доступа на уровне обработчика
has_object_permission - проверяет доступ к объекту
Чтобы разрешить доступ нужно возвращать True, чтобы запретить - False

"""