import json

data = {
        'Фамилия': 'Алексеевич',
        'Имя': 'Дмитрий',
        'Отчество': 'Кузнецов',
        'Телефон': '+71234567890',
        'Год рождения': 2005,
        'Город рождения': 'Казань',
        'Место учёбы': 'КФУ'
}

with open('my_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
