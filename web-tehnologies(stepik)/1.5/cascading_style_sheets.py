"""
--------------------- STEP 1 (2) -----------------------------------------------------------------------------

sources:
    https://devdocs.io/css/
    http://htmlbook.ru/
    https://github.com/Kirill67tyar/scraping-service-production/blob/master/src/scraping_service/static/css/style.css

CSS - язык описания стилей

В html есть теги для управления внешним стилем, но их явно не достаточно

Решение - Cascading Style Sheets

HTML создает стуктуру страницы
CSS - внешний вид каких либо отдельных элементов

Но css также является частью структуры (размер, длина прописывается там же)

.mid-play {
    padding: 13px 0px 0px 13px;
}

mid-play - здесь селектор
padding: 13px 0px 0px 13px; - стиль

Стили состоят из имени (ключа) и значения

У каждого стиля есть свои значения: цвет, url, какое-то слово
Желательно сверяться с документацией

3 способа подключения css стилей:

- подключение к файлу
<link rel="stylesheet" href="{% static 'font-awesome-4.7.0/css/font-awesome.min.css' %}">

- внутри тега <style></style>
(такие стили не кешируются)

- атрибут style в теге - <img style="margin: 3px" ...>


Какие бывают стили:

-- width, height -  размеры элемента
-- margin, padding -  границы и отступы (поле, набивка)
-- display, visibility -  режим отображения (отображать, видимость)
-- top, left, right, bottom -  расположение элемента (верх, лево, право, нижний)
-- background, background-color - фон элемента
-- font - управление шрифтом
-- text-align - выравнивание текста

Это были наиболее популярные стили. Но реальный список стилей намного больше
http://htmlbook.ru/css
https://devdocs.io/css/
Есть также множество версий css

!!!                                                         !!!
    Просто запомни, что для каждого элемента html (тега) свои стили
    а для каждого стиля свои параметры
    которые желательно сверять в документации
!!!                                                         !!!

Ну и вишенка на торте, многие стили отображаются разными браузерами по разному
Чем стиль ближе к последней версии css, тем больший шанс, что в разных браузерах
он будет отображаться по разному


--------------------- STEP 2 (3) -----------------------------------------------------------------------------

CSS селекторы

В css стили применяются к набору элементов

***** Классы и идентификаторы

Две важные концепции CSS идентификаторы и классы
#id - индентификатор элемента, должен быть уникален для всей страницы (одной web страницы)
.class - список классов элемента, классы могут повторяться

<div id="userpic"><img src="..."></div>
<button class="btn btn-main">Одобрить</button>

Атрибуты id и class могут быть указаны у совершенно любого HTML элемента.


***** Селекторы

Базовые селекторы:

-- Универсальный селектор
* { margin: 0px; padding: 0px; border: 0px; }

-- Имена тегов
p { margin-top: 10px; }

-- Имена классов (начинается с .)
.some-class { border: solid 1px gray; }

-- ID тегов (начинается с #)
#userpic { padding: 10px; }


* - выбирает вообще все элементы на странице. Используется редко

p { margin-top: 10px; } - в данном случае селектор p выбирет все параграфы на странице

.some-class - означает что этот серектор соответствует всем элементам, у которых есть класс some-class


* Сложные селекторы:

-- Контекстные (вложенные) селекторы
div.article a {text-decoration: underline;}

Селектор выше означает, что нужно выбрать все элементы a,
которые находятся внутри элементов div с классом article (! Пробел здесь не ставится - div.article)
насчет пробела очень важно, если там нет пробела, то это совместное применение селекторов
Логика проста:
если вначале стоит div То нужно выбрать все элементы с div на странице
если в начале стоит .article то выбрать все элементы с классов .article
а если они идет вместе, и не разделены пробелом (div.article), то выбрать
все div с классом article (div="article")
а дальше идет пробел и тег a. Это значит выбрать все элементы a внутри тега div с классом article
Пробел здесь играет решающую роль


-- Дочерние (вложенность = 1 уровень)
a > img {border: 2px;}

Данное обозначение означает выбрать все элементы img которые идут сразу внутри гиперссылки
Ключевое слово здесь СРАЗУ, т.к. уровень вложенности - 1, т.е. <a href="https//.."> <img src=""> </a>

-- Соседние
h2.sic + p {margin-left: 30px; }
+ в CSS означает после. Данный селектор означает выбрать все p которые идет после <h2 class="sic"></h2>
Насчет после, я так понимаю, что после того, как этот тег (h2) закроется

-- Группировка
h1, h2 {color: red;}
, в CSS является перечислением. Ну тут все понятно, для всех h1 и h2 сделать красный цвет



***** Псевдоклассы

a:visited - посещенная ссылка

a:link - непосещенная ссылка

div:hover - элемент при наведении мыши (hover - парить, свободный полет)

input:focus - элемент при получении фокуса (курсор мышки находится в поле)

li:first-child - выбирает первого потомка средт множества элементов


Псевдоклассы добавляет браузер, автоматически, в зависимости от некоторых условий.
к примеру к тегу a будет добавлен класс visited, после того, как на ссылку нажали и т.д.


***** Псевдоэлементы

Это настоящие теги, которые не присутствуют в исходном файле
Эти теги браузер создает автоматически сам, в зависимости от стилей
псеводэлемент after и before используются чаще всего

#el:after - виртуальный элемент сразу после #el
#el:before - виртуальный элемент, непосредственно перед #el

.jack-sparrow:before {
	content: "Captain";
	display: inline;
}

.jack-sparrow в данном случае класс. И автоматически, допустим перед span class=".jack-sparrow"
будет добавляться "Captain" (content)

У псевдоэлементов есть два важных свояйства - это content и display

content - это содержимое, что появится
display - задает режим отображения

Псевдоэлементы используются таки довольно часто.


--------------------- STEP 3 (4) -----------------------------------------------------------------------------

            Наследование и приоритеты стилей в CSS

Таки важная тема

Cascading в названии CSS означает наследование. (а вообще inheritance)

1 правило - Не все стили наследуются

что есть наследование:

<head>
    <style>
        body { color: darkgray; font-family: Arial; }
        p { font-size: 110% }
    </style>
</head>
<body>
	<p> Hello <a href="/">World</a></p>
</body>

Некоторые стили имеют свойство применяться не только к тому элементу, для
которого они написаны (определены в селекторах)
НО! и ко всем вложенным в него элементам.

В примере выше color: darkgray; и font-family: Arial; будет применяться
ко всем элементам p и a что вложены в тег body (основная страница)

Это и есть наследование

Такие стили как color и font-family есть у <p> и <a> тегов, (насчет h1, h..  не уверен)
У тега body же color и font-family нет


далее для тега <p> задан размер шрифта - 110% от родительского
этот стиль также наследуется и у гиперссылки будет тот же самый размер шрифта
(что странно, ведь он определен для тега p)

Стили наследуются внутрь по дереву html элементов

Как было написано, не все стили наследуются
Как правило наследуются стили связанные с оформлением текста, шрифта, цвета

Стили связанные с размерами, отступом и позиционированием как правило не наследуются

Общего правила нет, если нужно узнать наследуется или не наследуется стиль -
документация/google в помощь


***** Приоритеты стилей

Иногда бывает конфликт стилей. Допустим в примере выше мы добавим в стили тега p
color: red;
Но выше в body уже определен стиль color: darkgray;
Возникает конфликт стилей. Так какой же стиль будет использовать тег p?


В случае, если два разных стиля конфликтуют между собой,
применяется тот, что обладает большей специфичностью.
Если специфичность двух стилей совпадает, применяется тот,
что расположен ниже в HTML/CSS коде

Указание в значение стиля флага !important позволяет перекрыть проверку спцифичности
(является хаком)

Есть специальные правила расчета специфичности:

* id - 100 (самая высокая специфиность)
* классы и псевдоклассы - 10
* теги и псевдотеги - 1

Так, например, селектор ul.info ol + li обладает
специфичностью 13, а селектор li.red.level специфичностю 21 балл

Вывод такой: чем больше специфичность, тем больше вероятноть, что стиль будет применен

Отсюда есть правило (best practice):
     Низкую специфичность нужно определять для всей страницы и большинства тегов,
     А высокую - только для конкретных тегов, чтобы в случае чего можно было легко
     перебить специфичность для большинства.
     Чем ниже специфичность, тем проще и легче должны быть стили.



--------------------- STEP 4 (5) -----------------------------------------------------------------------------

Отображение (позиционирование) элементов

Есть стили, которые определяют расположение элементов на странице


***** режимы отображения элементов:

display: none - элемент невидим, не занимает места
Чаще всего используется совместно с javascript. при некоторых действиях пользователя его отображают

display: block - элемент занимает максимальную ширину, наинается с новой строки,
учитывая(!) width, height

display: inline - элемент занимает минимальную ширину, и не прерывает строку,
игнорируя(!) width, height

display: inline-block - блочный элемент, но не разрывает строку, примерно как img

Это далеко не все режимы отображения.


Отлиный пример разницы между div и span (между блочным и строным элементом):
сохрани в блокноте как html и открой в браузере:

    <div class="t">ONE</div>
    <div class="t">2</div>
    <span class="t">ONE</span>
    <span class="t">2</span>
    <style>
    .t {
        width: 150px; height: 100px;
        background: red; color: white;
        margin: 30px; padding: 4px;
    }
    </style>

Здесь мы видим, что строчной элемент span игнорирует width и height, а также отступы сверху и снизу,
слева и справа отступы есть (это margin: 30px;). У дива же все стили учтены.

Вывод - для позиционирования элементов, если нужно расположить элемент в каком-либо месте,
или разделить страницу на две части - логичнее использовать элементы display:block

Элементы со стилем display:inline используются в основном для выделения отдельных слов
внутри текста

Для того чтобы задать структуру страницы используются блочные элементы


***** стиль float

Изначально стиль float использовался для обтекания текста

Этот стиль позволяет задать обтекание какого-то конкретно блока

допустим есть картинка и у неё есть стиль float
где эта картинка будет всплывать в тексте:

float: left - всплывание влево
float: right - всплывание вправа
clear: both - отменяет всплывание, начиная с данного элемента, "проводит черту"

1 - Если у нас есть два одинаковых float элемента, допустим с right
то они выстроятся друг за другом
2 - float элементы не раздвигают контейнер. они его раздвигают, если он также float

<div class="outer">
    <div class="sqr fl"></div>
    <div class="sqr fl"></div>
    <div class="sqr fl"></div>
    <div class="sqr fl"></div>
    <div class="clr"></div>
    <div class="sqr fr"></div>
    <div class="sqr fr"></div>
    <div class="sqr fr"></div>
    <div class="sqr fr"></div>
</div>
<style>
    .outer { float: left; width: 300px; }
    .sqr { background: red; width: 70px; height: 70px; }
    .fl { float: left; }
    .fr { float: right; }
    .clr { clear: both; }
</style>

В теории это должно работать, на практике каких-то стилей не хватает

***** Позиционирование position

- position: static - обычное расположение (по умолчанию)
- position: relative - смещение относительно начального местоположения на странице
                       (relative - относительный)
- position: absolute - если родитель relative, absolute, или fixed -
                       относительно родителя, иначе - относительно начала докумнта
                       будет скролиться, прокручиваться вместе с самим документом
- position: fixed - относительна окна браузера
- top/right/bottom/left - отступы, могут быть отрицательными



--------------------- STEP 5 (6) -----------------------------------------------------------------------------

Важная проблема с которой сталкиваются web мастера - это необходимость
подогнать элемент друг к другу, если элемент чуть чуть выбивается из необходимого пожелания

В таком случае скоре всего стаит неправильное использваоние отступов,
либо незнание box-model

Какие отсупы есть у элементов?

смотри очень полезную картинку:
C:\Users\kiril\Desktop\Job\tree-of-knowledge\web-tehnologies(stepik)\1.5\1_5_6_отступы

padding - это внутренний отступ, отступ внутрь элемента (анг. padding - набивка)
border - граница элемента. У большинства элементов она нулевая (полоска нулевой ширины)
margin - это отступ наружу (анг. margin - допуск)

Все три эти величины padding, border, margin величины можно завдавать сходным образом.
Спопособы задания отступов для этих трёх элементов (margin заменить на border или padding ):

margin: 10px; - со всех сторон 10 пикселей
margin: 10px 5px; - первое число верхний и нижний, второе правый и левый
margin: 1px 2px 3px 4px; - если 4 числа то верхний, правый, нижний, левый (по часовой)
или конкретно каждую сторону уточнять
margin-left: 10px;
margin-right: 10px;
margin-top: 10px; - верх
margin-bottom: 10px; - низ

Для border и padding всё тоже самое просто заменить margin на border допустим


чтобы элементы не слиплялись друг с другом часто ставят margin-bottom: 5px;

В css длиной элемента является длина содержимого

А как сделать так, чтобы под шириной понимать содержимое + padding + border?

это позволяет сделать стиль box-sizing

box-sizing позволяет поменять то, как считается ширина

Варианты box-sizing:
- content-box(default)
- border-box

content-box - используется по умолчанию
border-box - ширина содержимого вместе с padding и border

размер margin + border + padding + содержимое часто называется box-model
в chrome есть инструмент, чтобы посмотреть на него

открывается он - посмотреть код -> внизу Computed




"""