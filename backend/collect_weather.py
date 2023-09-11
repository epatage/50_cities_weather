import requests
import time
import sqlite3

APPID = 'b55a9ba478028ce2cea598edde9a7960'
UNITS = 'metric'
LANG = 'ru'
DB_PATH = "/app/db.sqlite3"
ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
RETRY_PERIOD = 3600


def get_weather(city):
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
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        response = cur.execute('SELECT id, name FROM cities_city;')
        con.commit()

    return response


def add_weather(city, temp=None, pressure=None, dt=None, humidity=None):
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        params = (dt, pressure, humidity, city, temp)

        cur.execute('''
        INSERT INTO weather_weather(dt, pressure, humidity, city_id, temp)
            VALUES (?, ?, ?, ?, ?);
        ''', params)

        con.commit()


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
