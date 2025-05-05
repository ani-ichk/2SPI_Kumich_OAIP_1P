import csv


budget = 5000
max_cnt = 10
products = []

with open('wares.csv', 'w', encoding='utf-8', newline='') as f:
    data = csv.writer(f, delimiter=';')
    # while True:
    #     s = input()
    #     if not s or len(s.split()) < 2:
    #         break
    #     data.writerow(s.split()[0])
    #     data.writerow(s.split()[1])
    data.writerow(['Товар1', '6000'])
    data.writerow(['Товар2', '8000'])
    data.writerow(['Товар3', '700'])
    data.writerow(['Товар4', '1000'])
    data.writerow(['Товар5', '25'])
    data.writerow(['Товар6', '250'])
    data.writerow(['Товар7', '150'])
    data.writerow(['Товар8', '840'])
    data.writerow(['Товар9', '300'])

with open('wares.csv', 'r', encoding='utf-8') as f:
    data = csv.reader(f, delimiter=';')
    for row in data:
        name = row[0]
        price = int(row[1])
        products.append((price, name))

# сортируем товары по возрастанию цены
products.sort()

basket = []  # корзина
balance = budget  # остаток

for price, name in products:
    if price > balance:
        continue  # товар слишком дорогой
    max_possible = min(max_cnt, balance // price)
    if max_possible == 0:
        continue  # в дальнейшем необходимо умножать, а 0 нам не нужен
    # добавляем столько товаров, сколько возможно купить на наш бюджет
    basket.extend([name] * max_possible)
    balance -= max_possible * price

if not basket:
    print('error')

# сортируем выбранные товары по цене
res = {}
for price, name in products:
    if name in basket and name not in res:
        res[name] = price

sorted_res = sorted(res.items(), key=lambda x: x[1])
result = [name for name, price in sorted_res]
print(', '.join(result))