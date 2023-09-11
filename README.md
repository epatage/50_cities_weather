# Weather

## Описание

Сбор, обработка и хранение данных о погоде

## Что использовалось

Django, Docker


### Как запустить проект:

Клонировать репозиторий:

```
git clone git@github.com:epatage/weather.git
```


Cоздать и активировать виртуальное окружение:
```
cd backned
```

```
python -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:


```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```
Загрузить в БД список 50 городов

```
python manage.py download_cities --delete-existing
```


Запустить работу приложения:

```
docker compose up
```

Проверить наполнение БД можно через инструменты просмотра БД 
или через django admin-панель, выполнив следующие шаги:
- создать пользователя
```
python manage.py createsuperuser
```
- пройти в admin-панель по url-адресу
```
http://127.0.0.1:8000/admin/
```


