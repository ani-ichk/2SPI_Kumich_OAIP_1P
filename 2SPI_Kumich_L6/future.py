def future(*args, **kwargs):
    c = 1
    # перемножаем значения констант
    for k, v in kwargs.items():
        c *= v
    # высчитываем массу
    mass = sum(args) * c
    # проверяем условия и возвращаем результат
    if mass > VIN:
        return 'ACCELERATION'
    elif mass < VIN:
        return 'DECELERATION'
    return 'UNCHANGED'


VIN = 3
mass = [1, 2, 3, 4, 5]
const = {'charge': 1.6, 'alpha': 0.137, 'pi': 3.14}
print(future(*mass, **const))

VIN = 540
mass = [1, 2, 3, 4, 5]
const = {'e0': 9, 'mu0': 4}
print(future(*mass, **const))