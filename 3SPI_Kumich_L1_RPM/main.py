class DatabaseConnection:
    instance = None # место для хранения единичного объекта

    def __new__(cls, *args, **kwargs):
        """
        Вызывается ПЕРЕД созданием об-та (контролирует создание об-та)
        Ссылается на класс
        """
        # возвращаем существующий экземпляр или создаем новый
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        """
        Вызывается ПОСЛЕ созданием об-та (инициализирует об-т)
        Ссылается на экземпляр
        """
        if not hasattr(self, 'initialized'): # есть ли у об-та атрибут "initialized"
            self.connection = False # флаг подключения
            self.initialized = True # флаг инициализации

    def get_connection(self):
        # подключение к бд
        if not self.connection:
            self.connection = True
        print('\033[32mПодключение к базе данных установлено \033[0m')

    def close_connection(self):
        # закрывает подключение к бд
        if self.connection:
            self.connection = False
        print('\033[31mПодключение к базе данных закрыто \033[0m')


if __name__ == "__main__":
    # первое подключение
    db1 = DatabaseConnection()
    conn1 = db1.get_connection()
    print(f'DB1 ID: {id(db1)}, connection ID: {id(conn1)}')

    # второе подключение - должно вернуть тот же об-т
    db2 = DatabaseConnection()
    conn2 = db2.get_connection()
    print(f'DB2 ID: {id(db2)}, connection ID: {id(conn2)}')

    # проверяем, что это один и тот же об-т
    print(f'Один и тот же объект DatabaseConnection? {db1 is db2}')
    print(f'Одно и то же подключение? {conn1 is conn2}')

    # закрываем подключение
    db1.close_connection()