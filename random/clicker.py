import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class ClickerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cnt = 0
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setWindowTitle('Кликер')
        self.resize(300, 200)

        # поле ввода начального числа
        self.input_label = QLabel('Введите начальное число:')
        self.number_input = QLineEdit()
        self.number_input.setText('0')

        # кнопка для установки начального числа
        self.set_button = QPushButton('Установить число')
        self.set_button.clicked.connect(self.set_number)

        # метка для отображения числа
        self.number_label = QLabel('0')
        self.number_label.setStyleSheet('font-size: 30px;')  # увеличение размера шрифта

        # кнопка для увеличения числа
        self.click_button = QPushButton('Увеличить на 1')
        self.click_button.clicked.connect(self.plus_one)

        layout.addWidget(self.input_label)
        layout.addWidget(self.number_input)
        layout.addWidget(self.set_button)
        layout.addWidget(self.number_label)
        layout.addWidget(self.click_button)

        self.setLayout(layout)

    # установка начального числа
    def set_number(self):
        try:
            self.cnt = int(self.number_input.text())  # преобразуем текст в число
            self.number_label.setText(str(self.cnt))  # обновляем метку
        except ValueError:
            self.number_label.setText('Ошибка!')

    # увеличения числа на 1
    def plus_one(self):
        self.cnt += 1
        self.number_label.setText(str(self.cnt))  # обновляем текст метки


app = QApplication(sys.argv)
window = ClickerApp()
window.show()
sys.exit(app.exec())