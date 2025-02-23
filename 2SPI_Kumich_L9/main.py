from Chest import Chest
from Button import Button
from Tamagotchi import Tamagotchi


def main():
    print(0)



if __name__ == '__main__':
    # СУНДУК
    chest = Chest(True)
    print(chest.add_thing('яблоко', 2))
    # КНОПКА
    button = Button(input('''Ведите: текст, цвет кнопки:
    \033[40m40 - чёрный\033[0m
    \033[41m41 - красный\033[0m
    \033[42m42 - зелёный\033[0m
    \033[47m43 - белый\033[0m
    \033[44m44 - синий\033[0m
команду и координаты x и y
''').split(', '))
    button.button_hover()

    # ПИТОМЕЦ
    cat = Tamagotchi('Tomas', 'black')

    cnt_afk = 4
    while cat.is_life():
        action = input('''Выберите действие:
        1. Показатели питомца
        2. Кормление (перечислите продукты)
        3. Уложить спать
        4. Развлечение
    ''')
        if action == '':
            cnt_afk -= 1
            if cnt_afk == 0:
                break
            else:
                print('Возвращайтесь скорее ⸜(´ ꒳ `)⸝')
                cat.afk()
        elif int(action) == 1:
            cat.condition()
        elif int(action) == 2:
            cat.feeding(input('Питомцу можно: молоко, бургер, пиццу, кока-колу, брокколи и торт').split())
        elif int(action) == 3:
            cat.sleeping()
        elif int(action) == 4:
            what_game = int(input('Выберите развлечение: 1 - Догонялки, 2 - Музыка, 3 - Качалка'))
            if 0 < what_game < 4:
                cat.playing(what_game)
            else:
                print('Неверный ввод')
        else:
            print('Неверный ввод')