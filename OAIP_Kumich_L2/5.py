import json


with open('test.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    ['metaDataProperty']['GeocoderMetaData']['Address']['country_code'] = 'Russia'
    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    ['metaDataProperty']['GeocoderMetaData']['Address']['postal_code'] = '00100'
    data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    ['metaDataProperty']['GeocoderMetaData']['Address']['formatted'] = 'Благовещенск, ул. Ленина, 104'

with open("test.json", 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
