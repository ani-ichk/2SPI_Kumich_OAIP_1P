# ввод с клавиатуры ширины плота
a = int(input('ширина плота: '))
# если сумма 1 и 3 цифр при делении на 8 не даёт остаток ноль(число не кратно 8) и 2 цифра равна 3, то вывести 'Подходит'
if (((a // 100) + (a % 10)) % 8 != 0) and (a % 100 // 10 == 3):
    print('Подходит')
# иначе вывести через пробел сумму 1 и 3 цифр и 2 цифру
else:
    print(a // 100 + a % 10, a % 100 // 10)