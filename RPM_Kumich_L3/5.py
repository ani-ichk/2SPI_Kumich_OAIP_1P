class Player:
    def __init__(self, name):
        self.name = name
        self._health = 100
        self._level = 1
        self._experience = 0

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, val):
        if val < 0:
            self._health = 0
        elif val > 100:
            self._health = 100
        else:
            self._health += val

    @health.deleter
    def health(self):
        self._health = None

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, val):
        if val < 1:
            self._level = 1
        else:
            self._level += val

    @level.deleter
    def level(self):
        self._level = None

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, val):
        if val < 0:
            self._experience = 0
        else:
            self._experience += val

    @experience.deleter
    def experience(self):
        self._experience = None

    def level_up(self):
        self.level += 1
        print(f'{self.name} повысил левел: {self.level}')

    def get_experience(self, val):
        if val > 0:
            self.experience += val
            print(f'{self.name} +{val} очков опыта')
            if self.experience >= 100:
                self.experience = 0
                self.level_up()

    def __str__(self):
        return f'''\tИмя: {self.name}
    Health: {self.health}
    Level: {self.level}
    Experience: {self.experience}'''


player = Player('Mag')
print(player)

player.get_experience(50)
print(player)

player.get_experience(60)
print(player)