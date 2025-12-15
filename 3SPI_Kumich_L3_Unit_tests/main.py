import sys
from PyQt6.QtWidgets import QApplication
from app.mainWin import MainWindow
from app.db import Database


def main():
    app = QApplication(sys.argv)

    db = Database("contacts.db")
    db.connect()
    db.setup()

    window = MainWindow(db)
    window.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()