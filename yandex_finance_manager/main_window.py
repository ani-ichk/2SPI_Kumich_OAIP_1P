from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QPushButton, QStackedWidget)
from PyQt6.QtGui import QFont
from operations_tab import OperationsTab
from analytics_tab import AnalyticsTab
from budget_tab import BudgetTab


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Финансовый менеджер")
        self.setGeometry(100, 100, 1000, 800)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)

        # левая панель с балансом и кнопками
        self.create_left_panel(main_layout)

        # правая панель с вкладками
        self.create_right_panel(main_layout)

    def create_left_panel(self, main_layout):
        left_widget = QWidget()
        left_widget.setFixedWidth(250)
        left_layout = QVBoxLayout(left_widget)

        self.create_balance_block(left_layout)

        self.create_navigation_buttons(left_layout)

        main_layout.addWidget(left_widget)

    def create_balance_block(self, layout):
        balance_title = QLabel("ТЕКУЩИЙ БАЛАНС")
        balance_title.setFont(QFont("Segoe UI Black", 16, QFont.Weight.Bold))

        self.balance_amount = QLabel("42000.0 ₽")
        self.balance_amount.setFont(QFont("Segoe UI Black", 16, QFont.Weight.Bold))

        income_label = QLabel("Доход: 52000.0 ₽")
        income_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        expense_label = QLabel("Расход: 10000.0 ₽")
        expense_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        layout.addWidget(balance_title)
        layout.addWidget(self.balance_amount)
        layout.addWidget(income_label)
        layout.addWidget(expense_label)

        layout.addStretch()

    def create_navigation_buttons(self, layout):
        self.operations_btn = QPushButton("Операции")
        self.operations_btn.clicked.connect(self.show_operations)

        self.analytics_btn = QPushButton("Аналитика")
        self.analytics_btn.clicked.connect(self.show_analytics)

        self.budget_btn = QPushButton("Бюджет")
        self.budget_btn.clicked.connect(self.show_budget)

        layout.addWidget(self.operations_btn)
        layout.addWidget(self.analytics_btn)
        layout.addWidget(self.budget_btn)

    def create_right_panel(self, main_layout):
        self.stacked_widget = QStackedWidget()

        self.operations_tab = OperationsTab()
        self.analytics_tab = AnalyticsTab()
        self.budget_tab = BudgetTab()

        self.stacked_widget.addWidget(self.operations_tab)
        self.stacked_widget.addWidget(self.analytics_tab)
        self.stacked_widget.addWidget(self.budget_tab)

        main_layout.addWidget(self.stacked_widget)

    def show_operations(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_analytics(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_budget(self):
        self.stacked_widget.setCurrentIndex(2)