#создаём список с английским алфавитом
#за первый элемент берём любое значение, т.к. нам надо, чтобы буква A имела индекс 1
letter = ['zero', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#считываем с клавиатуры номер буквы в алфавите
letter_number = int(input('Номер буквы: '))
#проверяем если номер равен 24, то выводим "XYZA" и так далее
if letter_number == 24:
    print('XYZA')
elif letter_number == 25:
    print('YZAB')
elif letter_number == 26:
    print('ZABC')
#в противном случае выводим элемент списка с индексом номера буквы и последующие элементы с прибавлением к индексу 1, 2 и 3
else:
    print(letter[letter_number] + letter[letter_number + 1] + letter[letter_number + 2] + letter[letter_number + 3])
