with open('text1.txt', 'r', encoding='utf-8') as f:
    words = [i.strip() for i in f if i.strip()]
    if words:
        max_len = max(len(i) for i in words)
        long_word = [i for i in words if len(i) == max_len]
        print(*long_word)
    else:
        print('Файл пуст')