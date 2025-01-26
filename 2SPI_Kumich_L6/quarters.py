def quarters(*args):
    # словарь с ключами-четвертями
    res = {'I': 0, 'II': 0, 'III': 0, 'IV': 0, }
    # проходимся по значениям x и y
    for x, y in args:
        if x > 0 and y > 0:
            res['I'] += 1
        elif x < 0 and y > 0:
            res['II'] += 1
        elif x < 0 and y < 0:
            res['III'] += 1
        elif x > 0 and y < 0:
            res['IV'] += 1
    return res