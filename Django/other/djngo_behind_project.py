# ------------------------------------------------------- Запуск Django в не самого проекта
import os, sys


proj = os.path.dirname(os.path.abspath('manage.py'))    # устанавливаем абсолютный путь

# тут мы добавляем путь в системные переменные путей
sys.path.append(proj)

# здесь мы импортируем все настройки, которые находятся в django-проекте
# и переменные окружения операционной системы добавляем ключ, в котором
# содержатся наши настройки
os.environ['DJANGO_SETTINGS_MODULE'] = 'scraping_service.settings'
# for p in os.environ:
#     print(f'{p} - {os.environ[p]}')
import django

django.setup()
# ------------------------------------------------------- Запуск Django в не самого проекта