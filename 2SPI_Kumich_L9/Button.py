class Button:
    def __init__(self, args):
        self.label = args[0]
        self.color = int(args[1])
        self.command = args[2]
        self.xcord = int(args[3])
        self.ycord = int(args[4])
        self.clickability = True

    # работает ли кнопка
    def is_work(self):
        if self.clickability:
            print('\033[32mКнопка активна\033[0m')  # зелёный текст
        else:
            print('\033[31mКнопка не активна\033[0m')  # красный текст

    # наведение курсора курсора на кнопку
    def button_hover(self):
        if self.clickability: # 4m - подчёркнутый текст
            print(f''' *Наведение на кнопку*
Кнопка: \033[4;{self.color}m{self.label}\033[0m
Инструкция: {self.command}
\033[3m(щёлкните 1 раза для действия или 2 для активации/дизактивации кнопки)''') # 3m - курсив

        else: # 37m - белый цвет текста
            print(f''' *Наведение на кнопку*
Кнопка: \033[47m{self.label}\033[0m
Инструкция: {self.command}
\033[37mкнопка не активна\033[0m
\033[3m(щёлкните 1 раза для действия или 2 для активации/дизактивации кнопки)\033[0m''')

    # нажатие
    def clicking(self, cnt_click):
        if self.clickability:
            if cnt_click == 1:
                print(f''' *Нажатие на кнопку*
Кнопка: \033[1;{self.color}m{self.label}\033[0m
Действие: {self.command}''') # 1m - жирный текст
            elif cnt_click == 2:
                self.clickability = False
                print(f''' *Кнопка была дизактивирована*
Кнопка: \033[47m{self.label}\033[0m''') # 47m - белый фон
            else:
                print('Неверное число нажатий')

        else:
            if cnt_click == 1:
                print(f''' *Нажатие на кнопку*
Кнопка: \033[47m{self.label}\033[0m
Действие: не может быть совершено, т.к \033[31mкнопка не активна\033[0m''')  # 1m - жирный текст
            elif cnt_click == 2:
                self.clickability = True
                print(f''' *Кнопка была активирована*
Кнопка: \033[{self.color}m{self.label}\033[0m''')  # 47m - белый фон
            else:
                print('Неверное число нажатий')