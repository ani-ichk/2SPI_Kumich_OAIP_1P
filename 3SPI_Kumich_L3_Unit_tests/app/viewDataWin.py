from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTableWidget, QHBoxLayout, QPushButton, QTableWidgetItem, QMessageBox


class ViewDataWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle("Список контактов")
        self.setGeometry(100, 100, 500, 300)

        center = QWidget()
        self.setCentralWidget(center)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "ФИО", "Телефон", "Город"])
        layout.addWidget(self.table)

        button_box = QHBoxLayout()
        self.delete_btn = QPushButton("Удалить контакт")
        self.refresh_btn = QPushButton("Обновить")

        button_box.addWidget(self.delete_btn)
        button_box.addWidget(self.refresh_btn)
        layout.addLayout(button_box)

        center.setLayout(layout)

        self.delete_btn.clicked.connect(self.delete_selected)
        self.refresh_btn.clicked.connect(self.load_data)

    def load_data(self):
        contacts = self.db.get_contacts()
        self.table.setRowCount(len(contacts))

        for i, contact in enumerate(contacts):
            self.table.setItem(i, 0, QTableWidgetItem(str(contact["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(contact["full_name"]))
            self.table.setItem(i, 2, QTableWidgetItem(contact["phone"]))
            self.table.setItem(i, 3, QTableWidgetItem(contact["city"]))

    def get_selected_contact_id(self):
        selected = self.table.selectionModel().selectedRows()
        if selected:
            row = selected[0].row()
            id_item = self.table.item(row, 0)
            if id_item:
                return int(id_item.text())
        return None

    def delete_selected(self):
        contact_id = self.get_selected_contact_id()
        if contact_id is None:
            QMessageBox.warning(self, "Ошибка", "Выберите контакт для удаления")
            return

        reply = QMessageBox.question(
            self,
            "Подтверждение",
            "Удалить выбранный контакт?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            success = self.db.delete_contact(contact_id)
            if success:
                QMessageBox.information(self, "Успех", "Контакт удален")
                self.load_data()
            else:
                QMessageBox.warning(self, "Ошибка", "Ошибка при удалении")