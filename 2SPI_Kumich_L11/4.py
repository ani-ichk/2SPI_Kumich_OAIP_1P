import random


class Character:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.attack_power = 10
        self.stamina = 100

    def attack(self, enemy):
        if self.hp > 0:
            print(f'{self.name} атаковал {enemy.name} и нанёс {self.attack_power} урона')
            enemy.hp -= self.attack_power
            print(f'Здоровье {enemy.name}: {enemy.hp}')
        else:
            print(f'{self.name} мёртв')

    def info(self):
        print(f'''\033[35mИмя: {self.name}\033[0m
Здоровье: {self.hp}
Сила атака: {self.attack_power}
Выносливость: {self.stamina}''')


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name)
        self.energy = 0
        self.ulta = False

    def super_attack(self):
        if self.energy > 49:
            self.energy -= 10
            self.attack_power = 15

    def attack(self, enemy):
        if self.hp > 0:
            if self.ulta:
                print(f'{self.name} активирует ульту и наносит \033[32m{self.attack_power * 2.5}\033[0m урона')
                self.ulta = False
                self.energy = 0
                enemy.hp -= self.attack_power * 2
            else:
                if random.choice([True, False]):
                    self.super_attack()
                print(f'{self.name} атаковал {enemy.name} и нанёс \033[32m{self.attack_power}\033[0m урона')
                self.energy += 50
                enemy.hp -= self.attack_power
                self.attack_power = 10

                if self.energy == 100:
                    self.ulta = True
                    print(f'{self.name} готов атаковать ультой')
            print(f'Здоровье \033[31m{enemy.name}: {enemy.hp}\033[0m')
        else:
            print(f'{self.name} мёртв')


class Mage(Character):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 100

    def healing(self):
        if self.mana >= 40:
            self.hp += 10
            print(f'\033[32m{self.name} +10\033[0m здоровья')

    def attack(self, enemy):
        if self.hp > 0:
            if self.mana > 20:
                print(f'{self.name} использует магию и наносит \033[35m{self.attack_power * 1.5}\033[0m урона')
                self.mana -= 20
                self.hp += 5
                enemy.hp -= self.attack_power * 1.5
            else:
                if random.choice([True, False]):
                    self.healing()
                print(f'{self.name} не хватает маны для полной атаки')
                print(f'{self.name} наносит \033[35m{self.attack_power - 5}\033[0m урона своему врагу')
                self.mana += 10
                enemy.hp -= self.attack_power - 5
            print(f'Здоровье \033[31m{enemy.name}: {enemy.hp}\033[0m')
        else:
            print(f'{self.name} мёртв')


class Archer(Character):
    def __init__(self, name):
        super().__init__(name)
        self.arrows = 15
        self.energy = 0
        self.ulta = False

    def fire_arrow(self):
        if self.energy > 50:
            self.attack_power += 10
            print(f'Теперь стрелы горящие')

    def attack(self, enemy):
        if self.hp > 0:
            if self.arrows > 0:
                if self.ulta:
                    print(f'{self.name} атакует {enemy.name} двумя стрелами, нанося \033[34m{self.attack_power * 2}\033[0m урона')
                    self.arrows -= 2
                    self.energy = 0
                    self.ulta = False
                    enemy.hp -= self.attack_power * 2
                else:
                    if random.choice([True, False]):
                        self.fire_arrow()
                    print(f'{self.name} аткует {enemy.name}, нанося \033[34m{self.attack_power}\033[0m урона')
                    self.arrows -= 1
                    self.energy += 20
                    enemy.hp -= self.attack_power
                    self.attack_power = 10 # возвращаем силу атаки если стрелы стали горящими

                    if self.energy == 100:
                        self.ulta = True
                        print(f'{self.name} готов атаковать ультой')
                print(f'Здоровье \033[31m{enemy.name}: {enemy.hp}\033[0m')
            else:
                print('Стрел нет')
        else:
            print(f'{self.name} мёртв')




def battle(character1, character2):
    while character1.hp > 0 and character2.hp > 0:
        character1.attack(character2)
        if character2.hp > 0:
            character2.attack(character1)
    character1.info()
    character2.info()


warrior = Warrior('Воин')
mage = Mage('Маг')
archer = Archer('Лучник')

# Воин - зелёный
# Маг - фиолетовый
# Лучник - синий
print('\033[44;30mБой воина и мага\033[0m')
battle(warrior, mage)

warrior = Warrior('Воин')
mage = Mage('Маг')
archer = Archer('Лучник')
print('\033[44;30mБой мага и лучника\033[0m')
battle(mage, archer)