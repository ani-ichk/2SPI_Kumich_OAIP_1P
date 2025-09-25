# Двигатель
class Engine:
    def on(self):
        print('-> Двигатель включён')

    def off(self):
        print('-> Двигатель выключен')

# Климат-контроль
class ClimateControl:
    def on(self):
        print('-> Климат-контроль установлен на XX°C')

    def off(self):
        print('-> Климат-контроль выключен')

# Мультимедиа
class MultimediaSystem:
    def on(self):
        print('-> Музыка включена')

    def off(self):
        print('-> Музыка выключена')

# Фары
class Headlights:
    def on(self):
        print('-> Фары включены')

    def off(self):
        print('-> Фары выключены')

# Фасад
class CarFacade:
    def __init__(self):
        self.engine = Engine()
        self.climate = ClimateControl()
        self.multimedia = MultimediaSystem()
        self.headlights = Headlights()

    def start_vroom_vroom(self):
        print('=== Запускаем поездку ===')
        self.engine.on()
        self.headlights.on()
        self.climate.on()
        self.multimedia.on()
        print('Машина готова к поездке!')

    def end_vroom_vroom(self):
        print('=== Завершаем поездку ===')
        self.multimedia.off()
        self.climate.off()
        self.headlights.off()
        self.engine.off()
        print('Поездка завершена')


def main():
    print('=== Поездка БЕЗ фасада ===')
    engine = Engine()
    climate = ClimateControl()
    multimedia = MultimediaSystem()
    headlights = Headlights()

    engine.on()
    headlights.on()
    climate.on()
    multimedia.on()

    engine.off()
    headlights.off()
    climate.off()
    multimedia.off()

    print()

    print('=== Поездка ИСПОЛЬЗУЯ фасад ===')
    car = CarFacade()

    car.start_vroom_vroom()
    car.end_vroom_vroom()


if __name__ == '__main__':
    main()