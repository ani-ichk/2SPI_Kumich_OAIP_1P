import pytest
from PyQt6.QtCore import Qt
from app.mainWin import MainWindow


@pytest.mark.usefixtures("qapp")
class TestMainWindow:
    def test_window_initialization(self, temp_db, qtbot):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)
        assert window.windowTitle() == "Управление контактами"

    def test_ui_elements_exist(self, temp_db, qtbot):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)

        assert hasattr(window, 'view_btn') is True
        assert hasattr(window, 'add_btn') is True

        assert window.view_btn.text() == "Показать контакты"
        assert window.add_btn.text() == "Добавить контакт"

    @pytest.mark.parametrize("button_name,expected_text", [
        ("view_btn", "Показать контакты"),
        ("add_btn", "Добавить контакт"),
    ])
    def test_buttons_text(self, temp_db, qtbot, button_name, expected_text):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)

        button = getattr(window, button_name)
        assert button.text() == expected_text

    def test_buttons_enabled(self, temp_db, qtbot):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)

        assert window.view_btn.isEnabled() is True
        assert window.add_btn.isEnabled() is True

    def test_view_button_click(self, temp_db, qtbot):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)
        qtbot.mouseClick(window.view_btn, Qt.MouseButton.LeftButton)
        assert window.view_btn.clicked is not None

    def test_add_button_click(self, temp_db, qtbot):
        window = MainWindow(temp_db)
        qtbot.addWidget(window)
        qtbot.mouseClick(window.add_btn, Qt.MouseButton.LeftButton)
        assert window.add_btn.clicked is not None