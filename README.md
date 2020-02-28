## Создание проекта
1. requirements.txt (Зависимости)
2. `django-admin startproject name_project .`
3. Настройка
  
    * `TIME_ZONE = 'Europe/Moscow'`
    * `LANGUAGE_CODE = 'ru-ru'`
    * `STATIC_ROOT = os.path.join(BASE_DIR, 'static')`
    * `ALLOWED_HOSTS = ['localhost', 'site.com']`

4. `python manage.py migrate` (Создание БД)
5. Запуск на localhost `python manage.py runserver 127.0.0.1:5000`
## Создание приложения
1. `python manage.py startapp blog`