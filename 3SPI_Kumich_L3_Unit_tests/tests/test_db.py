import pytest


class TestDatabase:
    def test_database_creation(self, temp_db):
        contacts = temp_db.get_contacts()
        assert contacts == []

    @pytest.mark.parametrize("name,phone,city", [
        ("Алексеев Алексей", "+79160000001", "Москва"),
        ("Борисов Борис", "+79160000002", "Санкт-Петербург"),
        ("Васильев Василий", "+79160000003", "Казань"),
    ])
    def test_add_contact_parametrized(self, temp_db, name, phone, city):
        result = temp_db.add_contact(name, phone, city)
        assert result is True

        contacts = temp_db.get_contacts()
        assert len(contacts) == 1
        assert contacts[0]["full_name"] == name
        assert contacts[0]["phone"] == phone
        assert contacts[0]["city"] == city

    def test_duplicate_phone(self, temp_db):
        temp_db.add_contact("Первый", "+79161111111", "Москва")
        result = temp_db.add_contact("Второй", "+79161111111", "Казань")

        assert result is False  # должна быть ошибка уникальности

    def test_get_all_contacts(self, temp_db, sample_data):
        # добавляем несколько контактов
        for contact in sample_data:
            temp_db.add_contact(contact["name"], contact["phone"], contact["city"])

        contacts = temp_db.get_contacts()
        assert len(contacts) == len(sample_data)

        # проверяем порядок и содержимое
        for i in range(len(sample_data)):
            assert contacts[i]["full_name"] == sample_data[i]["name"]
            assert contacts[i]["phone"] == sample_data[i]["phone"]
            assert contacts[i]["city"] == sample_data[i]["city"]

    def test_update_contact(self, temp_db):
        # добавляем контакт
        temp_db.add_contact("Старое имя", "+79161111111", "Старый город")
        contacts = temp_db.get_contacts()
        contact_id = contacts[0]["id"]

        # обновляем
        result = temp_db.update_contact(
            contact_id,
            "Новое имя",
            "+79162222222",
            "Новый город"
        )
        assert result is True

        # проверяем
        updated = temp_db.get_contacts()[0]
        assert updated["full_name"] == "Новое имя"
        assert updated["phone"] == "+79162222222"
        assert updated["city"] == "Новый город"

    def test_update_nonexistent(self, temp_db):
        result = temp_db.update_contact(
            999,  # несуществующий ID
            "Имя",
            "+79160000000",
            "Город"
        )
        assert result is False

    def test_delete_contact(self, temp_db):
        # добавляем
        temp_db.add_contact("Удалить", "+79163333333", "Город")
        contacts = temp_db.get_contacts()
        contact_id = contacts[0]["id"]

        # удаляем
        result = temp_db.delete_contact(contact_id)
        assert result is True
        assert len(temp_db.get_contacts()) == 0

    def test_delete_nonexistent(self, temp_db):
        result = temp_db.delete_contact(999)
        assert result is False