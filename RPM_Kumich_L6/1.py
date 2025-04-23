class MathUtils:
    pi = 3.14159
    e = 2.71828

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return 'ошибка деления на ноль'
        return a / b

    @staticmethod
    def power(base, exponent):
        return base ** exponent

    @staticmethod
    def circle_area(radius):
        return MathUtils.pi * (radius ** 2)

    @staticmethod
    def is_even(number):
        return 'чётное' if number % 2 == 0 else 'нечётное'


print('Сумма:', MathUtils.add(1, 3))
print('Разность:', MathUtils.subtract(3, 1))
print('Произведение:', MathUtils.multiply(2, 3))
print('Частное:', MathUtils.divide(6, 3))
print('Возведение в степень:', MathUtils.power(2, 3))
print('Площадь круга:', MathUtils.circle_area(3))
print('Проверка четности:', MathUtils.is_even(4))
