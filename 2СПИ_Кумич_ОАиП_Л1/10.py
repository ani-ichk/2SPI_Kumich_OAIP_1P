#создаём пустое множество
a = set()
#создаём множество с элементами
b = set('fish')
#добавляем в пустое множество элементы
a.update('clown')
#выполняем объединение списков
a.union(b)
#выполняем пересечение списков
a.intersection(b)
#выполняем разность списков
a.difference(b)
#выполняем симметричную разность списков
a.symmetric_difference(b)
