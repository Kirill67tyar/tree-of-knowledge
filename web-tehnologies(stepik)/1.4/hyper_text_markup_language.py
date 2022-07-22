"""
--------------------- STEP 1 (2) -----------------------------------------------------------------------------

Базовый шаблон:

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="description" content="Сайт">

    <title>SOME TITLE</title>

    <link href="{% static 'font-awesome-4.7.0/css/font-awesome.min.css' %}" rel="stylesheet">
    <link href="{% static 'css/base.css' %}" rel="stylesheet">

</head>
<body id="the_body">

<script src="...../script.js"></script>
</body>
</html>

Особенности html разметки:

-- произвольный регистр <form ...> == <FORM ...>
-- аттрибуты могут быть как ключ:значение так и непарные: disabled, required
-- можно допускать дофига ошибок - браузер все равно попытается отобразить (не желательно)
-- даже парные теги можно прописывать без закрывающего тега (не желательно)

DOCTYPE нужен для определения версии html и возможно различных других форматов,
которые использовались до html

для HTML 5й версии используется doctype - <!DOCTYPE html>

HTML5 - последняя версия HTML. Принято, что просто будут ее дополнять,
а не выпускать новую версию.

!!! ИТОГ:********************************************************************************************

*****************************************************************************************************


--------------------- STEP 2 (3) -----------------------------------------------------------------------------
            HTML теги

В XML теги используются для задания структуры документа
В HTML теги - имеют значение, т.е. у html есть семантика

тег head - невидимый для страницы браузера тег, т.е. он содержит meta информацию

какие есть теги в head:

title - рядом с фавиконом отображение заголовка
meta - содержит информацию для user-агентов.
с помощью meta можно задавать http заголовки.
Зачем задавать заголовки для HTTP response?
Это может быть полезно, когда открываешь файл с диска.

Внутри тега <head> часто указывают загрузку связанных ресурсов (css, javascript).
соответственно link и script теги.

у тега link предназначение - указание связанных ресурсов. Связанные ресурсы бывают разные
но если это css то обязательно добавлять именованный аргумент (в html атрибут)
rel="stylesheet"
<link rel="stylesheet" href="css/style.css">

rel="alternate" - альтернативное представление данного документа, например RSS

тег script
src - путь до файла js
charset - указание кодировки
неименованный (без знаения) аргумент (атрибут) async - указывает, что js
нужно грузить асинхронно
Дело в том, что когда браузер читает html, когда он доходит до тега script
он останавливает парсинг, загружает файл javascript, после чего
продолжает парсинг документа
async указывает на то, что останавливаться не следует, а скрипт загружается в фоне

Загрузку css рекомендуется ставить в теге head (в начале, даже как можно раньше), а
загрузку javascript наооборот в конце документа (в идеале перед </body>)
это повышает скорость отрисовки страницы



--------------------- STEP 3 (4) -----------------------------------------------------------------------------

---------------Блочные теги:
h1-h6 - различные уровни заголовков
p - разбиение текста на параграфы
hr - горизонтальная линия (horizont)
pre - блок преформатированного кода, например исходный код
blockquote - цитирование длинного блока текста (quote - ковычки)
span - абстрактный строчный контейнер


тег div - абстрактный блочный контейнер

абстрактный значит то, что браузер тег div визуально не отображает
этот тег используется для создания структуры (как и многие другие),
но конкретно этот (как мне кажется) для стилей css и возможно id (css и js)\

Особенности блочных тегов:
-- они занимают всю предоставленную ширину
-- всегда наинаются с новой строки

Но! для блочного тега можно установить явно ширину, и он станет короче


---------------Строчные (inline) теги:
a - гиперссылка
em, i - акцентирование
strong, b - выделение
img - вставка изображений
sub - верхний индекс
sup - нижний индекс
span - абстрактный строчный контейнер


img - если вставить изображение, оно будет находиться внутри строки
span - по сути тоже что и div, но не блочный а строчный. Визуально никак себя не проявляет


Поведение строчных тегов противоположно поведению блочных
Особенности блочных тегов:
-- стараются занимать минимально возможную ширину
-- не прерывают строку
-- задать размеры строчных тегов нельзя

Размеры строчных тегов читаются автоматически по их содержимому.
Соответственно задать размер нельзя
хотя тег img исключение - задать ширину и высоту можно.
По сути img промежуточный тег
В span например нельзя задать ширину и длину

Ну и как последняя инфа на сегодня - деление на строчные и блочные теги условно



--------------------- STEP 4 (5) -----------------------------------------------------------------------------

здесь про ul/ol  li

и про table thead tbody tr


<table>
    <caption> название таблицы </caption> - для названия таблицы
    <thead> - для заголовка


        <tr> - строка

            <th> - ячейки (столбик) заголовков (как правило подсвечиваются)
            </th>

        </tr>
    </thead>

    <tbody> - для основной таблицы
        <tr> - строка

            <td> - столбик(ячейка если точнее)
            </td>

            <td colspan="2"> - два столбика объединяются в один
            </td>

            <td rowspan="2"> - два строки объединяются в одину
            </td>
        </tr>
    </tbody>
</table>

В это структуре три необходимых тега: table, tr, td.
Остальные необязательны

атрибуты tr
colspan="2" - две ячейки в одном столбце
rowspan="2" - две ячейки в одномй строке

Эти атрибуты позволяют объединять две (или больше) ячейки в одну


--------------------- STEP 5 (6) -----------------------------------------------------------------------------

Гиперссылка задается с помощью тега a
<a href="https//:some_ip:tcp_port/qweqwe" target="_blank"><img src='some url.png'></a>

target="_blank" в теге a означает что открывать новое окно в браузере при переходе

Внутрь гиперссылки можно разместить довольно сложную верстку

если указать в теге a атрибут name, то гиперссылка становится некликабельной
а значение этого name - это якорь.
как это выглядит:

<a href="#1" ...
...
где-то в другом месте документа
<a name="1"

если нажать на a с href="#1", то окно перенесется в место где a name=1,
а в конце url появится #1

если в теге a - href="javascript" браузер начнет испольнять указанный код javascript
(не знаю как это будет выглядеть)



--------------------- STEP 6 (7) -----------------------------------------------------------------------------

sources:
    https://www.w3schools.com/html/html_forms.asp

Формы

тег <form>


Тут все просто - формы используются для отправки данных на сервер

<form action="/add/" method="post" enctype="multipart/form-data" target="frame3">
    <input name="title" type="text">
    <input name="image" type="file">
    <input name="id" type="hidden">
    <input name="email" type="email" value="some_email@yandex.ru">
    <input name="password" type="password">

    <input type="hidden">

    <input type="submit" value="Отправить">
    <button type="submit" name="action" value="more">тоже отправить</button>
</form>

Внутри тега формы находятся непосредственно поля ввода данных,
ну или поля с уже пришедшими данными (для update)

!!! Визуально тег form себя никак не проявляет
Видны только поля ввода, а сам тег form используется как контейнер

-- атрибут - method
Метода может быть только два - GET или POST (регистр не важен)

put, patch, delete нельзя отправлять из html шаблона (во всяком лучае пока)

GET - дает нам get параметры (в заголовках HTTP и отображаются в url)
POST - в теле запроса (Значения отправляются в теле запроса в формате, указанном типом содержимого.)

!!!Любые изменения данных на сервере должны осуществляться с помощью метода POST!!!
!!!А получение данных с помощью метода GET (кроме авторизации)
Это очень важное правило но видимо только для HTML

Ведь в архитектуре RESTful API можно изменять данные также и с PUT, PATCH, DELETE


-- атрибут - action

в action указывается url (как относительный так и абсолютный)
на который будет отправлена форма


-- атрибут - target

указвает будет ли открыто новое окно


-- атрибут - enctype

Указывает на то, как будут закодированы данные формы при передаче на сервер

enctype="application/x-www-form-urlencoded" - для текста (по умолчанию)
enctype="multipart/form-data" - для передачи файлов

multipart/form-data - похожа на attachment при передачи файлов в электронных письмах

!!! Если нужно сделать форму для отправки файлов, то важно поменять enctype !!!

"application/x-www-form-urlencoded" - способы кодирования данных формы для передачи через url

обычно данные при GET запросе и POST запросе кодируются.
И вот application/x-www-form-urlencoded это способ кодирования этих данных.

смотри картинку:
C:\Users\User\Desktop\Job\learning_tree\tree-of-knowledge\web-tehnologies(stepik)\media\way_coding_for_http

Национальные символы недопустимы в url, в url допустима только латиница

Тела запроса это тоже касается.


--------------------- STEP 7 (8) -----------------------------------------------------------------------------

Содержимое form:

тег input может быть (иметь атрибуты):
    type="text"
    type="email"
    type="password"
    type="hidden"
    type="checkbox"
    type="radio"
    type="file"
    type="submit" (кнопка)
по сути input универсальное поле
type="hidden" не видно для пользователя вообще
hidden нужен для передачи данных, которые разработчик хочет скрыть от пользователя
но hidden никак не защищает данные
type="button" отображение галочки, переклюатель да/нет
type="file" - кнопка, которая предлагает выбрать файл, который будет загружен в форму

тег button - кнопка

textarea - многострочное поле ввода
с точки зрения программирования отличий от input type="text" только визуальные
textarea намного больше

select, option - выпадающий список

*** Атрибуты input
    name - имя с которым данный элемент попадет в запрос
    value="" - начальное значение, пользователь может изменить (может прийти вообще пустое)
    type
    placeholder="Search..." - подсказка для пользователя
    autocomplete="off"

autocomplete="off" - отключает подсказку
Браузер запоминает, что пользователь вводил в определенные поля
с определенными именами (возможно с помощью кеша или куки (скорее всего кеш))

"""