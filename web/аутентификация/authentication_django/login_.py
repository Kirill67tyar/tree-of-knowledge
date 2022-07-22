from pprint import pprint as pp

"""
sources:
    https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in

- Set-Cookie
    https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie
    https://www.ietf.org/rfc/rfc2109.txt
    https://www.ietf.org/rfc/rfc2965.txt
    позволяет web-серверу установить сессию на клиенте
    Схема работы с куками:
        1) клиент отправляет логин - пароль (вход на сайт)
        2) web сервер проверяет авторизацию
        3) с помощью Set-Cookie при HTTP ответе клиенту передаёт очень длинную строчку
           это строчка и есть ключ сессии
        4) браузер запоминает эту строчку у себя
        5) и возвращает эту строчку при каждом последующем запросе
           в заголовке Cookie
    по этому сессионному ключу web сервер может понять какой пользователей к нему пришёл
    
с помощью функции login(request=..., user_instance=...) Django создаёт 
в HTTP ответе заголовок Set-Cookie с сессионным ключом
далее, когда браузер будет делать HTTP запросы к серверу 
он будет возвращать этот сессионный ключ в заголовке Cookie
сервер будет проверять этот сессионный ключ,
и по нему определять какой пользователь делает HTTP запрос
(класс для request.user будет User а не AnonymousUser)

logout(request=request) - разрывает этот сессионный ключ
"""
