from abc import ABC, abstractmethod


class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity

    @abstractmethod
    def use(self):
        pass

    def get_description(self):
        return f'"{self.item_name}" (Редкость: {self.rarity}, Вес: {self.weight})'


class HealthPotion(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)

    def use(self):
        return f'Зелье здоровья использовано: +50 HP'

    def get_description(self):
        return f'Зелье здоровья {super().get_description()} - восстанавливает 50 HP'


class ManaCrystal(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)

    def use(self):
        print(f'Кристалл маны использован: +30 MP')

    def get_description(self):
        return f'Кристалл маны {super().get_description()} - восстанавливает 30 MP'


hp = HealthPotion('Большой флакон', 'Обычное', 0.5)
mc = ManaCrystal('Синий осколок', 'Редкое', 0.3)

print(hp.use())
print(hp.get_description())
print(mc.get_description())
