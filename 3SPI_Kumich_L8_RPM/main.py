from abc import ABC, abstractmethod


# Интерфейс наблюдателя
class Observer(ABC):
    @abstractmethod
    def update(self, match):  # метод, который вызывается при изменении счета матча
        pass


# Класс матча (Издатель)
class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.score1 = 0  # счет первой команды
        self.score2 = 0  # счет второй команды
        self._observers = []  # список наблюдателей (подписчиков)

    # добавить наблюдателя
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f'{observer.name} подписывается на матч')
        else:
            print(f'{observer.name} уже подписан на матч')

    # исключить наблюдателя
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f'{observer.name} отписывается от матча')
        else:
            print(f'{observer.name} нет в подписчиках матча')

    # оповещение
    def notify(self):
        for observer in self._observers:
            print(f'Уведомление для {observer.name}...')
            observer.update(self)

    # гол первой команды
    def goal_team1(self):
        self.score1 += 1
        print(f'{self.team1} забивает гол')
        self.notify()  # уведомляем всех наблюдателей

    # гол второй команды
    def goal_team2(self):
        self.score2 += 1
        print(f'{self.team2} забивает гол')
        self.notify()  # уведомляем всех наблюдателей

    # счёт
    def get_score(self) -> str:
        return f'{self.score1}:{self.score2}'


# Конкретные наблюдатели
class Scoreboard(Observer):
    def __init__(self):
        self.name = 'Табло на стадионе'

    def update(self, match):
        print(f'---{self.name} обновляется: {match.team1} {match.score1} - {match.score2} {match.team2}---')


class MobileApp(Observer):
    def __init__(self):
        self.name = 'Мобильное приложение'

    def update(self, match):
        print(f'---{self.name}: ГООЛ! Счет: {match.get_score()}---')


class Commentator(Observer):
    def __init__(self):
        self.name = 'Комментатор'

    def update(self, match):
        print(f'---{self.name}: "ГОООООЛ! НЕВЕРОЯТНО! Счет стал {match.get_score()}!"---')


def main():
    # создаём матч (издателя)
    match = Match('Команда 1', 'Команда 2')

    # создаем наблюдателей
    scoreboard = Scoreboard()
    mobile_app = MobileApp()
    commentator = Commentator()

    # подписываем наблюдателей на матч
    match.attach(scoreboard)
    match.attach(mobile_app)
    match.attach(commentator)

    print('*первая команда забивает гол*')
    match.goal_team1()

    print('*вторая команда забивает гол*')
    match.goal_team2()

    # отписываем наблюдателей
    match.detach(mobile_app)

    # +гол после отписки
    print('*команда 2 забивает гол*')
    match.goal_team2()


if __name__ == '__main__':
    main()