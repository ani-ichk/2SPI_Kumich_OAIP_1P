class InterfaceChecker(type):
    def __new__(mcs, name, bases, attrs):
        obj = super().__new__(mcs, name, bases, attrs)
        for i in ['load', 'save']:
            if i not in attrs:
                raise TypeError(f'В классе {name} должен быть реализован метод {i}')
        return obj


class CorrectPlugin(metaclass=InterfaceChecker):
    def load(self):
        print('Загрузка')

    def save(self):
        print('Сохранение')


class BrokenPlugin(metaclass=InterfaceChecker):
    def load(self):
        print('Загрузка')


plugin = CorrectPlugin()
plugin.load()
plugin.save()