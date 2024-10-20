period = []  # список периодов
while True: # цикл, запрашивающий ввод и работающий пока не введут пустую строку
    age = input('возраст находки: ')
    if age == '':
        break
# условная конструкция, умножающая числовое значение от ввода и проверяющая к какому периоду относится полученное число
    if int(age) * 1000 in range(635000000, 2800000000):
        period.append('Proterozoic')  # если число входит в диапазон, то доб-ем его в список периодов
    elif int(age) * 1000 in range(300000000, 635000000):
        period.append('Paleozoic')
    elif int(age) * 1000 in range(145000000, 300000000):
        period.append('Mesozoic')
    elif int(age) * 1000 in range(145000000):
        period.append('Cenozoic')
    else:  # не подходит ни одному из диапазонов - период 'Archaea'
        period.append('Archaea')
print('\n'.join(period))   # выводим список как строки каждая с новой строки