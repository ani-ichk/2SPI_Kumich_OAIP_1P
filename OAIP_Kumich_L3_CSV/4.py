n, m = map(int, input().split())
array = []

while True:
    line = input().strip()
    parts = line.split()
    if not line or len(parts) < 5:
        break
    parts = line.split()
    surname, name, *scores = parts
    scores = list(map(int, scores))
    array.append((surname, name, scores))

# фильтрация абитуриентов
filtered = []
for surname, name, scores in line:
    total = sum(scores)
    if total >= n and all(score >= m for score in scores):
        filtered.append((surname, name, scores, total))

# запись в файл
with open('exam.csv', 'w', encoding='utf-8') as file:
    file.write('Фамилия;Имя;Результат 1;Результат 2;Результат 3;Сумма\n')
    for surname, name, scores, total in filtered:
        line = f'{surname};{name};{scores[0]};{scores[1]};{scores[2]};{total}\n'
        file.write(line)