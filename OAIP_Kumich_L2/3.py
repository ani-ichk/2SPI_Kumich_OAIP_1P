import json


with open('my_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

    print('Текущие данные:')
    for key, value in data.items():
        print(f'{key}: {value}')

    key = input('Введите название ключа, значение которого хотите изменить: ')

    if key in data:
        value = input('Введите новое значение: ')
        data[key] = value
        print('Данные успешно обновлены.')
        for key, value in data.items():
            print(f'{key}: {value}')
    else:
        print('Такого ключа нет в данных.')

with open('my_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)