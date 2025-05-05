import csv


with open('wares2.csv', 'w', encoding='utf-8', newline='') as f:
    data = csv.writer(f, delimiter=';')
    data.writerow(['Name', 'Old price', 'New price'])
    # while True:
    #     s = input()
    #     if not s or len(s.split()) < 3:
    #         break
    #     data.writerow(s.split()[0])
    #     data.writerow(s.split()[1])
    #     data.writerow(s.split()[2])
    data.writerow(['Product1', '3', '5'])
    data.writerow(['Product2', '124', '34'])
    data.writerow(['Product3', '2', '5'])
    data.writerow(['Product4', '3', '8'])
    data.writerow(['Product5', '120', '1'])
    data.writerow(['Product6', '5', '10'])

discounted_products = []

with open('wares2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';')
    for i in reader:
        name = i[0].strip()
        try:
            old_price = int(i[1].strip())
            new_price = int(i[2].strip())
        except (ValueError, IndexError):
            continue  # пропускаем строки с некорректными данными
        if new_price < old_price:
                discounted_products.append(name)

print('\n'.join(discounted_products))