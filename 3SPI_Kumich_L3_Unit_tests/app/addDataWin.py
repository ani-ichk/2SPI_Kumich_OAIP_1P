from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QMessageBox


class AddDataWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Добавление контакта")
        self.setFixedSize(350, 200)

        center = QWidget()
        self.setCentralWidget(center)

        layout = QVBoxLayout()

        form = QFormLayout()
        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.city_input = QLineEdit()

        form.addRow("ФИО:", self.name_input)
        form.addRow("Телефон:", self.phone_input)
        form.addRow("Город:", self.city_input)

        layout.addLayout(form)

        self.save_btn = QPushButton("Сохранить")
        layout.addWidget(self.save_btn)

        center.setLayout(layout)

        self.save_btn.clicked.connect(self.save)

    def validate(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        city = self.city_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите ФИО")
            return False

        if not phone or len(phone) < 5:
            QMessageBox.warning(self, "Ошибка", "Введите корректный телефон")
            return False

        if not city:
            QMessageBox.warning(self, "Ошибка", "Введите город")
            return False

        return True

    def save(self):
        if not self.validate():
            return

        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        city = self.city_input.text().strip()

        success = self.db.add_contact(name, phone, city)
        if success:
            QMessageBox.information(self, "Успех", "Контакт добавлен")
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Телефон уже существует")