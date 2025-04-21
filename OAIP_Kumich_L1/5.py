with open('text1.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    if text:
        bit = len(text) * 8
        byte = bit / 8
        kb = byte / 1024
        mb = kb / 1024
        gb = mb / 1024

        if kb < 1:
            print(f'Максимальная возможная величина - {byte} байт')
        elif mb < 1:
            print(f'Максимальная возможная величина - {kb} кб')
        elif gb < 1:
            print(f'Максимальная возможная величина - {mb} мб')
        elif gb >= 1:
            print(f'Максимальная возможная величина - {gb} гб')
    else:
        print('Файл пуст')
