def circuit_resistance(*resistors, connection='serial'):
    # если соединение последовательно, то возвращаем сумму значений r
    if connection == 'serial':
        return sum(resistors)
    # если соед-е пар-но, то проходимся по списку resistors,
    elif connection == 'parallel':
        # вычисляем обратные зн-я каждого r и суммируем
        res = sum(map(lambda x: 1 / x, resistors))
        # возвращаем обратное значение результата
        return 1 / res


data = [30, 30, 30]
print(circuit_resistance(*data, connection='parallel'))
