"""
sources:
    https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-template-context-processors
    https://docs.djangoproject.com/en/3.2/ref/templates/api/

    как написать контекстный процессор
    https://docs.djangoproject.com/en/4.0/ref/templates/api/#writing-your-own-context-processors

from django.template.context_processors import request


                            Контекстный процессор django
как сделать так, чтобы какая-нибудь переменная была доступна на всех шаблонах проекта?
скажем как request
Для этого и существует контекстный процессор. В настройках в константе TEMPLATES по ключу OPTIONS
список подключенных контекстных процессоров. Они устанавливаются автоматически.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [ ----------- ВОТ ЭТО И ЕСТЬ ПОДКЛЮЧЕННЫЕ КОНТЕКСТНЫЕ ПРОЦЕССОРЫ
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
Контекстный процессор - это функция Python, принимающая объект запроса request (request - это и есть объект)
и возвращающая словарь, который будет добавлен в контекст запроса. Этотссловарь будет добавляться в контекст
любого шаблона, работающего с контекстом типа RequestContext.
К их использованию прибегают, когда нужно получить доступ к какимм-либо объектам или
переменным глобально, во всех шаблонах проекта
Пример контекстного процессора:
def cart(request):
    return {'cart': Cart(request=request)}
или посмотри в файле:
from django.template.context_processors import request

Когда мы создаем проект django-admin startproject some_name в проект уже добавляется несколько
контекстных процессоров:
    1) django.template.context_processors.debug - Добавляет булевое знаяение debug и переменную
       sql_queries содержащую выполненные для запроса SQL инструкции в контексте шаблона
    2) django.template.context_processors.request - добавляет объект запроса request в контекст
       (request - экземпляр класса HttpRequest или WSGIRequest)
    3) django.contrib.auth.context_processors.auth - добавляет объект текущего пользователя в
       переменную user (можен request.user)
    4) django.contrib.messages.context_processors.messages - добавляет переменную messages, содержащую
       уведомления сформированные для пользователя подсистемой сообщений Django
    5) Есть еще django.template.context_processors.csrf процессор - обезопашивающий проект от
       CSRF-атак. Отключить его никак нельзя (во всяком случае без хака django).
       Хотя напрямую он не указан

    Полный список контекстных прочцессоров
    https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-template-context-processors

И так:
    1) создаешь файл в одном из приложений context_processors.py
    2) создаешь там функцию которая будет принимать request и возвращать определенный словарь
    3) подключаешь в settings.py в контанте TEMPLATES в ключе context_processors
       вот таким образом
       'context_processors': [
                'django.template.context_processors.debug',
                ...
                'cart.context_processors.cart', # мой контекстный процессор
            ],
    Если нужна переменная котрая будет обращаться в бд, то луше написать шаблоный тег
    или просто inclusion_tag
    Контекстные процессоры выполняются при обработке всех запросов использующих RequestContext (хз как это понимать)
"""