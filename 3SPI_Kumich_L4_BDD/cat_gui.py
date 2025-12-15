from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,QLineEdit,
                             QPushButton, QLabel, QTableWidget,QTableWidgetItem, QDialog, QMessageBox)


class CatWindow(QMainWindow):
    def __init__(self, database):
        super().__init__()
        self.db = database
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Учет котов")
        self.setGeometry(100, 100, 600, 400)

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()

        form_add_cat_layout = QHBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя кота")

        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Возраст")

        self.breed_input = QLineEdit()
        self.breed_input.setPlaceholderText("Порода")

        self.color_input = QLineEdit()
        self.color_input.setPlaceholderText("Цвет")

        form_add_cat_layout.addWidget(QLabel("Имя:"))
        form_add_cat_layout.addWidget(self.name_input)
        form_add_cat_layout.addWidget(QLabel("Возраст:"))
        form_add_cat_layout.addWidget(self.age_input)
        form_add_cat_layout.addWidget(QLabel("Порода:"))
        form_add_cat_layout.addWidget(self.breed_input)
        form_add_cat_layout.addWidget(QLabel("Цвет:"))
        form_add_cat_layout.addWidget(self.color_input)

        button_layout = QHBoxLayout()

        self.add_btn = QPushButton("Добавить кота")
        self.view_btn = QPushButton("Показать всех котов")

        self.add_btn.clicked.connect(self.add_cat)
        self.view_btn.clicked.connect(self.show_cats)

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.view_btn)

        layout.addLayout(form_add_cat_layout)
        layout.addLayout(button_layout)
        central.setLayout(layout)

        self.cats_window = CatsViewWindow(self.db)

    def add_cat(self):
        name = self.name_input.text().strip()
        age_text = self.age_input.text().strip()
        breed = self.breed_input.text().strip() or "неизвестно"
        color = self.color_input.text().strip() or "разный"

        # простая валидация
        if not name:
            QMessageBox.warning(self, "Ошибка", "Введите имя кота!")
            return

        if not age_text or not age_text.isdigit():
            QMessageBox.warning(self, "Ошибка", "Возраст должен быть числом!")
            return

        age = int(age_text)
        if age < 0 or age > 30:
            QMessageBox.warning(self, "Ошибка", "Возраст кота должен быть от 0 до 30 лет!")
            return

        try:
            self.db.add_cat(name, age, breed, color)
            QMessageBox.information(self, "Успех", f"Кот {name} добавлен!")
            self.name_input.clear()
            self.age_input.clear()
            self.breed_input.clear()
            self.color_input.clear()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка базы: {str(e)}")

    def show_cats(self):
        self.cats_window.refresh()
        self.cats_window.show()


class CatsViewWindow(QDialog):
    def __init__(self, database):
        super().__init__()
        self.db = database
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Все коты")
        self.setGeometry(200, 200, 500, 300)

        layout = QVBoxLayout()
        self.table = QTableWidget()
        layout.addWidget(self.table)
        self.setLayout(layout)

    def refresh(self):
        cats = self.db.get_all_cats()
        self.table.setRowCount(len(cats))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Имя", "Возраст", "Порода", "Цвет"])

        for row, cat in enumerate(cats):
            for col, value in enumerate(cat):
                self.table.setItem(row, col, QTableWidgetItem(str(value)))