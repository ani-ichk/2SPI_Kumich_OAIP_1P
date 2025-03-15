class Stick:
    def __init__(self):
        pass


class Wood:
    def __init__(self):
        pass


class Iron:
    def __init__(self):
        pass


class Diamond:
    def __init__(self):
        pass


class WoodHoe:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}


    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mWood hoe: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class WoodShovel:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mWood shovel: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class WoodSword:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

    def get_endurance(self):
        return self.__endurance

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def info(self):
        return f'\033[33mWood sword: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class IronHoe:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mIron hoe: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class IronShovel:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mIron shovel: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class IronSword:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

    def get_endurance(self):
        return self.__endurance

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def info(self):
        return f'\033[33mIron sword: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class DiamondHoe:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mDimond hoe: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class DiamondShovel:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def get_endurance(self):
        return self.__endurance

    def info(self):
        return f'\033[33mDimond shovel: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


class DiamondSword:
    def __init__(self):
        self.__damage = 1
        self.__endurance = 3
        self.characteristic = {'damage': self.__damage, 'endurance': self.__endurance}

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage = damage

    def get_endurance(self):
        return self.__endurance

    def set_endurance(self, endurance):
        self.__endurance = endurance

    def info(self):
        return f'\033[33mDimond sword: damage - {self.__damage}, endurance - {self.__endurance}\033[0m'


def craft(*materials):
    temp = [type(elem) for elem in materials]

    if len(temp) == 3:  # мечи и лопаты
        if temp.count(Wood) == 2 and temp.count(Stick) == 1:
            return WoodSword()
        elif temp.count(Wood) == 1 and temp.count(Stick) == 2:
            return WoodShovel()
        elif temp.count(Iron) == 2 and temp.count(Stick) == 1:
            return IronSword()
        elif temp.count(Iron) == 1 and temp.count(Stick) == 2:
            return IronShovel()
        elif temp.count(Diamond) == 2 and temp.count(Stick) == 1:
            return DiamondSword()
        elif temp.count(Diamond) == 1 and temp.count(Stick) == 2:
            return DiamondShovel()
        else:
            print('\033[31mx\033[0m Из данного набора материалов невозможно скрафтить инструмент')
    elif len(temp) == 4:  # мотыги
        if temp.count(Wood) == 2 and temp.count(Stick) == 2:
            return WoodHoe()
        if temp.count(Iron) == 2 and temp.count(Stick) == 2:
            return IronHoe()
        elif temp.count(Diamond) == 2 and temp.count(Stick) == 2:
            return DiamondHoe()
        else:
            print('\033[31mx\033[0m Из данного набора материалов невозможно скрафтить инструмент')
    else:
        print('\033[31mx\033[0m Не верное количество материалов')

def fix(tool, *materials): # починка
    materials = [type(elem) for elem in materials]
    # находим материал какого инструмента необходимо проверять в дальнейшем
    if isinstance(tool, (WoodHoe, WoodShovel,WoodSword )):
        material = Wood
    elif isinstance(tool, (IronHoe, IronShovel, IronSword)):
        material = Iron
    elif isinstance(tool, (DiamondHoe, DiamondShovel, DiamondSword)):
        material = Diamond
    else:
        print('\033[31mx\033[0m Такого инструмента нет')
        return -1

    if material in materials:
        if tool.get_endurance() < tool.characteristic['endurance']:  # не полная прочность
            if materials.count(material) == 1:
                tool.set_endurance(tool.get_endurance() + 1)
                print('Починка \033[32m+1\033[0m')
                materials.remove(material)
                return materials
            elif materials.count(material) >= 2:
                print(f'Полная починка \033[32m+{tool.characteristic['endurance'] - tool.get_endurance()}\033[0m')
                tool.set_endurance(tool.characteristic['endurance'])
                materials.remove(material)
                materials.remove(material)
                return materials
        else:  # прочность полная
            return materials
    else:
        print('\033[31mx\033[0m Материалы не подходят для прокачки данного инструмента')
        return -1


def upgrade(tool, *materials):  # улучшение
    # перед прокачкой инструмент надо починить
    # возвращаем список оставшихся материалов после починки
    materials = fix(tool, *materials)
    if materials == -1:
        print('\033[31mОшибка при починке\033[0m')
    if len(materials) > 0:
        if tool is WoodSword or IronSword or DiamondSword:
            tool.characteristic['damage'] += 1
            tool.set_damage(tool.get_damage() + 1)
            print('Вы прокачали урон меча \033[32m+1\033[0m')
        else:
            tool.characteristic['endurance'] += 1
            tool.set_endurance(tool.get_endurance() + 1)
            print('Вы прокачали прочность инструмента \033[32m+1\033[0m')
    else:
        print('\033[31mНе хватает материалов для прокачки\033[0m')


def use(tool):
    if (tool is WoodHoe or WoodShovel or WoodSword
            or IronHoe or IronShovel or IronSword
            or DiamondHoe or DiamondShovel or DiamondSword):
        tool.set_endurance(tool.get_endurance() - 1)
        print('Прочность \033[31m-1\033[0m')