class Tamagotchi:
    def __init__(self, name, color):
        if len(name) == 0 or len(name) > 10:
            print('Имя не подходит. Доступная длина - от 1 до 10 символов')
        else:
            self.name = name
            self.color = color
            self.health = 100    # 0 - смерть
            self.happiness = 10
            self.hanger = 10     # 100 - смерть
            self.sleepiness = 0  # 100 - смерть
            self.life = True



    # состояние питомца
    def condition(self):
        print(f'''
        ★｡*:{self.name}:゜★｡
    Окрас: {self.color}
    Здоровье: {self.health}
    Настроение: {self.happiness}
    Голод: {self.hanger}
    Сонливость: {self.sleepiness}
    Жизнь: {self.life}''')

    # проверка жив или мёртв
    def is_life(self):
        n = (10 - len(self.name)) // 2
        m = n
        if len(self.name) % 2 != 0:
            m += 1
        grave = f'''
        ▂ ▂ ▂ ▂ ▂ ▂ 
        │  R.I.P.  │
    ✿✿ │{' ' * n + self.name + m * ' '}│ ✿✿
    ~~~~~~~~~~~~~~~~~~~'''
        if self.health < 1:
            print('Питомец заболел и умер (っ╥╯﹏╰╥c)', grave, sep='\t')
            self.life = False
        elif self.hanger > 99:
            print('Вы заморили питомца голодом (⋟﹏⋞)', grave, sep='\t')
            self.life = False
        elif self.sleepiness > 99:
            print('Питомец умер от недосыпа', grave, sep='\t')
            self.life = False
        return self.life

    # кормление
    def feeding(self, food):
        if food == 'лекарства':   # лечение
            self.health += 30

        elif self.hanger < 70:   # кормление
            if self.sleepiness < 70:
                for i in food:
                    if i == 'бургер':
                        self.hanger -= 25
                        self.health -= 5
                        self.sleepiness += 10
                        print('Вы покормили питомца o(>ω<)o')
                    elif i == 'брокколи':
                        self.hanger -= 10
                        self.health += 10
                        self.happiness -= 5
                        print('Бе (＞﹏＜)')
                    elif i == 'пицца':
                        self.hanger -= 30
                        self.health -= 4
                        self.sleepiness += 15
                        print('Вы покормили питомца (˶˃⤙˂˶)')
                    elif i == 'торт':
                        self.hanger -= 20
                        self.health -= 5
                        self.happiness += 30
                        print('Вы покормили питомца ヽ(>∀<☆)ノ')
                    elif i == 'молоко':
                        self.hanger -= 10
                        self.health += 5
                        self.sleepiness += 15
                        print('Вы напоили питомца (─‿‿─)')
                    elif i == 'кока-кола':
                        self.hanger -= 15
                        self.health -= 5
                        self.happiness += 5
                        print('Вы напоили питомца (*¯︶¯*)')
                    elif i != '':
                        self.health -= 30
                        print(f'Питомцам нельзя {i}! {self.name} отравился/-ась _:(´ཀ`」 ∠):_ дайте ему/ей лекарства.')
            else:
                print(f'''{self.name} хочет спать (￣ρ￣)..zzZZ
        Сонливость: {self.sleepiness}''')
        else:
            print(f'''{self.name} не хочет кушать (￣□￣」)
        Голод: {self.hanger}''')

    # сон
    def sleeping(self):
            self.sleepiness = 0
            self.hanger -= 30
            self.health += 10
            print('(￣ρ￣)..zzZZ')

    # развлечение
    def playing(self, game):
        if game == 1:
            self.happiness += 25
            self.sleepiness += 20
            self.hanger += 30
            print(self.name, 'побегал/-а с друзьями ε=ε=ε= ᕕ( ᐛ )ᕗ')
        elif game == 2:
            self.happiness += 30
            self.sleepiness += 10
            self.hanger += 15
            print(self.name, 'послушал/-а музыку ♫꒰･◡･๑꒱')
        elif game == 3:
            self.happiness += 20
            self.sleepiness += 20
            self.hanger += 20
            print('+1000 к силе ୧(๑•̀ㅁ•́๑)૭✧')


    def afk(self):
        self.health -= 10
        self.happiness -= 20
        self.hanger += 30
        self.sleepiness += 20