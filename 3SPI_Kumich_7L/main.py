import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class GameGuessNumber(QWidget):
    def __init__(self):
        super().__init__()
        self.secret_number = 0  # переменная для хранения загаданного числа
        self.min_range = 1  # минимальное значение диапазона
        self.max_range = 100  # максимальное значение диапазона
        self.generate_number()  # генерация случайного числа при запуске
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Угадай число')
        self.resize(300, 150)

        layout = QVBoxLayout()  # вертикальный контейнер для размещения виджетов
        self.range_label = QLabel(f'Загадано число от {self.min_range} до {self.max_range}')
        self.number_input = QLineEdit()
        self.number_input.setPlaceholderText('Введите число')
        self.guess_button = QPushButton('Проверить')

        layout.addWidget(self.range_label)
        layout.addWidget(self.number_input)
        layout.addWidget(self.guess_button)

        self.guess_button.clicked.connect(self.check_guess)

        self.setLayout(layout)

    def generate_number(self):
        self.secret_number = random.randint(self.min_range, self.max_range)

    def check_guess(self):
        user_input = self.number_input.text()  # получение текста из поля ввода

        if not user_input.isdigit():
            QMessageBox.warning(self, 'Ошибка', 'Пожалуйста, введите число')
            return

        user_number = int(user_input)

        if user_number > self.secret_number:  # если число больше загаданного
            QMessageBox.information(self, 'Результат', 'Больше')
        elif user_number < self.secret_number:  # если число меньше загаданного
            QMessageBox.information(self, 'Результат', 'Меньше')
        else:    # если число угадано
            QMessageBox.information(self, 'Поздравляем!', 'Отгадал!')
            self.generate_number()  # генерация нового числа
            self.number_input.clear()  # очистка поля ввода


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GameGuessNumber()
    window.show()
    sys.exit(app.exec())
