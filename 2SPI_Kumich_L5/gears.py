def gears(s, n, m):
    num = n / m # передаточное число
    # проходимся по каждому списку списка
    for i in s:
        # проходимся по всем шестеренкам в списке
        for gear in i:
            # gear_wheel не должен быть равен нулю
            if gear == 0:
                continue
            # определяем какая шестеренка нам необходима
            a = gear * num
            # находим подходящую шестеренку в коробке
            if a in i:
                return int(a), gear
    return None, None