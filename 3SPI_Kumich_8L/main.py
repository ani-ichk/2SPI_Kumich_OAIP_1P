import sys
import csv
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QTableWidget, QTableWidgetItem, QComboBox, QPushButton,
                             QMessageBox, QFileDialog)
from PyQt6.QtGui import QColor


class OlympiadResults(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = []  # список для хранения всех данных из CSV
        self.filtered_data = []  # список для хранения отфильтрованных данных
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Результаты олимпиады')
        self.resize(600, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.load_button = QPushButton('Загрузить файл результатов')
        self.load_button.clicked.connect(self.load_file_dialog)

        buttons_layout = QHBoxLayout()

        self.school_combo = QComboBox()  # выпадающий список для выбора школы
        self.school_combo.addItem('Все')

        self.class_combo = QComboBox()  # выпадающий списко для выбора класса
        self.class_combo.addItem('Все')

        self.results_button = QPushButton('Узнать результаты')  # кнопка для применения фильтров
        self.results_button.clicked.connect(self.apply_filters)  # обработчика нажатия

        buttons_layout.addWidget(self.load_button)
        buttons_layout.addWidget(self.school_combo)
        buttons_layout.addWidget(self.class_combo)
        buttons_layout.addWidget(self.results_button)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Фамилия', 'Результат', 'Логин'])
        # запрет на редактирование для всей таблицы
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.table)

    def load_file_dialog(self):
        """ Открывает диалог выбора файла и загружает его """
        try:
            file_path, _ = QFileDialog.getOpenFileName(
                self,  # родительское окно
                'Выберите файл с результатами олимпиады',  # заголовок диалога
                '',  # начальная директория
                '*.csv')  # фильтр файлов

            # если файл выбран
            if file_path:
                self.load_file(file_path)

        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Ошибка при выборе файла: {str(e)}')

    def load_file(self, file_path):
        """ Загружает данные из указанного файла """
        try:
            # очистка предыдущих данных
            self.data.clear()

            with open(file_path, 'r', encoding='utf-8') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # пропуск заголовков

                for row in csv_reader:
                    user_name = row[1]
                    score = int(row[7])

                    name_parts = user_name.split()

                    school = name_parts[1]
                    class_num = name_parts[2]
                    surname = name_parts[3]

                    self.data.append({
                        'user_name': user_name,
                        'surname': surname,
                        'score': score,
                        'school': school,
                        'class': class_num
                    })

            self.update_filter_lists()
            self.apply_filters()

        except FileNotFoundError:
            QMessageBox.critical(self, 'Ошибка', 'Файл не найден')
        except Exception as e:
            QMessageBox.critical(self, 'Ошибка', f'Не удалось загрузить файл: {str(e)}')

    def update_filter_lists(self):
        """ Обновление выпадающих списков """
        schools = set(student['school'] for student in self.data)
        self.school_combo.clear()
        self.school_combo.addItem('Все')
        for school in sorted(schools, key=int):
            self.school_combo.addItem(school)

        classes = set(student['class'] for student in self.data)
        self.class_combo.clear()
        self.class_combo.addItem('Все')
        for class_num in sorted(classes, key=int):
            self.class_combo.addItem(class_num)

    def apply_filters(self):
        """ Фильтрация """
        selected_school = self.school_combo.currentText()
        selected_class = self.class_combo.currentText()

        self.filtered_data = []

        for student in self.data:
            # проверка соответствия
            school_match = (selected_school == 'Все' or selected_school == student['school'])
            class_match = (selected_class == 'Все' or selected_class == student['class'])
            if school_match and class_match:
                self.filtered_data.append(student)

        self.filtered_data.sort(key=lambda x: x['score'], reverse=True)  # сортировка по баллам
        self.display_data()

    def display_data(self):
        """ Отображение данных в таблице """
        if not self.filtered_data:  # выходим из метода, если нет данных
            return

        self.table.setRowCount(len(self.filtered_data))

        # определение баллов для цветов
        first_place = self.filtered_data[0]['score']
        second_place = None
        for student in self.filtered_data:
            if student['score'] < first_place:
                second_place = student['score']
                break

        third_place = None
        for student in self.filtered_data:
            if student['score'] < second_place:
                third_place = student['score']
                break

        # заполнение таблицы данными
        for row, student in enumerate(self.filtered_data):
            surname = QTableWidgetItem(student['surname'])
            score = QTableWidgetItem(str(student['score']))
            login = QTableWidgetItem(student['user_name'])
            self.table.setItem(row, 0, surname)
            self.table.setItem(row, 1, score)
            self.table.setItem(row, 2, login)

            # применение цветов по баллам
            if student['score'] == first_place:
                color = QColor(255, 215, 0)  # золотой
            elif second_place is not None and student['score'] == second_place:
                color = QColor(192, 192, 192)  # серебряный
            elif third_place is not None and student['score'] == third_place:
                color = QColor(205, 127, 50)  # бронзовый
            else:
                continue

            # установка цвета фона для всей строки
            for col in range(3):
                self.table.item(row, col).setBackground(color)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OlympiadResults()
    window.show()
    sys.exit(app.exec())