# просим ввести числа через пробел
num = input('Введите числа через пробел: ')
# с помощью метода split() разделяем строку на отдельные элементы по пробелам и сохраняем их в новую переменную-список
num_list = (num.split(' '))
#преобразовываем элементы списка в числовые значения
num_list = list(map(float, num_list))
# создаём переменную минимального значения, которая равна первому элементу списка
min_num = num_list[0]
count = 1 # создаём переменную-счётчик, равную 1, тк счёт мы начнём со второго эл-та списка
# создаём цикл, перебирающий каждый эл-т списка, если он меньше мин. значения, то вписываем его как новое мин. значение
# цикл работает до тех пор, пока счётчик не превысит длину списка
while count < len(num_list):
    if num_list[count] < min_num:
        min_num = num_list[count]
    count += 1 # после проверки каждого эл-та прибавляем к счётчику 1 для проверки следующего эл-та списка
print(min_num) # выводим минимальное значение
