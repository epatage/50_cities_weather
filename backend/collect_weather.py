import requests
import time
import psycopg2
from backend.settings import DATABASES
from dotenv import load_dotenv
import os

load_dotenv()

# url-адрес API сервиса погоды
ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
# Период отправки запросов к API
RETRY_PERIOD = 3600
# Ключ API сервиса
APPID = os.getenv('APPID')
# Система измерений, передаваемая параметром в запросе к API
UNITS = 'metric'
# Язык ответа, передаваемый параметром в запросе к API
LANG = 'ru'

# Переменные базы данных
DB_NAME = DATABASES['default']['NAME']
DB_HOST = DATABASES['default']['HOST']
USER = DATABASES['default']['USER']
PASSWORD = DATABASES['default']['PASSWORD']

# Получение переменной хоста БД из окружения указанного в Dockerfile
CONTAINER_DB_HOST = os.environ.get('CONTAINER_DB_HOST')
# Изменение переменной хоста БД при запуске приложения в контейнере
if CONTAINER_DB_HOST:
    DB_HOST = CONTAINER_DB_HOST


def get_weather(city):
    """Запрос по API данных погоды в городе, который передается параметром."""

    url = f'{ENDPOINT}?q={city}&appid={APPID}&units={UNITS}&lang={LANG}'

    response = requests.get(url)
    json_response = response.json()

    main = json_response.get('main')
    temp = pressure = humidity = None
    if main:
        temp = main.get('temp')
        pressure = main.get('pressure')
        humidity = main.get('humidity')

    dt = json_response.get('dt')

    return temp, pressure, dt, humidity


def get_city():
    """Выборка всех городов из БД для передачи в функцию запроса погоды."""

    con = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=DB_HOST,
        database=DB_NAME)

    with con.cursor() as cur:
        cur.execute('SELECT id, name FROM cities_city;')
        response = cur.fetchall()
    con.commit()
    con.close()

    return response


def add_weather(city, temp=None, pressure=None, dt=None, humidity=None):
    """Добавление в БД данных погоды, полученных по запросу API и городу."""

    con = psycopg2.connect(
        user=USER,
        password=PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )
    cur = con.cursor()
    params = (dt, pressure, humidity, city, temp)

    query = '''
    INSERT INTO weather_weather(dt, pressure, humidity, city_id, temp)
        VALUES ('%s','%s','%s','%s','%s');
    '''
    cur.execute(query, params)

    con.commit()
    con.close()


def main():
    cities = tuple(get_city())

    while True:
        for city in cities:
            city_id, city_name = city[0], city[1]
            city_weather = ''
            try:
                city_weather = get_weather(city_name)
            except Exception as error:
                print(f'Ошибка: {error} на городе: {city_name}')
            try:
                add_weather(city_id, *city_weather)
            except Exception as error:
                print(f'Ошибка: {error} на городе: {city_name}')
            else:
                print(f'Погода добавлена для {city_name}')

        time.sleep(RETRY_PERIOD)


if __name__ == '__main__':
    main()
