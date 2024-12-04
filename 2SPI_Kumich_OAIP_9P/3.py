while True:
    try:
        n1 = int(input('Введите первое число: '))
        n2 = int(input('Введите второе число: '))
        print(f'{n1} / {n2} = {n1 / n2}')
        break
    except ZeroDivisionError:
        print('Второе число не может быть 0')