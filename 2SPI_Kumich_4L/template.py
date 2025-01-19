def template(a, b, c):
    # проверка на существование треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        print('None')
    else:
        print('Периметр: ', a + b + c)
        p = (a + b + c) / 2
        print('Площадь: ', (p * (p - a) * (p - b) * (p - c)) ** 0.5)
        if a == b or a == c or b == c:
            print('Равнобедренный: да')
        else:
            print('Равнобедренный: нет')
        if a == b == c:
            print('Равносторонний: да')
        else:
            print('Равносторонний: нет')