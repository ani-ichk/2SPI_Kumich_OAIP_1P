class Game:
    def __init__(self):
        pass

    def start(self): # начать игру
        pass

    def pause(self): # пауза
        pass

    def reset(self): # перезагрузка
        pass

    def exit(self): # выход
        pass


class Board:
    def __init__(self, width, height):
        self.width = width # ширина и высота игрового поля
        self.height = height
        self.grid = []  # состояние игрового поля

    def create(self): # создание поля
        pass

    def clear_lines(self):
        pass

    def add_shape(self, shape):
        pass


class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type
        self.rotation_state = 0  # Положение фигуры
        self.coordinates = []  # координаты клетки фигуры
    # действия с фигурой: вращение, сдвиг влево, вправо, опустить вниз
    def rotate(self):
        pass

    def left(self):
        pass

    def right(self):
        pass

    def down(self):
        pass

# фигуры
class TShape(Shape):
    def __init__(self):
        super().__init__('T')


class SShape(Shape):
    def __init__(self):
        super().__init__('S')


class ZShape(Shape):
    def __init__(self):
        super().__init__('Z')


class JShape(Shape):
    def __init__(self):
        super().__init__('J')


class LShape(Shape):
    def __init__(self):
        super().__init__('L')


class IShape(Shape):
    def __init__(self):
        super().__init__('I')


class OShape(Shape):
    def __init__(self):
        super().__init__('O')