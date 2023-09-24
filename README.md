# Weather

## Описание

#### Сбор, обработка и хранение данных о погоде
При запуске приложения в контейнерах запускается модуль collect_weather.py, который с переодичностью раз в 60 минут
делает запросы к API сервису https://openweathermap.org,
получает данные о погоде в заранее обозначенных городах 
и записывает полученные данные в БД.



## Что использовалось

Django, PostgreSQL, Docker


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

Создать файл .env с переменными, указанными в 
файле .env.example:
```
cp .env.example .env
```
Для получения APPID необходима регистрация на https://openweathermap.org (после получения
ключ APPID активируется с задержкой).


Загрузить в БД список 50 городов

```
python manage.py download_cities --delete-existing
```


Запустить работу приложения и БД в контейнерах:

```
docker compose up -d
```

Проверить наполнение БД можно через инструменты просмотра БД 
или через django admin-панель, выполнив следующие шаги:
- создать пользователя
```
python manage.py createsuperuser
```
- запустить сервер разработки
```
python manage.py runserver
```
- пройти в admin-панель по url-адресу с данными суперпользователя
```
http://127.0.0.1:8000/admin/
```
При завершении тестирования приложения остановить работу контейнеров:

```
docker compose down
```

