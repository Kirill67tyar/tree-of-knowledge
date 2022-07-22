
----------------------------------------------------------------------------------------------------------
Draft:
1) git init

2) git remote add origin (ssh github)

3) git pull origin master

OR

1,2,3) git clone (ssh repository/url repository)

git clone -b <branch> <remote_repo>

Рекомедуется установить виртуальное окружение и включить его

4) User@DESKTOP-MUSPUHU C:\Users\.....\scraping_service\src>

5) как записать все пакеты в файл requirements.txt, что используются в нашем приложении:
pip freeze > requirements.txt

установить же:
или так - $pip install -r requirements.txt
или так - $pip install -r requirements.txt --no-index --find-links file:///tmp/packages
или так - $pip install -r /path/to/requirements.txt

6) как сделать собственный секретный ключ для django:

import secrets

generated_key = secrets.token_hex(24)
'32nsd33223fsfsdyty556213gfdftre455tre4434terqf53gd2fss'

или
generated_key = secrets.token_urlsafe(length)
'32nsd33223fsfsdyty556213gfdftre455tre4434terqf53gd2fss'

эти цифры подойдут как SECRET_KEY для Django

Или вы можете создать django проект в другом виртуальном окружении
django-admin startproject some_empty_project_for_secret_key

скопировать от туда SECRET_KEY и использовать в это проекте


7) вам нужно создать файл .env в папке scraping_service (wsgi.py, urls.py, asgi.py)
(это для переменных из виртуального окружения)


8) добавить в файл .env:
SECRET_KEY=<your secret key>
EMAIL_HOST_USER=<mail for application>
EMAIL_HOST_PASSWORD=<password from mail>

(заменить <your secret key> на ваш secret key без ковычек и знаков <> и т.д.)

Как работать с python-dotenv:
https://pypi.org/project/python-dotenv/

9) ввести команду в консоль:
python manage.py migrate


10) ввести команду в консоль:
django-admin createsuperuser
We have error. Or error have us.

пример REDMI:
https://github.com/devmanorg/wines_api