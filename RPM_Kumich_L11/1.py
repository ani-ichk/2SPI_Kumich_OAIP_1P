import requests

# задание 1
params = {'apikey': 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13',
          'll': '127.540927,50.256563',
          'spn': '0.004457,0.00219',
          'l': 'map'}
url = 'https://static-maps.yandex.ru/1.x/?'


response = requests.get(url, params)
if response.status_code == 200:
    with open('map.png', 'wb') as f:
        f.write(response.content)
        print('Успешно')
else:
    print(f'Ошибка: {response.status_code}')

# задание 2
import requests


url = 'http://geocode-maps.yandex.ru/1.x/'
params = {'apikey': '8013b162-6b42-4997-9691-77b7074026e0',
          'geocode': input('Адрес: '),
          'format': 'json'}

response = requests.get(url, params)
if response:
    data = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    postal_code = data['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
    if postal_code:
        print(postal_code)
    else:
        print('Почтовый индекс не найден')

# Москва, Красная площадь, 1


# задание 3
import requests


apikey = '78a45f73ed1310f62dfa194797931fa4'
city = 'Лондон'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric&lang=ru'
response = requests.get(url)
if response.status_code == 200:
    weather_data = response.json()
    temperature = weather_data['main']['temp']
    print(f"Температура в г.{city}: {temperature}°C")
else:
    print(f'Ошибка: {response.status_code}')