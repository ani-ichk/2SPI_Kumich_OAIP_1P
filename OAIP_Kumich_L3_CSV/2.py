import csv


min_percent = float(input())
specialties = []

with open('vps.csv', 'r', encoding='utf-8') as file:
    # пропускаем первую строку (заголовок)
    lines = file.readlines()[1:]
    for i in lines:
        # разделяем строку по точке с запятой
        parts = i.strip().split(';')
        specialty = parts[0]
        percent_match = float(parts[4])
        if percent_match >= min_percent:
            specialties.append(specialty)

print('\n'.join(specialties))