#создаём пустой список
list = []
#добавляем элементы
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
#удаляем элемент списка с индексом 0
list.pop(0)
#производим срез списка
srez = list[0:4:2]
#переворачиваем список с помощью среза и метода
tsil = list[::-1]
list.reverse()
#делаем двумерный список
list2 = [6, 7, 8]
list.append(list2)
print(list)
#очищаем список
list.clear()
