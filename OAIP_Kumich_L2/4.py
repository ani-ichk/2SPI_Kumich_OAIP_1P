import json


with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    country = ''
    latitude = ''
    longitude = ''

    if 'response' in data and 'GeoObjectCollection' in data['response']:
        res = data['response']['GeoObjectCollection']['featureMember']
        if res:
            geo_object = res[0]['GeoObject']
            pos = geo_object['Point']['pos'].split()
            longitude = float(pos[0])
            latitude = float(pos[1])
            meta_data = geo_object['metaDataProperty']['GeocoderMetaData']
            country = meta_data.get('CountryName')

    print(f'Страна: {country}, координаты: долгота - {longitude}, широта - {latitude}')