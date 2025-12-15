from PyQt6.QtCore import Qt
from app.viewDataWin import ViewDataWindow


class TestViewWindow:
    def test_window_creation(self, temp_db, qtbot):
        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)
        assert window.windowTitle() == "Список контактов"
        assert window.table is not None

    def test_table_headers(self, temp_db, qtbot):
        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)

        headers = []
        for i in range(window.table.columnCount()):
            header_item = window.table.horizontalHeaderItem(i)
            if header_item:
                headers.append(header_item.text())

        expected_headers = ["ID", "ФИО", "Телефон", "Город"]
        assert headers == expected_headers

    def test_empty_database(self, temp_db, qtbot):
        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)
        assert window.table.rowCount() == 0

    def test_table_with_data(self, temp_db, qtbot, sample_data):
        for contact in sample_data:
            temp_db.add_contact(
                contact['name'],
                contact['phone'],
                contact['city']
            )

        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)
        assert window.table.rowCount() == len(sample_data)

    def test_buttons_exist(self, temp_db, qtbot):
        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)
        assert hasattr(window, 'delete_btn') is True
        assert hasattr(window, 'refresh_btn') is True
        assert window.delete_btn.text() == "Удалить контакт"
        assert window.refresh_btn.text() == "Обновить"

    def test_refresh_button(self, temp_db, qtbot):
        window = ViewDataWindow(temp_db)
        qtbot.addWidget(window)

        temp_db.add_contact("Новый", "+79161111111", "Москва")
        qtbot.mouseClick(window.refresh_btn, Qt.MouseButton.LeftButton)
        assert window.table.rowCount() == 1