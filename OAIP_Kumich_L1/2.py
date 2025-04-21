total_price = 0.0
order = {}  # заказ
with open('prices.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()
    if text:
        while True:
            input_str = input('Введите ваш заказ: ')
            if not input_str:
                break
            need_name, need_cnt = input_str.split()
            order[need_name] = int(need_cnt)
        prices = {}
        for i in text:
            name_cnt_cost = i.strip().split('\t')
            name, cnt, cost = name_cnt_cost[0].split()
            prices[name] = (int(cnt), float(cost))
        # общая стоимость заказа
        for i, cnt in order.items():
            if i in prices:
                need_count, need_cost = prices[i]
                if cnt <= need_count:
                    total_price += cnt * need_cost
                else:
                    print(f'Недостаточно товара {i}')
        print(f'{total_price:.2f}')
    else:
        print('Файл пуст')
