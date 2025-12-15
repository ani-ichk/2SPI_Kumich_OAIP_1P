import pytest
from app.addDataWin import AddDataWindow


class TestAddWindow:
    def test_add_window_initialization(self, temp_db, qtbot):
        window = AddDataWindow(temp_db)
        qtbot.addWidget(window)
        assert window.windowTitle() == "Добавление контакта"

    @pytest.mark.parametrize("name,phone,city,expected", [
        ("", "+79161111111", "Москва", False),
        ("Иван", "", "Москва", False),
        ("Иван", "+7916", "", False),
        ("Иван", "+79161234567", "Москва", True),
    ])
    def test_validation_cases(self, temp_db, qtbot, name, phone, city, expected):
        window = AddDataWindow(temp_db)
        qtbot.addWidget(window)

        window.name_input.setText(name)
        window.phone_input.setText(phone)
        window.city_input.setText(city)

        result = window.validate()
        assert result == expected

    def test_save_new_contact_success(self, temp_db, qtbot):
        window = AddDataWindow(temp_db)
        qtbot.addWidget(window)

        window.name_input.setText("Петров Петр")
        window.phone_input.setText("+79269876543")
        window.city_input.setText("Казань")

        window.save()
        contacts = temp_db.get_contacts()
        assert len(contacts) == 1
        assert contacts[0]["full_name"] == "Петров Петр"

    def test_save_duplicate_phone(self, temp_db, qtbot):
        temp_db.add_contact("Первый", "+79161111111", "Москва")
        window = AddDataWindow(temp_db)
        qtbot.addWidget(window)

        window.name_input.setText("Второй")
        window.phone_input.setText("+79161111111")
        window.city_input.setText("Казань")

        window.save()
        contacts = temp_db.get_contacts()
        assert len(contacts) == 1
        assert contacts[0]["full_name"] == "Первый"