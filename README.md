# Описание

Информационно-поисковая система для КыргызПатента

# Для запуска проекта

pip3 должен быть установлен.

После этого просто установите локальные зависимости, запустите миграцию и запустите сервер.

#  SearchSystem 

# Начало

Во-первых склонируйте репозиторий:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Создайте и активируйте виртуальное окружение:

    $ virtualenv venv
    $  $ cd venv/scripts/./activate
    
Установите зависимости:

    $ pip install -r requirements.txt
    
    
Затем проведите миграции:

    $ python manage.py makemigrations
    $ python manage.py migrate
    
    

И можно запускать сервер:

    $ python manage.py runserver

Для изменения СУБД в файле /KyrgyzPatent/settings.py находим раздел DATABASE и меняем на нужные параметры:

<img src="C:\Users\User\Desktop\Web2\KyrgyzPatent\SearchSystem\static\img\db.PNG"/>
