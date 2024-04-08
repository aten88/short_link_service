# short link service - сервис укорачивания ссылок с web-страницей и API.
Его задача — укорачивать и ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или генерирует сервис самостоятельно.

[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/)
[![Jinja2](https://img.shields.io/badge/-Jinja2-464646?style=flat&logo=Jinja&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![Flask](https://img.shields.io/badge/-Flask-464646?style=flat&logo=Flask&logoColor=ffffff&color=043A6B)](https://www.djangoproject.com/)
[![SQLAlchemy](https://img.shields.io/badge/-SQLAlchemy-464646?style=flat&logo=SQLAlchemy&logoColor=ffffff&color=043A6B)](https://www.postgresql.org/)
[![REST](https://img.shields.io/badge/-REST-464646?style=flat&logo=REST&logoColor=ffffff&color=043A6B)](https://www.django-rest-framework.org/)


## Ключевые возможности сервиса
- Генерация коротких ссылок и связь их с исходными длинными ссылками
- Переадресация на исходный адрес при обращении к коротким ссылкам
- /api/id/ — POST-запрос на создание новой короткой ссылки;
- /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору.

Доступны web и api интерфейсы.

## Технологии
- Python 3.11
- Flask 2.0.2
- Jinja2 3.0.3
- SQLAlchemy 1.4.29

## Использование
Клонировать репозиторий и перейти в него в командной строке:
- `git clone git@github.com:aten88/yacut.git`
- `cd yacut`

Cоздать и активировать виртуальное окружение:
- `python3 -m venv venv`
    - Если у вас Linux/macOS
        - `source venv/bin/activate`

    - Если у вас Windows
        - `source venv/scripts/activate`

Обновить пакетный менеджер pip и установить зависимости из файла requirements.txt:
- `python3 -m pip install --upgrade pip`
- `pip install -r requirements.txt`

Создать файл .env в корне проекта с переменными окружения:
- `FLASK_APP=имя пакета приложения "somename_pack_app"`
- `FLASK_ENV=статус типа разработки "some_development_status"`
- `DATABASE_URI=тип подключаемой БД "some_db_name:///db.some_type_db"`
- `SECRET_KEY=секретный ключ приложения FLASK "SomeXXXSecretKey"`

Создать БД и применить миграции:
- Создать репозиторий для миграций: `flask db init`
- Создать миграции:  `flask db migrate -m "some comment by migrate"`
- Обновить БД: `flask db upgrade`

Запустить приложение Yacut:
- `flask run`

Автор: Алексей Тен
