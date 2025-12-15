import pytest
from app.db import Database
from PyQt6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
        app.setQuitOnLastWindowClosed(False)
    yield app


@pytest.fixture
def temp_db():
    db = Database(":memory:")
    db.connect()
    db.setup()
    yield db
    db.close()


@pytest.fixture
def sample_data():
    return [
        {"name": "Иванов Иван Иванович", "phone": "+79161234567", "city": "Москва"},
        {"name": "Петрова Анна Сергеевна", "phone": "+79269876543", "city": "Санкт-Петербург"},
        {"name": "Сидоров Алексей", "phone": "+79361234567", "city": "Казань"},
    ]