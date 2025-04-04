from abc import ABC, abstractmethod


class Emplovee(ABC):
    def __init__(self, name, base_rate, position):
        self.name = name
        self.base_rate = base_rate
        self.position = position

    @abstractmethod
    def calculate_salary(self):
        pass

    def get_info(self):
        return f'Сотрудник: {self.name} ({self.position}). Зарплата: {self.base_rate}.'


class Manager(Emplovee):
    def __init__(self, name, base_rate, position):
        super().__init__(name, base_rate, position)

    def calculate_salary(self):
        return self.base_rate * 1.5

    def promote(self, val):
        self.base_rate += val

    def work(self):
        return f'{super().get_info()} Организует работу команды.'


class Developer(Emplovee):
    def __init__(self, name, base_rate, position):
        super().__init__(name, base_rate, position)

    def calculate_salary(self):
        return self.base_rate + 500

    def promote(self, val):
        self.base_rate += val

    def work(self):
        return f'{super().get_info()} Пишет код и исправляет ошибки'


staff = [Manager('Иван', 7500, 'Менеджер'),
         Manager('Николай', 7000, 'Менеджер'),
         Developer('Анна', 5500, 'Разработчик'),
         Developer('Александр', 5000, 'Разработчик')]

print(staff[0].calculate_salary())
staff[2].promote(500)

for i in staff:
    print(i.get_info())