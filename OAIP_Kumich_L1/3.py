with open('text1.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    if text:
        even = [j.strip() for i, j in enumerate(text) if i % 2 == 1]
        odd = [j.strip() for i, j in enumerate(text) if i % 2 == 0]
        print('\n'.join(even))
        print('\n'.join(odd))
    else:
        print('Файл пуст')