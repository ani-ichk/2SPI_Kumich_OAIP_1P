import json


with open('file1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    age = 0
    cnt = 0
    for i in data.values():
        if i['city'] == 'Moscow':
            age += i['age']
            cnt += 1
    if cnt:
        print('Людей, живущих в Москве:', cnt)
        print('Их средний возраст:', age / cnt)
    else:
        print('Таких людей нет')