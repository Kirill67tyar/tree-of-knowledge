"""
sources:
    https://github.com/python-social-auth
    https://github.com/python-social-auth/social-app-django
    https://python-social-auth.readthedocs.io/en/latest/
    https://django.fun/docs/social-docs/ru/0.1/
    https://pypi.org/project/python-social-auth/

    полный список поддерживаемых бэкэндов аворизации через социальные сети
    https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends

    примеры аутентификации через facebook и google
    https://github.com/Kirill67tyar/bookmarks-service/blob/master/src/bookmarks/settings.py
    https://github.com/Kirill67tyar/bookmarks-service/blob/master/src/bookmarks/urls.py

    django-book стр. 122

это Python приложение, которое даёт возможность пользователям использовать
аккаунты сторонних соцсетей для входа на наш сайт.
доступна не только для django но и для других фреймвороков на Python
pip install social-auth-<component>

--- Установка:
1) pip install social-auth-app-django
2) INSTALLED_APPS = [..., 'social_django',]
3) python manage.py migrate
   у тебя появится куча таблиц в бд, начинающихся на social_
4) urlpatterns = [..., path('social-auth/', include('social_django.urls', namespace='social')),] (в базовом urlpatterns)
5) некоторые социальные сервисы не позволяют выполнять перенаправление
   на 127.0.0.1 или localhost после успешной аутентификации пользователя.
   Для того чтобы работать с ними локально, нам нужен домен.
   нужно отредактировать файл hosts, добавить туда вконец 127.0.0.1 mysite.com
   (разумеет вместо mysite.com можно написать другой хост)
    - для Linux или macOSX, отредактировать файл etc/hosts
    - для windows отредактировать файл C:\Windows\System32\drivers\etc\hosts
      https://help.reg.ru/hc/ru/articles/4408047768849-%D0%A4%D0%B0%D0%B9%D0%BB-hosts-%D0%B4%D0%BB%D1%8F-Windows-10
6) ALLOWED_HOSTS = [..., 'mysite.com'] (добавить твой хост, как бы он не назывался)

--- Использование (на примере подключения google):
1) AUTHENTICATION_BACKENDS = [..., 'social_core.backends.google.GoogleOAuth2',]
   как выгледят бэкэнды для разных сервисов:
   from social_core.backends.   (посмотри какие варианты доступны для импорта)
   полный список поддерживаемых бэкэндов аворизации через социальные сети
   https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends
2) смотри как подключать приложение google к твоему проекту на странице 130 djangoo-book
   понадобится этот сайт https://console.cloud.google.com/apis/dashboard?project=myproject61365
   также есть гугл, где можно посмотреть как это можно подключать
3) узнать какими будут Client ID и Client secret
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '736958318829-vfc9nfio....apps.googleusercontent.com' # Client ID
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'v7OX...QMKYm' # Client secret


настройки для yandex:
https://github.com/omab/python-social-auth/issues/981
SOCIAL_AUTH_YANDEX_OAUTH2_KEY = ''
SOCIAL_AUTH_YANDEX_OAUTH2_SECRET = ''



!!!                                                             !!!
    важно при запуске не использовать localhost или 127.0.0.1
    именно для этого на локальной машине мы добавляли домен
    mysite.com
!!!                                                             !!!



from bookmarks-service
# 1) pip install social-auth-app-... (django)
# 2) в INSTALLED_APPS добавить 'social_django'
# 3) создать таблицы в бд (python manage.py migrate)
# 4) добавляешь в корневой urls.py path('social-auth/', include('social_django.urls', namespace='social')),
# 5) В settings должен быть указан обязательно LOGIN_REDIRECT_URL = 'accounts:dashboard' (свой app_name и pathname)
# туда куда будет релиректиться при успешной аутентификации
# 6) В settings должен быть указан обязательно AUTHENTICATION_BACKENDS
# с базовой аутентификацией и дополнительным аутентификациями от python-social-auth, как
# 'social_core.backends.google.GoogleOAuth2'
# 7) Создаешь приложение или бот, или гуглишь что и как нужной соц сети
# 8) по итогу подключаешь SOCIAL_AUTH_FACEBOOK_KEY и SOCIAL_AUTH_FACEBOOK_SECRET (FACEBOOK на другое приложение)
# см. в settings.py
"""
from pprint import pprint as pp
from decimal import Decimal
