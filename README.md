## Создание проекта
1. requirements.txt (Зависимости)
2. `django-admin startproject name_project .`
3. Настройка
  
    * `TIME_ZONE = 'Europe/Moscow'`
    * `LANGUAGE_CODE = 'ru-ru'`
    * `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
    * `ALLOWED_HOSTS = ['localhost']`

4. `python manage.py migrate` (Создание БД)
5. Запуск на localhost `python manage.py runserver 127.0.0.1:5000`

## Создание приложения
1. `python manage.py startapp blog`

2. `INSTALLED_APPS = [ ..., 'blog', ]`

## Heroku
1. `heroku git:remote -a geraldina-blog`
2. Procfile, Procfile.windows
3. `heroku local web -f Procfile.windows`
4. Зависимости requirements.txt

    * gunicorn
    * django-heroku

5. `ALLOWED_HOSTS = ['localhost', 'geraldina-blog.herokuapp.com']`
6. settings.py

    ```
    import django_heroku
    ...
    django_heroku.settings(locals())
    ```

> ## Django
> * Собрать статические файлы в STATIC_ROOT `python manage.py collectstatic`

## Создание модели (в blog/models.py)

* Model fields:
https://docs.djangoproject.com/en/1.11/ref/models/fields/

## Создание таблиц моделей
1. `python manage.py makemigrations` (Создание файла с миграцией для базы данных)

2. `python manage.py migrate` (Добавление модели в базу данных)

## Администрирование Django
1. Чтобы модель стала доступна на странице администрирования, нужно её зарегистрировать (admin.py) `admin.site.register(<Model>)`. 
    * Страница http://127.0.0.1:5000/admin/
2. Создание superuser
    * `python manage.py createsuperuser`

## Heroku
1. A database is an add-on `heroku addons`

2. DATABASE_URL `heroku config` `heroku pg:credentials:url DATABASE`

3. postgres `heroku pg`

4. `heroku run python manage.py migrate` if it is showing ETIMEDOUT then your port 5000 is blocked

5. heroku run python manage.py createsuperuser

## Создание страниц
1. Добавление URL

2. Добавление view

3. Добавление html