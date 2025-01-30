def func_table(f, x_max, y_max):
    # цикл, проходящий по всем возможным значениям y
    for x in range(x_max + 1):
        res = []
        # цикл, проходящий по всем возможным значениям x
        for y in range(y_max + 1):
            # вычисляем значение функции и доб-ем в список-результат
            res.append(str(eval(f)))
        print('\t'.join(res))
