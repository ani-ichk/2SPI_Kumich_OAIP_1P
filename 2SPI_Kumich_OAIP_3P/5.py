# просим ввести любое число
num = float(input('Введите число: '))
# пока какое-то из условий не выполнится...
while True:
    if num == 0:  # если введённое число = 0 - прекращаем выполнение цикла
        break
    elif num % 3 == 0 and num % 7 == 0:  # если число кратно 3 и 7, то выводим 'Караул!'
        print('Караул!')
    elif num % 3 == 0 and num % 7 != 0:  # если число кратно 3 и не кратко 7, то выводим 'несчастливое'
        print('несчастливое')
    elif num % 7 == 0 and num % 3 != 0:  # если число кратно 7 и не кратко 3, то выводим 'опасное'
        print('опасное')
    else:  # не одно из условий не совпадает - просто выводим само число
        print(num)
    num = float(input('Введите число: ')) # ...запрашиваем ввод любого числа
