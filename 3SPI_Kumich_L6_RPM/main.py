# Класс итератор для обхода текста по словам
class Iterator:
    def __init__(self, text):
        self.words = text.split()  # разбиваем текст на слова
        self.index = 0  # текущая позиция

    def __iter__(self):
        """
        Метод, который возвращает сам итератор
        """
        return self  # возвращаем сам себя как итератор

    def __next__(self):
        """
        Метод, который возвращает СЛЕДУЮЩЕЕ слово
        Python вызывает этот метод на каждой итерации цикла for
        """
        if self.index < len(self.words):  # проверка дошли ли мы до конца
            word = self.words[self.index]  # берем текущее слово
            self.index += 1  # переходим к следующему
            return word
        raise StopIteration  # конец итерации

# Класс текст
class Text:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return Iterator(self.text)


def main():
    text = Text('Реализуйте итератор для обхода строкового текста по словам')
    for word in text:
        print(word)


if __name__ == '__main__':
    main()