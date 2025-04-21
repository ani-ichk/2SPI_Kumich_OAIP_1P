import random


with open('text1.txt', encoding='utf-8') as f:
    text = f.readlines()
    if text:
        print(random.choice(text).strip())
    else:
        print('Файл пуст')