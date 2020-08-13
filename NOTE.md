## Создание проекта
1. requirements.txt (Зависимости)
2. `django-admin startproject blog_project .`
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
> * Собрать/обновить статические файлы в STATIC_ROOT `python manage.py collectstatic` (Сервера могут оптимизировать использование статических файлов так, чтобы они быстрее загружались. Поэтому после изменения статических файлов нужно дать серверу команду обновить их)

## Создание модели (в blog/models.py)

1. Model fields:
https://docs.djangoproject.com/en/1.11/ref/models/fields/

    ### Создание таблиц моделей
    * `python manage.py makemigrations` (Создание файла с миграцией для базы данных)

    * `python manage.py migrate` (Добавление модели в базу данных)

3. Чтобы модель стала доступна на странице администрирования, нужно её зарегистрировать (admin.py) `admin.site.register(<Model>)`. 
    * Страница http://127.0.0.1:5000/admin/    

## Администрирование Django

1. Создание superuser
    * `python manage.py createsuperuser`

## Heroku
1. База данных — это add-on `heroku addons`

2. DATABASE_URL `heroku config` или `heroku pg:credentials:url DATABASE`

3. Postgres `heroku pg`

4. `heroku run python manage.py migrate` if it is showing ETIMEDOUT then your port 5000 is blocked

5. `heroku run python manage.py createsuperuser`

## Создание страниц
1. Добавить URL

2. Добавить view

3. Добавить html

4. Использовать шаблоны Django `{{ }}` и `{% %}`, которые позволяют вставлять Python в HTML
https://docs.djangoproject.com/en/3.0/ref/templates/builtins/

5. Добавить CSS

    * https://getbootstrap.com/docs/3.4/components/

    * urls.py `urlpatterns = [...] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)`

   
## Создание форм (в blog/forms.py)

* Model forms:
https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/

## Администрирование

1. Защита страниц от неавторизованных пользователей 
    ```
    from django.contrib.auth.decorators import login_required
    @login_required
    ```
2. Вход в систему 
    * В `blog_project/urls.py` добавить `from django.contrib.auth import views` и `urlpath('accounts/login/', views.LoginView.as_view(), name='login')`

    * Создать шаблон для страницы входа в систему `blog/templates/registration/login.html`

    * `LOGIN_REDIRECT_URL = '/'`

    * Добавить кнопку входа в систему с `href="{% url 'login' %}"`

3. Выход из системы
    * В `blog_project/urls.py` добавить `path('accounts/logout/', views.LogoutView.as_view(next_page='/'), name='logout'),`

    * `LOGOUT_REDIRECT_URL = '/'`
    
    * Добавить кнопку выхода из системы с `href="{% url 'logout' %}"`
