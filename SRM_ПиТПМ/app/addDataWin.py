from PyQt6.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
                             QComboBox, QLineEdit, QTextEdit,
                             QMessageBox, QLabel)  # добавлен QLabel
from PyQt6.QtGui import QIcon  # не было импорта
from database.scripts.db import Data


class AddDataWin(QWidget):
    def __init__(self, data = None):
        super().__init__()
        self.db = Data('database/service_center.db')  # добавлен путь к БД
        self.data = data
        self.initUI()
        if data:
            self.upload_editable_data()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/computer.ico'))
        self.setWindowTitle("Добавить новый заказ")
        self.setGeometry(100, 100, 400, 400)  # 2000 высоты - слишком много
        self.work_label = QLabel("Тип работы:")
        self.work_input = QComboBox()
        self.load_work_types()
        self.description_label = QLabel("Описание работы:")
        self.description_input = QTextEdit()
        self.date_label = QLabel("Дата принятия (YYYY-MM-DD):")
        self.date_input = QLineEdit()
        self.customer_label = QLabel("Клиент:")  # исправлено с "XXXXXXXXX:"
        self.customer_input = QLineEdit()
        self.executor_label = QLabel("Исполнитель:")
        self.executor_input = QComboBox()
        self.load_executors()
        self.status_label = QLabel("Статус:")
        self.status_input = QComboBox()
        self.load_statuses()
        self.add_button = QPushButton("Добавить заказ")
        self.back_button = QPushButton("Назад")  # создание кнопки "Назад"

        layout = QVBoxLayout()
        layout.addWidget(self.work_label)
        layout.addWidget(self.work_input)
        layout.addWidget(self.description_label)
        layout.addWidget(self.description_input)
        layout.addWidget(self.date_label)
        layout.addWidget(self.date_input)
        layout.addWidget(self.customer_label)
        layout.addWidget(self.customer_input)
        layout.addWidget(self.executor_label)
        layout.addWidget(self.executor_input)
        layout.addWidget(self.status_label)
        layout.addWidget(self.status_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.back_button)  # добавление кнопки "Назад" в layout
        self.setLayout(layout)

        self.add_button.clicked.connect(self.add_order)  # подключение сигнала
        self.back_button.clicked.connect(self.go_back)  # подключение кнопки "Назад"

    def go_back(self):  # метод для возврата в предыдущее окно
        self.close()  # просто закрывает текущее окно

    def upload_editable_data(self):
        self.work_input.setCurrentText(self.data[1])
        self.description_input.setText(self.data[2])
        self.date_input.setText(self.data[3])  # вместо 4
        self.customer_input.setText(self.data[4])  # вместо 3
        self.executor_input.setCurrentText(self.data[5])  # вместо -2
        self.status_input.setCurrentText(self.data[6])  # вместо -1

    def load_work_types(self):
        self.work_input.clear()
        self.db.get_work_types()
        if isinstance(self.db.data, list):  # добавлена проверка типа
            for id_work, work in self.db.data:
                self.work_input.addItem(work, id_work)

    def load_executors(self):
        self.executor_input.clear()
        self.db.get_executors()
        if isinstance(self.db.data, list):  # добавлена проверка типа
            for id_employee, surname in self.db.data:  # исправлено employee на surname
                self.executor_input.addItem(surname, id_employee)

    def load_statuses(self):
        self.status_input.clear()
        self.db.get_statuses()
        if isinstance(self.db.data, list):  # добавлена проверка типа
            for id_status, status in self.db.data:
                self.status_input.addItem(status, id_status)

    def add_order(self):
        type_of_work = self.work_input.currentData()
        description = self.description_input.toPlainText()
        acceptance_date = self.date_input.text()  # переменная использовалась, но не была определена
        customer = self.customer_input.text()
        executor = self.executor_input.currentData()
        status = self.status_input.currentData()
        if self.data:
            id_order = self.data[0]
            answer = self.db.update_order(type_of_work=type_of_work, description=description,
                                       acceptance_date=acceptance_date,
                                       customer=customer, executor=executor, status=status, id_order=id_order)
        else:
            answer = self.db.add_order(type_of_work=type_of_work, description=description, acceptance_date=acceptance_date,
                                       customer=customer, executor=executor, status=status)
        QMessageBox.information(self, "Инфо", answer)
        self.close()
