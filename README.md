# Установка и использование (для Windows)
1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение (проект использует Poetry, за информацией по установке https://pythonchik.ru/okruzhenie-i-pakety/menedzher-zavisimostey-poetry-polnyy-obzor-ot-ustanovki-do-nastroyki).
3. Для работы программы необходимо установить зависимости, пропишите "poetry init" в командную строку.
4. Создайте файл .env. Введите туда свои настройки как указано в файле .env.sample.
5. Создайте базу данных ( Например, через консоль: 1 - psql -U postgres; 2 - create database online_studing; 3 - выход: \q)
6. Сделайте и примените миграции. 
    6.1 python manage.py makemigrations 
    6.2 python manage.py migrate
7. Можете загрузить тестовые данные: 
    7.1 python manage.py loaddata data_blog.json 
    7.2 python manage.py loaddata data_mails.json либо создать свои.
8. Создайте суперпользователя: python manage.py csu
9. Запустите сервер: python manage.py runserver
10. Зарегистрируйтесь на проекте, cоздайте своих клиентов, сообщения и саму рассылку. После создание рассылки нужно вызвать команду в терминале python manage.py runapscheduler
11. Настройка для кеша. Перед тем как использовать пакет redis внутри Django, не забудьте установить БД Redis. Для этого: в Linux используется команда sudo apt install redis или sudo yum install redis, в macOS — команда brew install redis, в случае с Windows воспользуйтесь инструкцией: https://redis.io/docs