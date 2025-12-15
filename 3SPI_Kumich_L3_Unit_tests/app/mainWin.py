from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt6.QtGui import QFont
from app.viewDataWin import ViewDataWindow
from app.addDataWin import AddDataWindow


class MainWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Управление контактами")
        self.setFixedSize(350, 200)

        center = QWidget()
        self.setCentralWidget(center)

        layout = QVBoxLayout()

        label = QLabel("Телефонная книга")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        label.setFont(font)

        button_layout = QHBoxLayout()
        self.view_btn = QPushButton("Показать контакты")
        self.add_btn = QPushButton("Добавить контакт")

        button_layout.addWidget(self.view_btn)
        button_layout.addWidget(self.add_btn)

        layout.addWidget(label)
        layout.addLayout(button_layout)

        center.setLayout(layout)

        self.view_btn.clicked.connect(self.show_contacts)
        self.add_btn.clicked.connect(self.add_contact)

    def show_contacts(self):
        self.view_window = ViewDataWindow(self.db)
        self.view_window.show()

    def add_contact(self):
        self.add_window = AddDataWindow(self.db)
        self.add_window.show()