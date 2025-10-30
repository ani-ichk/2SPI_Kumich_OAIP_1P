import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class GeneratorRandomNumber(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.setWindowTitle('Генератор случайных чисел')
        self.resize(400, 200)

        # метка и поле для вывода сгенерированного числа
        self.result_label = QLabel('Случайное число:')
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)  # только для чтения

        # метка и поле для ввода минимального значения
        self.min_label = QLabel('От:')
        self.min_input = QLineEdit()
        self.min_input.setText('1')

        # метка и поле для ввода максимального значения
        self.max_label = QLabel('До:')
        self.max_input = QLineEdit()
        self.max_input.setText('100')

        # кнопка генерации
        self.generate_button = QPushButton('Сгенерировать')
        self.generate_button.clicked.connect(self.generate_number)

        layout.addWidget(self.result_label)
        layout.addWidget(self.result_display)
        layout.addWidget(self.min_label)
        layout.addWidget(self.min_input)
        layout.addWidget(self.max_label)
        layout.addWidget(self.max_input)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def generate_number(self):
        try:
            # получение значений из полей ввода и преобразование в целые числа
            min_val = int(self.min_input.text())
            max_val = int(self.max_input.text())
            if min_val > max_val:
                self.result_display.setText('Ошибка: минимальное значение диапазона больше максимального')
                return
            random_number = random.randint(min_val, max_val)
            self.result_display.setText(str(random_number))
        except ValueError:
            self.result_display.setText('Ошибка: введите числа')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GeneratorRandomNumber()
    window.show()
    sys.exit(app.exec())