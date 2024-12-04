try:
    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))
    print(f'{n1} / {n2} = {n1 / n2}')
except ValueError:
    print('Неверный ввод, одно из чисел не является целочисленным')
except ZeroDivisionError:
    print('Второе число не может быть 0')
finally:
    print('Выход из программы')