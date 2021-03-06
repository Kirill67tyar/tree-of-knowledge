"""
--------------------- STEP 1 (2) -----------------------------------------------------------------------------

Оглавление для step 1:

1.--- Web-сервера
2.--- Запуск web-сервера
3.--- Файлы web-сервера
4.--- Процессы web-сервера

web-сервер - сетевой сервер, который занимается обработкой протокола HTTP

Именно сервер занимается отдачей документов по протоколу HTTP, SMTP, FTP

1.--------------------- Web-сервера:

--- Apache
    https://httpd.apache.org/
    Наиболее старый сервер
    Универсальный интернет комбайн, у которого огромное кол-во функций
    Наиболее распространён (60% серверов)

--- Nginx
    https://nginx.org/ru/
    https://nginx.org/ru/docs/
    https://ru.wikipedia.org/wiki/Nginx
    Довольно молодой сервер
    Преимущества:
                быстрота
                надёжность
                легковесность
    Быстро растущей сервер

--- Lighttpd - аналог Nginx


--- Internet information service
    сервер от Microsoft, этим и уникален


    Apache, Nginx, Lighttpd - Unix-сервера
    Unix - https://ru.wikipedia.org/wiki/Unix
           https://thecode.media/unix/


2.--------------------- Запуск web-сервера:

    Последовательность запуска web-сервера следующая:
    - Команда на запуск
    - Чтение файла конфигурации
    - Получение порта 80
    - Открытие (создание) логов
    - Понижение привилегий
    - Запуск дочерних процессов/потоков (*)
    - Готов к обработке запроса

--- Команда на запуск - sudo /etc/init.d/nginx start
    https://ru.wikipedia.org/wiki/%D0%94%D0%B5%D0%BC%D0%BE%D0%BD_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B0)#:~:text=%D0%94%D0%B5%CC%81%D0%BC%D0%BE%D0%BD%20(daemon%2C%20d%C3%A6mon%2C%20%D0%B4%D1%80,%D0%B7%D0%B0%D0%BF%D1%83%D1%81%D0%BA%D0%B0%D1%8E%D1%82%D1%81%D1%8F%20%D0%B2%D0%BE%20%D0%B2%D1%80%D0%B5%D0%BC%D1%8F%20%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8%20%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D1%8B.
    https://losst.ru/chto-takoe-demony-v-linux
    Сначала web-сервер нужно установить в на os linux
    В linux web-сервер является демоном
    Демон - это программа, которая не связана с консолью, с графическим интерфесом
    машины на которой она работает
    Демон - это программа, которая висит в памяти постоянно,
    запускается, висит в памяти, обрабатывает данные,
    которые в большинстве случаев приходят по сети (какой-то сокет)
    Так вот сервер это демон на Linux а все демоны запускаются с помощью init скрипта
    sudo /etc/init.d/nginx start   # команда запуска nginx (может меняться)

    --- init скрипт
        Каждый демон запускается по своему, у него есть свои опции командной строки,
        переменные окружения, которые ему нужны
        Чтобы администратору системы не возиться со всем этим разнообразием
        Разработчики, или скорее те кто оформляют пакет для операционной системы
        включают init скрипты
        init скрипт - программа на языке командного интерпретатора
        в этом скрипте указано как именно нужно запускать сервис
        Интерфейс инит скриптов походижий - имя скрипта, start для запуска, stop для остановки (см. следующий пункт)


--- Чтение файла конфигурации
    При запуске init скрипта:
        - запускается исполняемый код web-сервера
        - он читает файл конфигурации (у кажого web сервера есть файл конфигурации, большой такой, текстовый файл)
        - сервер прочитал конфигурацию. если конфигурация неправильная сервер не запустится вообще
        - в этот момент предполагается что мы запускаем скрипт от суперпользователя


--- Получение порта 80
    Для чего это нужно - веб сервер должен обрабатывать протокол HTTP,
    т.е. он должен открыть и прослушивать порт 80 (или 443)
    а порты ниже 1024 требуют привилегий суперпользователя (см. следующий пункт)

--- Открытие (создание) логов
    логи - текстовый файл, в которых отображается ход работы web-сервера, в частности сообщение об ошибках
    в хороших системах они доступны для чтения только суперпользователям


--- Понижение привилегий
    Дальше web-сервер понижает привилегии - меняет имя текущего суперпользователя
    на более низкий уровень привилегий, чтобы web-сервер не обслуживал постоянно запросы
    от суперпользователя, потому что если в нём есть уязвимость - поставит под угрозу систему

--- Запуск дочерних процессов/потоков (*)
    Когда рпивилегии понижены web сервер опционально запускает дочернии процессы
    так называемые воркеры, либо потоки


--- Готов к обработке запроса
    после того как все потоки запущены - web-сервер готов к обработке запросов


3.--------------------- Файлы web-сервера

Web-сервер работает с жестким диском

--- Конфиг /etc/nginx/nginx.conf
    include /etc/nginx/sites-enabled/*
    Конфиг большой и делится на несколько частей
    конфиг web-сервера - не один файл, а целый набор
    в конфиге инструкии include /etc/nginx/sites-enabled/*
    включения одного файла внутрь другого

--- init-скрипт /etc/init.d/nginx [start|stop|restart]
    запускает сервер

--- PID-файл /var/run/nginx.pid
    Когда сервер запущен он отключается полностью от консоли, и работает независимо от того
    кто его запустил
    иногда web-сервер нужно остановить
    для этого используется стандартный механизм:
        любой демон, который запускается, складывает свой идентификатор процесса
        (pid - порядковый номер процесса, запущенный в системе linux)
        демон складывает этот номер в pid файл к примеру nginx.pid
        далее из этого pid файла можно получить идентификатор pid сервера
        и сделать с ним что нужно, например остановить


--- Error-лог /var/log/nginx/error.log
    Web-сервер открывает файлы логов
    два принципиально разных лога error.log и access.log
    error.log - ошибки

--- Access-лог /var/log/nginx/access.log
    про успешно или неуспешо обработанные HTTP-запросы на web-сервере

--- Есть ещё пользовательские файлы
    web-сервер отдаёт документы с диска


4.--------------------- Процессы web-сервера:

    Процессы операционной системы, которые запущены в работающем web-сервере
    Всё это специфично для разных конкретных серверов
    Выделяется два вида процессов - Master и Worker

    - Master-процесс - запускаем из init-скрипта,
      работает от root (сохраняет свои привилегии)

    - Worker-процесс - работает с пониженными привилегиями
      работает от какого-то другого юзера (часто nobody)
      worker-процесс может быть как один так и много

    Master (root, 1 процесс) # запускаем из init-скрипта
        - Чтения и валидация конфига
        - Открытие сокета(ов) и логов
        - Запуск и управление дочерними процессами (worker)
        - режим мониторинга, поддержание правильного кол-ва работающих воркеров
        - Graceful restart, Binary updates

    Worker (www-data, 1 + процессов)
        - циклическая обработка входящих запросов

    Иногда в web-сервере есть дополнительные процессы, которые следят за очисткой кэша
    кэш-менеджеры


--------------------- STEP 2 (3) -----------------------------------------------------------------------------

Оглавление для step 2:

1.--- Процессы web-сервера:Цикл работы worker-процесса
2.--- Моудльная архитектура (вышло несколько хаотично)

1.--------------------- Процессы web-сервера:Цикл работы worker-процесса

представь, что ниже идёт круг (цикл)

Собственно worker-процесс обслуживает сетевое соединение и работает в цикле

Ниже идёт упрощённый цикл работы воркера

 -->  Чтение HTTP запроса --> Выбор virtual host --> Выбор location --> Провера доступа --> Чтение файла V
 ^                                                                                                      V
 ^ (Цикл замкнулся) Очистка <-- Запись Access Log <-- Отправка HTTP ответа <-- Применение фильтров <--

C:\Users\kiril\Desktop\Job\tree-of-knowledge\web-tehnologies(stepik)\1.8\цикл_работы_worker_процесса_или потока


1. Чтение HTTP запроса
   worker получил с помощью системного вызова accept новое сетевое соединение с клиентом
   Цикл начинается с того, что worker читает из этого соединения HTTP-запрос
   и парсит его

2. Выбор virtual host
   после чтения HTTP запроса происходит выбор virtual-host
   фактически определяется часть конфига, которая отвечает за данный запрос
   virtual-host определяется на основе заголока Host (но это при ответе)

3. Выбор location
   после выбора virtual host выбирается location
   location - более селка часть конфига, которая отвечает за обработку конкретной группы урлов (URLs)

   когда location выбран web-сервер может определить какой конкретно файл нужно отдавать
   это делается с помощью склеивания url и определённого пути который указан внутри location
   так называемый document root

4. Провера доступа
   когда мы определили конкретный файл, который собираемся отдавать
   web-сервер определяет права доступа
   проверка прав доступа состоит из нескольких частей
   1 - web-серверу можно задать определённые правила по ip адресам
       каким клиентам можно отдавать, а каким нельзя вообще, это задаётся в конфиге
   2 - можно потребовать авторизацию в виде логина и пароля, это также задаётся в конфиге
   3 - сервер просто проверяет доступ к файлу на диске (банальынй доступ к файловой системе)
   Если доступа нет 5 и 6 пункт пропускются и сразу посылается HTTP ответ с кодом 403 forbidden


5. Чтение файла
   Если доступ есть, то происходит чтение файла с диска
   здесь применяются разные методы
   считываем файл с диска, применяем различные выходные фильтры

6. Применение фильтров
   выходные фильтры - сжатие gzip, или отправка документа по частям, если документ большой
   уставливаем заголовки ответа, например Content-Type (критически важный заголовок)

7. Отправка HTTP ответа
   web-сервер отправляет HTTP ответ,
   причём если файл большой, этот ответ может отправляться по частям:
        сначала заголовки
        потом тело файла небольшими кусочками (но это не всегда так, а если файл большой)

8. Запись Access Log
   записывается информация - кому отправили документ, какой отправили документ,
   с каким кодом ответа, и прочая информация

9. Очистка
   очистка памяти (каких-то внутренних структур, которые мы выделяли)

10. Цикл замкнулся, снова Чтение HTTP запроса



2.--------------------- Моудльная архитектура

web сервера - сложный грамоздкий софт, и они склонны к расширению
в HTTP много разных фич, короче он расширяемый
для того чтобы обеспечить лёгкость и простоту изменения кода web-сервера его делают модульным

Внутри web-сервера выделятся

1. ядро
   ядро отвечает за ввод-вывод данных (чтение запроса, отправку ответа,), парсинг HTTP заголовков
   за работу с протоколом HTTP
2. модули
   модули добавляют функционал web-серверу, причём они могут добавлть его на различных этапах
   модули могут:
        - загружаться динамически
           LoadModule - директива apache с помощью которой можно загрузить shared библиотеку
        - модули могут быть вкомпилированы в код сервера (в nginx это так)

   после того как модель добавлен динамически или скомпилирован внутри сервера
   этот модуль добавляет дополнительные директивы, т.е. некоторые опции в конфиг web-сервера

   модуль регистрирует свои обработчики на этапах цикла, который мы разобрали выше

   Допустим этап проверака доступа
   Проверку доступа можно осуществлять:
       1. с помощью radius в linux (?)
       2. проверку доступа по логину и паролю можно осуществлять делая запрос в базу данных
       3. на основе ip адреса

       Эти модули регистрируют свои функции как обработчики, на этап "4. Проверка доступа" цикла выше
       Когда ядро сервера доходит до этапа "4. Проверка доступа" (из цикла)
       оно вызывает все три обработчика передавая им специальный объект запроса
       (структура в памяти со всей информацией о текущем запросе, аналог request в python)
       эти три модуля выполняют работу, проверяют авторизацию
       после чего они отдают ядру команду, что можно дальше выполнять обработку
       либо, что её следует закончить (нет доступа)
       таким образом наш код разделяется между ядром и модулями,которые делают дополнительный функционал


 - web-сервер - не монолитный
 - Динамическая загрузка модулей - LoadModule (директива apache с помощью которой можно загрузить shared библиотеку)
 - Этап обработки запроса и модули
 - Дополнительные директивы, контексты
 - Примеры модулей:
        mod_mime - определяет mime-тип (Content-Type документа), исходя из его расширения
        mod_mime_magic - делает тоже самое но исходя из первых байт документа (по сигнатуре),
        mod_autoindex - если сервер понимает, что запрос идёт не к файлу а к директории
                        может сгенерировать html страницу содержащую список файлов
        mod_rewrite - в проуессе запроса изменяет текущий url (влияет на обработку запроса, выбивается из той схемы),
        mod_cgi - в nginx его нет, в apache был популярен. вместо отдачи какого-то конкретного файла
                  он работает на этапе чтения отдачи файлов
                  вместо отдачи файла этот файл запускается и генерирует динамическикую страницу
                  (способ запуска динамических страниц)
        mod_perl - позволяет возможность писать скрипты к apache на языке perl,
        mod_gzip - сжамиает документы (gzip-сжатие)

И так, у сервера есть ядро, и есть модули, которые добавляют к нему полезный функционал
Как правило многие модули уже встроены при установке web-сервера
И у web-сервера описано внутренне API прзволяющее писать свои модули


"""
