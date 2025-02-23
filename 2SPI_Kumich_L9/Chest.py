class Chest:
    def __init__(self, open=False):
        # Атрибуты
        self.isOpen = open  # открыт/закрыт
        self.content = {}  # содержимое

    def open_chest(self):
        self.isOpen = True
        return f'Сундук открыт. Его содержимое:\t{self.content}'

    def close_chest(self):
        self.isOpen = False
        return f'Сундук закрыт.'

    def add_thing(self, thing, cnt=1):
        sum_val = sum(self.content.values())  # заполненное место
        check = thing in self.content  # проверка на нахождение предмета в сундуке

        # Если сундук открыт
        if self.isOpen:
            # с добавлением такого кол-ва сундук не переполнится
            if sum_val + cnt <= 42:
                # предмет уже есть в сундуке
                if check:
                    self.content[thing] += cnt
                # предмета нет в сундуке
                else:
                    self.content[thing] = cnt
            # с добавлением такого кол-ва сундук переполняется
            else:
                return f'В сундуке не хватает места для такого количества. Осталось: {42 - sum_val + cnt}.'
        # сундук закрыт
        else:
            return 'Сундук закрыт.'

        # вывод содержимого сундука
        return self.content

    # удаление вещи
    def removal(self, thing, cnt=1):
        check = thing in self.content

        # сундук открыт
        if self.isOpen:
            # такая вещь есть в сундуке
            if check:
                # запрашиваемое количество = всему кол-ву вещи => удаляем из словаря в целом
                if cnt == self.content[thing]:
                    del self.content[thing]
                # вытаскиваем не полностью, а только запрашиваемое кол-во
                elif cnt < self.content[thing]:
                    self.content[thing] -= cnt
                # запрашиваемого кол-ва нет в сундуке
                else:
                    return f'В сундуке нет такого количества, {thing}: {self.content[thing]}'
            # такой вещи нет в сундуке
            else:
                return 'В сундуке нет этой вещи'
        else:
            return 'Сундук закрыт'

        # вывод содержимого сундука
        return self.content