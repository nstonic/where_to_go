# Куда пойти

Сайт для тех, кто ищет занятия на досуг
[Работающий прототип](http://nstonic.pythonanywhere.com/)

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Примените все миграции командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver`

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py`
и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `SECRET_KEY` — секретный ключ проекта
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки. По умолчанию выключен
- `ALLOWED_HOSTS` — Список допустимых доменов или IP-адресов, с которых допускается управление данным сайтом.
см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).
- `DATABASE` — однострочный адрес к базе данных. По умолчанию - `sqlite:///db.sqlite3`.
Это позволяет легко переключаться между базами данных: PostgreSQL, MySQL, SQLite — без разницы, нужно лишь подставить нужный адрес.
Больше информации в [документации](https://github.com/jacobian/dj-database-url). 

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
