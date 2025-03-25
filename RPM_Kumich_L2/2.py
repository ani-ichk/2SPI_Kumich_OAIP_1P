class Seconds:
    def __init__(self, seconds):
        self._seconds = seconds

    def __str__(self):
        return f'{self._seconds}s'

    def __int__(self):
        return int(self._seconds)


class Minutes:
    def __init__(self, minutes):
        self._minutes = minutes

    def __str__(self):
        return f'{self._minutes}m'

    def __int__(self):
        return int(self._minutes)


class Hours:
    def __init__(self, hours):
        self._hours = hours

    def __str__(self):
        return f'{self._hours}h'

    def __int__(self):
        return int(self._hours)


class Time(Seconds, Minutes, Hours):
    def __init__(self, seconds, minutes, hours):
        Seconds.__init__(self, seconds)
        Minutes.__init__(self, minutes)
        Hours.__init__(self, hours)
        self.norm_form()
        self.total_seconds = self._hours * 3600 + self._minutes * 60 + self._seconds

    def __str__(self):
        return f"{self._hours}h {self._minutes}m {self._seconds}s"

    def norm_form(self):
        if self._seconds >= 60:
            self._minutes += self._seconds // 60
            self._seconds = self._seconds % 60
        if self._minutes >= 60:
            self._hours += self._minutes // 60
            self._minutes = self._minutes % 60

    def __add__(self, other):
        hours = self._hours + other._hours
        minutes = self._minutes + other._minutes
        seconds = self._seconds + other._seconds
        return Time(seconds, minutes, hours)

    def __sub__(self, other):
        total_seconds = self.total_seconds - other.total_seconds
        if total_seconds < 0:
            return '0s'
        return Time(total_seconds % 60, (total_seconds // 60) % 60, total_seconds // 3600)

    def __eq__(self, other):
        if self.total_seconds == other.total_seconds:
            return 'Оба равны'
        elif self.total_seconds > other.total_seconds:
            return 'Первый больше второго'
        else:
            return 'Первый меньше второго'

    def total_seconds(self):
        return f'{self._hours * 3600 + self._minutes * 60 + self._seconds}s'


time1 = Time(hours=1, minutes=30, seconds=45)
time2 = Time(hours=0, minutes=45, seconds=20)

print(time1)
print(time2)

time3 = time1 + time2
print('Сумма:', time3)

print('Вычитание:', time1 - time2)

print('Сравнение:', time1 == time3)