from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QComboBox, QDateEdit, QFrame)
from PyQt6.QtCore import QDate, Qt


class AnalyticsTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout(self)
        self.create_left_panel(main_layout)
        self.create_right_panel(main_layout)

    def create_left_panel(self, main_layout):
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        self.create_period_block(left_layout)

        self.create_amounts_block(left_layout)

        self.create_categories_block(left_layout)

        main_layout.addWidget(left_widget)

    def create_period_block(self, layout):
        period_label = QLabel("Период:")

        self.period_combo = QComboBox()
        self.period_combo.addItems(["За месяц", "За год"])

        dates_layout = QHBoxLayout()

        date_from_label = QLabel("с")
        self.date_from_edit = QDateEdit()
        self.date_from_edit.setDate(QDate.currentDate())
        self.date_from_edit.setDisplayFormat("dd.MM")

        date_to_label = QLabel("по")
        self.date_to_edit = QDateEdit()
        self.date_to_edit.setDate(QDate.currentDate())
        self.date_to_edit.setDisplayFormat("dd.MM")

        dates_layout.addWidget(date_from_label)
        dates_layout.addWidget(self.date_from_edit)
        dates_layout.addWidget(date_to_label)
        dates_layout.addWidget(self.date_to_edit)

        layout.addWidget(period_label)
        layout.addWidget(self.period_combo)
        layout.addLayout(dates_layout)

    def create_amounts_block(self, layout):
        amounts_frame = QFrame()
        amounts_frame.setFrameStyle(QFrame.Shape.Box)
        amounts_frame.setStyleSheet("background-color: rgba(255,255,255,150);")

        amounts_layout = QVBoxLayout(amounts_frame)

        income_label = QLabel("Доход: 52000.0 ₽")
        expense_label = QLabel("Расход: 10000.0 ₽")

        amounts_layout.addWidget(income_label)
        amounts_layout.addWidget(expense_label)

        layout.addWidget(amounts_frame)

    def create_categories_block(self, layout):
        categories_label = QLabel("Категории расходов:")

        food_category = QLabel("● Еда")
        food_category.setStyleSheet("font-weight: bold; font-size: 14px;")

        transport_category = QLabel("● Транспорт")
        entertainment_category = QLabel("● Развлечения")

        layout.addWidget(categories_label)
        layout.addWidget(food_category)
        layout.addWidget(transport_category)
        layout.addWidget(entertainment_category)

        layout.addStretch()

    def create_right_panel(self, main_layout):
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        self.create_balance_chart_block(right_layout)

        self.create_pie_chart_block(right_layout)

        main_layout.addWidget(right_widget)

    def create_balance_chart_block(self, layout):
        # пока что label для графика баланса (вместо графика)
        chart_label = QLabel("График баланса будет здесь")
        chart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        chart_label.setFrameStyle(QFrame.Shape.Box)
        chart_label.setStyleSheet("background-color: white; border: 1px solid gray;")
        chart_label.setMinimumHeight(200)

        layout.addWidget(chart_label)

    def create_pie_chart_block(self, layout):
        # label для круговой диаграммы (вместо диаграммы)
        pie_chart_label = QLabel("Круговая диаграмма расходов будет здесь")
        pie_chart_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pie_chart_label.setFrameStyle(QFrame.Shape.Box)
        pie_chart_label.setStyleSheet("background-color: white; border: 1px solid gray;")
        pie_chart_label.setMinimumHeight(200)

        layout.addWidget(pie_chart_label)