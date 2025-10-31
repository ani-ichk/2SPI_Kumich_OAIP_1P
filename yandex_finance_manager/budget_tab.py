from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QTableWidget,
                             QTableWidgetItem, QPushButton, QHeaderView,
                             QProgressBar, QFrame)
from PyQt6.QtCore import Qt


class BudgetTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout(self)

        self.create_top_panel(main_layout)

        self.create_middle_panel(main_layout)

        self.create_bottom_panel(main_layout)

    def create_top_panel(self, layout):
        top_layout = QHBoxLayout()

        period_label = QLabel("Период:")

        self.period_combo = QComboBox()
        self.period_combo.addItems(["Текущий месяц", "Год"])

        top_layout.addWidget(period_label)
        top_layout.addWidget(self.period_combo)
        top_layout.addStretch()

        layout.addLayout(top_layout)

    def create_middle_panel(self, layout):
        middle_layout = QHBoxLayout()

        self.create_budget_table(middle_layout)

        self.create_buttons_panel(middle_layout)

        layout.addLayout(middle_layout)

    def create_budget_table(self, layout):
        self.budget_table = QTableWidget()
        self.budget_table.setColumnCount(5)
        self.budget_table.setHorizontalHeaderLabels([
            "Категория", "Лимит", "Потрачено", "Остаток", "Прогресс"
        ])

        header = self.budget_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.add_sample_budget_data()

        layout.addWidget(self.budget_table)

    def add_sample_budget_data(self):
        self.budget_table.setRowCount(4)

        sample_data = [
            ["Еда", "10000", "7500", "2500"],
            ["Транспорт", "5000", "4500", "500"],
            ["Развлечения", "3000", "2800", "200"],
            ["Одежда", "8000", "2000", "6000"]
        ]

        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.budget_table.setItem(row, col, item)

            progress_bar = self.create_progress_bar(row, data[1], data[2])
            self.budget_table.setCellWidget(row, 4, progress_bar)

    def create_progress_bar(self, row, limit, spent):
        progress_bar = QProgressBar()

        limit_val = float(limit)
        spent_val = float(spent)

        if limit_val > 0:
            percentage = (spent_val / limit_val) * 100
        else:
            percentage = 0

        progress_bar.setValue(int(percentage))

        # цвет в зависимости от процента
        if percentage <= 70:
            progress_bar.setStyleSheet("QProgressBar::chunk { background-color: green; }")
        elif percentage <= 90:
            progress_bar.setStyleSheet("QProgressBar::chunk { background-color: yellow; }")
        else:
            progress_bar.setStyleSheet("QProgressBar::chunk { background-color: red; }")

        return progress_bar

    def create_buttons_panel(self, layout):
        buttons_layout = QVBoxLayout()

        add_limit_btn = QPushButton("Добавить лимит")
        add_limit_btn.clicked.connect(self.add_limit)

        edit_limit_btn = QPushButton("Редактировать лимит")
        edit_limit_btn.clicked.connect(self.edit_limit)

        delete_limit_btn = QPushButton("Удалить лимит")
        delete_limit_btn.clicked.connect(self.delete_limit)

        buttons_layout.addWidget(add_limit_btn)
        buttons_layout.addWidget(edit_limit_btn)
        buttons_layout.addWidget(delete_limit_btn)
        buttons_layout.addStretch()

        layout.addLayout(buttons_layout)

    def create_bottom_panel(self, layout):
        bottom_layout = QHBoxLayout()

        self.create_pie_chart_block(bottom_layout)

        self.create_categories_block(bottom_layout)

        layout.addLayout(bottom_layout)

    def create_pie_chart_block(self, layout):
        pie_chart_label = QLabel("Круговая диаграмма расходов")
        pie_chart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pie_chart_label.setFrameStyle(QFrame.Shape.Box)
        pie_chart_label.setStyleSheet("background-color: white; border: 1px solid gray;")
        pie_chart_label.setMinimumSize(200, 150)

        layout.addWidget(pie_chart_label)

    def create_categories_block(self, layout):
        categories_widget = QWidget()
        categories_layout = QVBoxLayout(categories_widget)

        food_category = QLabel("● Еда")
        transport_category = QLabel("● Транспорт")
        entertainment_category = QLabel("● Развлечения")
        clothes_category = QLabel("● Одежда")

        categories_layout.addWidget(food_category)
        categories_layout.addWidget(transport_category)
        categories_layout.addWidget(entertainment_category)
        categories_layout.addWidget(clothes_category)
        categories_layout.addStretch()

        layout.addWidget(categories_widget)

    def add_limit(self):
        print("Добавление нового лимита")

    def edit_limit(self):
        print("Редактирование лимита")

    def delete_limit(self):
        print("Удаление лимита")