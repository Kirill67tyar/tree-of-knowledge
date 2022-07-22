"""
------------------------------- Git --------------------------------------
sources:


    titles


    in Python


    вопросы


-----------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------
Git - система контроля версий

----- merging (слияние)
      Очень важное преимущество Git, а может вообще для чего он нужен

      Git берёт на себя слияние разных версий файлов

      Процесс слияния назвается merging. (merge - сливаться, merging - слияние)
      Может проводиться автоматически или в ручном режиме.

      два человека работают над одним и тем же файлом, и потом
      посылают его на удалённый репозиторий
      Git попытается слить два файла в один, и чаще всего у него получится

----- Git - система контроля версий
      У нас есть вся история изменений файлов.
      Мы можем вернуться к любой версии нашего проекта

----- Централизованный или распределённый подход

        show:
        C:\Users\kiril\Desktop\Job\tree-of-knowledge\Git\media\централизованный_или_распределённый_подход

      Централизованный подход - кодгда данные хранятся только в одном месте на сервере
      Распределённый подход - есть версия на сервере, но у каждого разработчика
      есть полная копия у себя на компьютере
      Git является распределённой системой контроля версий

      Преимущетсва:
        - можно вносить изменения в проект будучи в offline
        - безопаснее. если что-то случится с центральным сервером, то версии проекта
          (возможно даже целиком) останутся у программистов


----- Конфигурация Git на компьютере
      после установки нужно произвести конфигурацию

            git config --global user.name "Kirill Bogomolov"
            git config --global user.email "kirillbogomolov.ric@gmail.com"
            git config --global color.ui true

      git config --global color.ui true - меняет цветовую схему Git,
      чтобы она была более красивой и читабельной

      При создании контрольных точек Git будет
      помечать твою контрольную точку email, именем и фамилией

----- Хранения в Git
      Git хранит изменения в виде снимков проекта во времени
      В отличие от других систем контроля версий Git не хранит какие-то
      отдельные изменения, которые произошли в файлах
      Он каждый раз копирует проект целиком
      И копия проекта (какой-то версии проекта), называется снимком
      Единственный момент, если файл не поменялся, то Git не будет его копировать
      а сошлётся на предыдущую версию файла

      !!!                                                                           !!!
        Каждая версия в гите (каждый коммит) это отдельный снимок проекта во времени
      !!!                                                                           !!!

----- Базовая работа с Git

      1. вы создали файл -  статус "untracked" (неотслеживаемый)
      или
      1. вы изменили файл -  статус "modified" (изменённый)
      2. git add -  статус "staged" (подготовленный)
      3. git commit -  статус "committed" (зафиксированный, подтверждённый) (commit - совершить)

      Варианты добавления файлов в staged:
          git add . - все в текущей директории, и те что ниже
          git add <file name>.py[.txt.js и тд] - добавить какой-либо файл в текущей директории
          git add <file name>.py <another file>.js - добавить несколько файлов по имени
          git add *.py - добавить все файлы в текущей папке с расширением .py
          git add some_dir/ - добавляет все файлы в папке some_dir
          git add some_dir/*.py - добавляет все файлы в папке some_dir с расширением .py
          git add "*.py" добавляет все файлы в проекте с расширением .py


----- Как Git работает с изменёнными файлами
      допустим у нас есть срока:
        s = 'some value'
      допустим мы изменили эту строку
        s = 'some value with changes'
      Git воспримит это изменение так,
      мы удалили строчку s = 'some value'
      и написали новую строчку s = 'some value with changes'
      несмотря на то, что мы просто продолжили строку


Команды:
git init - инициализация Git
git status - узнать текущий статус репозитория
git add - перевести файлы в состояние staged
            add <file name>.py[.txt.js и тд]
            add <file name>.py <another file>.js
            add *.py
            git add some_dir/
            git add some_dir/*.py
            git add "*.py"
git commit -m "some message" - делает снимок (слепок) репозитория
git log - позволяет просмотреть всю историю commit'ов
git diff - показывет разницу между текущим неотслеживаемым состоянием
           репозитория и последним снимком репозитория
           git diff - все различия и staged и untracked
           git diff --staged - разница между текущим отслеживаемым
                               состоянием репозитория и последним
                               снимком репозитория
           git diff <commit id> - разница между текущим состоянием репозитория
                                  и указанным снимком репозитория (коммитом)














-----------------------------------------------------------------------------------------------------
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/stanruss/название.git
git push -u origin master

git log --oneline - посмотреть все коммиты.
git checkout . - восстановить все.
git checkout "код коммита" - вернуть до состояния этого коммита.
git checkout master - вернуться в ветку мастер.

Восстановить файлы на локальном компьютере:
git fetch --all
git reset --hard origin/master или git reset --hard origin/<название_ветки>

git add text.txt - Добавить файл в репозиторий
git rm text.txt - Удалить файл
git status - Текущее состояние репозитория (изменения, неразрешенные конфликты и тп)
git commit -a -m "Commit description" - Сделать коммит
git push origin - Замерджить все ветки локального репозитория на удаленный репозиторий
git push origin master - Аналогично предыдущему, но делается пуш только ветки master
git push origin HEAD - Запушить текущую ветку, не вводя целиком ее название
git pull origin - Замерджить все ветки с удаленного репозитория
git pull origin master - Аналогично предыдущему, но накатывается только ветка master
git pull origin HEAD - Накатить текущую ветку, не вводя ее длинное имя
git fetch origin - Скачать все ветки с origin, но не мерджить их в локальный репозиторий
git fetch origin master - Аналогично предыдущему, но только для одной заданной ветки
git checkout -b some_branch origin/some_branch - Начать работать с веткой some_branch (уже существующей)
git branch some_branch - Создать новый бранч (ответвится от текущего)
git checkout some_branch - Переключиться на другую ветку (из тех, с которыми уже работаем)
git branch # звездочкой отмечена текущая ветвь - Получаем список веток, с которыми работаем
git branch -a # | grep something - Просмотреть все существующие ветви
git merge some_branch - Замерджить some_branch в текущую ветку
git branch -d some_branch - Удалить бранч (после мерджа)
git branch -D some_branch - Просто удалить бранч (тупиковая ветвь)
git show d8578edf8458ce06fbc5bb76a58c5ca4a58c5ca4 - Изменения, сделанные в заданном коммите
git push origin :branch-name - Удалить бранч из репозитория на сервере
git reset --hard d8578edf8458ce06fbc5bb76a58c5ca4a58c5ca4 - Откатиться к конкретному коммиту и удалить последующие (хэш смотрим в «git log»)
git push -f - залить на сервер измененные коммиты
git clean -f - Удаление untracked files
--------------------------------------------------------------------------------------------------------------------
"""