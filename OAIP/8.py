# ввод с клавиатуры цен 3 товаров
a, b, c = float(input('цена первого товара: ')), float(input('цена второго товара: ')), float(input('цена третьего товара: '))
# если цены товаров возрастают, то выводим "Акция!" и к оплате будет: половина от суммы 3 товаров
if a < b < c:
    print('Акция! К оплате:', 0.5 * (a + b + c))
# если же цены товаров убывают, то выводим "Акция!" и к оплате будет: третья часть от суммы трёх товаров
elif a > b > c:
    print('Акция! К оплате:', (a + b + c) / 3)
# иначе к оплате будет полная сумма трёх товаров
else:
    print('К оплате:', a + b + c)