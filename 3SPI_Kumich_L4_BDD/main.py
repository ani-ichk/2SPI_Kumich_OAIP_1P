import sys
from PyQt6.QtWidgets import QApplication
from cat_db import CatDatabase
from cat_gui import CatWindow


def main():
    app = QApplication(sys.argv)

    db = CatDatabase(":memory:")

    # несколько тестовых котов
    db.add_cat("Барсик", 3, "британец", "серый")
    db.add_cat("Шурик", 2, "дворовая", "черный")
    db.add_cat("Вася", 5, "сиамский", "кремовый")

    window = CatWindow(db)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()