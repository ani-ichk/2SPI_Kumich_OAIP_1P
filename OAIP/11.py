# ввод с клавиатуры любого числа
a = float(input('Введите число: '))
# если число кратно 2, то оно является чётным
if a % 2 == 0:
    print('чётное')
# иначе число нечётное
else:
    print('нечётное')