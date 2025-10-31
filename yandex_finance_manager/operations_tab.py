from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QPushButton,
                             QHeaderView, QLabel, QComboBox)
from PyQt6.QtCore import Qt


class OperationsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        # панель с кнопками
        self.create_buttons_panel(main_layout)

        # таблица операций
        self.create_operations_table(main_layout)

        # панель фильтрации
        self.create_filter_panel(main_layout)

    def create_buttons_panel(self, layout):
        # горизонтальный layout для кнопок
        buttons_layout = QHBoxLayout()

        self.add_btn = QPushButton("+")
        self.add_btn.setToolTip("Добавить операцию")
        self.add_btn.clicked.connect(self.add_operation)

        self.delete_btn = QPushButton("🗑")
        self.delete_btn.setToolTip("Удалить операцию")
        self.delete_btn.clicked.connect(self.delete_operation)

        self.edit_btn = QPushButton("✏")
        self.edit_btn.setToolTip("Изменить операцию")
        self.edit_btn.clicked.connect(self.edit_operation)

        buttons_layout.addWidget(self.add_btn)
        buttons_layout.addWidget(self.delete_btn)
        buttons_layout.addWidget(self.edit_btn)

        buttons_layout.addStretch()

        layout.addLayout(buttons_layout)

    def create_operations_table(self, layout):
        self.operations_table = QTableWidget()
        self.operations_table.setColumnCount(5)
        self.operations_table.setHorizontalHeaderLabels([
            "Дата", "Категория", "Описание", "Сумма", "Статус"
        ])

        header = self.operations_table.horizontalHeader()
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.add_sample_data()

        layout.addWidget(self.operations_table)

    def add_sample_data(self):
        self.operations_table.setRowCount(4)

        # тестовые данные
        test_data = [
            ["2025-10-10", "Еда", "Продукты", "1500.0", "Расход"],
            ["2025-05-10", "Зарплата", "Аванс", "52000.0", "Доход"],
            ["2025-07-10", "Транспорт", "Бензин", "2000.0", "Расход"],
            ["2025-15-10", "Развлечения", "Аванс", "6500.0", "Расход"]
        ]

        for row, data in enumerate(test_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.operations_table.setItem(row, col, item)

    def create_filter_panel(self, layout):
        filter_layout = QHBoxLayout()

        filter_label = QLabel("Фильтрация:")

        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Все", "Только доходы", "Только расходы"])
        self.filter_combo.currentTextChanged.connect(self.apply_filter)

        filter_layout.addWidget(filter_label)
        filter_layout.addWidget(self.filter_combo)
        filter_layout.addStretch()

        layout.addLayout(filter_layout)

    def add_operation(self):
        print("Открытие диалога добавления операции")
        # здесь будет вызов диалогового окна для добавления операции

    def delete_operation(self):
        print("Удаление выбранной операции")
        # здесь будет логика удаления операции из БД

    def edit_operation(self):
        print("Редактирование выбранной операции")
        # здесь будет вызов диалогового окна для редактирования операции

    def apply_filter(self, filter_type):
        print(f"Применен фильтр: {filter_type}")
        # здесь будет логика фильтрации данных в таблице